#!/usr/bin/expect -f

#Puts you directly into Magellan machines to interact
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
# update which machine you want to log into (magellan2, magellan3 etc.)
send "ssh ****@magellan*.icrar.org
"
expect "*assword: "
send "PUT_UR_PASSWORD_HERE\r"
expect "$ "

# cd into whatever file you need next
send "cd grapepkg1.2.1/run.dir
"

send "tail ttt1
"

interact
