#!/bin/bash
#ldapsearch -x -H ldap://127.0.0.1:31001 -D "cn=XDMadmin,cn=config" -w XDMadminconfig -b cn=config objectclass=olcbdbconfig
#ldapsearch -x -H ldap://127.0.0.1:31001 -D "cn=XDMadmin,cn=config" -w XDMadminconfig -b cn=config objectclass=olcbdbconfig | grep olcDbCachePolicy | awk {'print $2'}

#删除自定义测试数据
sh truncate.sh > nohup.out

#导入自定义测试数据
ldapadd -c -x -H ldap://127.0.0.1:31001 -D "cn=directory manager,dc=ct" -w secret -f import.ldif > nohup.out

#动态修改cachepolicy=1
#ldapmodify -x -H ldap://127.0.0.1:31001 -D "cn=XDMadmin,cn=config" -w XDMadminconfig -f modifyCachePolicy.ldif
sh modifyCachePolicy.sh  > nohup.out

#开多进程分别进行search、modify、delete、add操作
nohup sh add.sh  > nohup.out &
nohup sh delete.sh  > nohup.out &
nohup sh modify.sh  > nohup.out &
nohup sh search.sh  > nohup.out &

sleep 10

#查询olmBDBEntryCache
entryCache=`ldapsearch -x -H ldap://127.0.0.1:31001 -D "cn=directory manager,dc=ct" -w secret -b cn=monitor -s sub monitoredinfo=bdb + | grep olmBDBEntryCache | awk {'print $2'}`

#查询olmBDBIDLCache
idlCache=`ldapsearch -x -H ldap://127.0.0.1:31001 -D "cn=directory manager,dc=ct" -w secret -b cn=monitor -s sub monitoredinfo=bdb + | grep olmBDBIDLCache | awk {'print $2'}`

#删除自定义测试数据
sh truncate.sh > nohup.out

#组合结果集
echo '{"olmBDBEntryCache":"'${entryCache}'","olmBDBIDLCache":"'${idlCache}'"}'