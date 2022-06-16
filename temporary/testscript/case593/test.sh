#!/bin/bash

#先清一遍数据
sh delete.sh  > nohup.out

#导入自定义测试数据
ldapadd -c -x -H ldap://127.0.0.1:31001 -D "cn=directory manager,dc=ct" -w secret -f import.ldif > nohup.out

res=`expect exop.sh | sed -n '8p' | sed -e 's/\r//g'`

echo '"'${res}'"'