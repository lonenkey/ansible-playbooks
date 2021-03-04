import paramiko
import time

ssh = parmiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ipaddress', username='username',password='password')

chan = ssh.invoke_shell()
chan.send('show version\r')
while not chan.recv_ready():
	time.sleep(5)
out = chan.recv(99999)
print (out.decode("ascii"))

chan.send('scope chassis\r')
chan.send('show psu\r')

while not chan.recv_ready():
	time.sleep(5)
out = chan.rev(99999)
print (out.decode("ascii"))

ssh.close()
