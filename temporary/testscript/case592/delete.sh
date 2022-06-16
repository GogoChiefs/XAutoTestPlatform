#!/bin/bash
ldapdelete -x -H ldap://127.0.0.1:31001 -D "cn=directory manager,dc=ct" -w secret -f delete.ldif