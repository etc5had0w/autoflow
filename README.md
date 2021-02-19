
# Autoflow - Windows Stack Based Auto Buffer Overflow Exploiter

Autoflow is a tool that exploits windows stack based buffer overflow automatically.

By reducing human efforts, Autoflow works flawlessly and performs all the steps involved in a buffer overflow attack.

Autoflow works on Interative Command Line Inteface and simplies the whole attack process.

Its Highly Recommended that you should already know the process of manual buffer overflow attack.

Autoflow needs only these inputs to function :

* IP Address of Target.
* Port Number Where Vulnarable Application is Active.
* Vulnarable Command
* EIP Register Value (Only Asked During EIP Overwrite Phase)
* Bad Characters
* Your LHOST and LPORT whew you want to spawn the shell
* JMP ESP Address


Meanwhile you will only have to provide inputs and the tool will perform all the tasks involved by itself.

The tool will ask you to perform small actions when needed.

Debugger is something that works on client side so the user needs to perform some tasks that are beyond the limits of this tool as of now.


Overall the idea behind building this tool is to perform the stack based buffer overflow attack in a small amount of time and without taking any hassle of manually performing everything.


## Requirements

* Kali Linux OS

* msfvenom (Included with metasploit)

* pattern_create.rb (Included with metasploit)

* pattern_offset.rb (Included with metasploit)

* netcat

* python2.7 with socket, time, sys, subprocess, os modules.

* Immunity Debbuger on client side


## How To Install Autoflow ?

```
git clone

cd autoflow/

chmod +rwx setup.sh

sudo ./setup.sh


```
## How To Run Autoflow ?

run this command from your console from the autoflow folder :

```
./autoflow
```

Note : Make sure you execute Autoflow only from the Autoflow Folder.

## Features

Autoflow performs these tasks automatically :

* 1.Fuzzing

* 2.Offset Matching

* 3.EIP Register Overwriting

* 4.Seding Intended Buffer for Bad Character Detection

* 5.Generating Payload For Reverse Shell

* 6.Sending Malicious Buffer to Spawn a Reverse Shell


## How to use Autoflow :

Here is a small video tutorial for Autoflow :





