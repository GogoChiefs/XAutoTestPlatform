#!/usr/bin/expect
spawn ldapexop -x -h 127.0.0.1 -p 31001 -D "cn=directory manager,dc=ct" -W 1.3.6.1.4.1.12900.1.4.4.6:dc=ct
expect "Enter LDAP Password:"
send "secret\r"
expect eof