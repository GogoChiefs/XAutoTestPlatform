import sys
import os
import paramiko
import time
from common.LogUtil import LogUtil

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
log = LogUtil()


class SSHUtil:
    def __init__(self, ip, port, username, passwd):
        self.ip = ip
        self.port = port
        self.username = username
        self.passwd = passwd
        self.client = None
        self.transport = None
        self.sftp = None

    def connect(self):
        print("startconnect")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(hostname=self.ip, port=self.port, username=self.username, password=self.passwd)

        transport = paramiko.Transport((self.ip, self.port))
        transport.connect(username=self.username, password=self.passwd)
        self.client = client
        self.transport = transport
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def close(self):
        if self.client is not None:
            self.client.close()

        if self.transport is not None:
            self.transport.close()

    def exec(self, command):
        # print(command)
        stdin, stdout, stderr = self.client.exec_command(command)
        # print('stdout: ', stdout.read().decode('utf-8'))
        # print('stderr: ', stderr.read().decode('utf-8'))
        if stdout is not None:
            return stdout

        if stderr is not None:
            return stderr

    """
    递归上传localpath中的文件到服务器
    """

    def upload(self, localpath, remotepath):

        if (os.path.isfile(localpath)):
            # localpath指向一个文件，直接上传文件
            self.sftp.put(localpath, remotepath)
        else:
            # localpath指向一个路径，在remotePath中创建以该路径名的目录，并上传路径下所有目录
            fatPath = os.path.split(localpath)[0]
            for root, dirs, files in os.walk(localpath):
                workdir = remotepath + root.replace(fatPath, "")
                # TODO:为啥不用sftp.rmdir?因为它不支持递归删除，后面自己实现递归删除再换
                # self.sftp.rmdir(workdir)
                if workdir != "/":
                    command = "rm -rf " + workdir + "*"
                    print(command)
                    self.client.exec_command("rm -rf " + workdir + "*")
                    # 为什么要sleep 1?因为上面的方法好像是个异步方法，调试的时候，debug没问题，但是一run疯狂在上传文件时报错说目标路径找不到,很无奈只能sleep
                    time.sleep(1)
                self.sftp.mkdir(workdir)

                for file in files:
                    print(os.path.abspath(os.path.join(root, file)), workdir + os.sep + file)
                    self.sftp.put(os.path.abspath(os.path.join(root, file)), workdir + os.sep + file)

                for dirname in dirs:
                    self.sftp.mkdir(workdir + os.sep + dirname)

    def download(self, localpath, remotepath):
        self.sftp.get(remotepath, localpath)
