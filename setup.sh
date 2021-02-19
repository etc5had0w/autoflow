#!/bin/bash
echo "[*] Setting Right Permissions..."
chmod +rwx autoflow.py espconvert.sh payloader.sh esp.py payload.py
echo "[*] Checking Availability of Tools..."
if [[ -f "/usr/share/metasploit-framework/tools/exploit/pattern_create.rb" ]]
then
    echo "[+] pattern_create.rb is installed and  present at correct directory."
fi
if [[ -f "/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb" ]]
then
    echo "[+] pattern_offset.rb is installed present at correct directory."
fi
which msfvenom | grep -o msfvenom > /dev/null &&  echo "[+] msfvenom is installed." || echo "[+] msfvenom is not installed. Please Install it before running Autoflow."
which nc | grep -o nc > /dev/null &&  echo "[+] netcat is installed."|| echo "[+] netcat is not installed. Please Install it before running Autoflow."
which python | grep -o python > /dev/null &&  echo "[+] python is installed." || echo 1 "[+] python is not installed. Please Install it before running Autoflow."
echo "[+] Setup Finished Successfullly."