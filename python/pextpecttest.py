import pexpect
import sys
server_ip = "server ip"
server_user = "username"
server+pass = "password"
child = pexpect.spawn('ssh %s@%s' % (server_user, server_ip))
child.timeout = 60
child.expect("password:")
child.sendline(server_pass)
child.expect ('#')
child.sendline("show user-session")
child.expect ('#')
print(child.before)
child.sendline ("scope chassis")
child.expect ("/chassis")
child.sendline ("show psu")
child.expect ("/chassis")
print(child.before)
child.sendline ("exit")
child.expect ('#')
child.sendline ("exit")

