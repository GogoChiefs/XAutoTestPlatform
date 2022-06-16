#!/bin/bash
ldapmodify -x -H ldap://127.0.0.1:31001 -D "cn=XDMadmin,cn=config" -w XDMadminconfig -f modifyCachePolicy.ldif