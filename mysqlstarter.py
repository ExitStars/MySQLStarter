#-*-coding:utf-8-*-
"""
 _____      _ _   ____  _                 
| ____|_  _(_) |_/ ___|| |_ __ _ _ __ ___ 
|  _| \ \/ / | __\___ \| __/ _` | '__/ __|
| |___ >  <| | |_ ___) | || (_| | |  \__ \
|_____/_/\_\_|\__|____/ \__\__,_|_|  |___/
"""
content = """import os, sys, time
os.system("clear")
print "Loading..."
time.sleep(1)
os.system("mkdir /var/run/mysqld")
os.system("touch /var/run/mysqld")
os.system("ls -lart /var/run/mysqld")
time.sleep(1)
os.system("chown -R mysql /var/run/mysqld")
os.system("ls -lart /var/run/mysqld")
time.sleep(1)
os.system("/etc/init.d/mysql restart")
time.sleep(1)
os.system("clear")
sys.exit(0)"""

def running():
	rcfile = open("/etc/rc.local", "r")
	rccontent = rcfile.read()
	rcfile.close()

	if "python /root/mysqlstarter.py" not in rccontent:
		rccontent = rccontent.replace("exit 0", "")
		result = rccontent+"\npython /root/mysqlstarter.py\nexit 0"
	else:
		result = rccontent

	rcfile = open("/etc/rc.local", "w")
	rcfile.write(result)
	rcfile.close()

def writing():
	stfile = open("/root/mysqlstarter.py", "w")
	stfile.write(content)
	stfile.close()

writing()
running()
