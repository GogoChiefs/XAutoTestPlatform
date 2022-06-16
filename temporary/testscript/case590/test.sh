#!/bin/bash

#先清一遍数据
sh delete.sh  > nohup.out

#导入自定义测试数据
ldapadd -c -x -H ldap://127.0.0.1:31001 -D "cn=directory manager,dc=ct" -w secret -f import.ldif > nohup.out

res=`expect exop.sh | awk -F ":" '$1=="data" {getline;print $0}' | sed 's/\r//g'`

sh delete.sh  > nohup.out

echo '"'${res}'"'