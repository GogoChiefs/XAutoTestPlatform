#!/bin/bash
ldapexop -x -H ldap://127.0.0.1:31001 -D "cn=directory manager,dc=ct" -w secret 1.3.6.1.4.1.12900.1.4.4.6:dc=ct
