#!/usr/bin/expect -f

#Puts you directly into Plieadies to interact
spawn ssh mmckenzie@inter.icrar.org
expect "*assword: "
send "PUT_UR_PASSWORD_HERE\r"
expect "$ "

send "ssh mmckenzie@uwa-inter.icrar.org
"
expect "*assword: "
send "PUT_UR_PASSWORD_HERE\r"
expect "$ "

# Put what machine you want to log onto (blocked out for github upload)
send "ssh ****@magellan2.icrar.org
"
expect "*assword: "
send "PUT_UR_PASSWORD_HERE\r"
expect "$ "

send "cd grapepkg1.2.1/run.dir/runggc1.dir
"

send "tail ttt1
"

interact
