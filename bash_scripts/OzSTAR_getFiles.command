#!/usr/bin/expect -f
set timeout -1

puts -nonewline "download to folder: "
flush stdout
gets stdin direct
send "cd $direct\r"
send "pwd \n"


puts -nonewline "which OzSTAR folder? "
flush stdout
gets stdin oz_direct


#Download chemo.para
spawn scp mmckenzi@ozstar.swin.edu.au:/home/mmckenzi/$oz_direct/chemo.para $direct/chemo.para
expect "*assword: "
send "SWIN_PASSWORD\r"
expect "$ "

#Download emerge.para
spawn scp mmckenzi@ozstar.swin.edu.au:/home/mmckenzi/$oz_direct/emerge.para $direct/emerge.para
expect "*assword: "
send "SWIN_PASSWORD\r"
expect "$ "

#Download ttt1
spawn scp mmckenzi@ozstar.swin.edu.au:/home/mmckenzi/$oz_direct/ttt1 $direct/ttt1
expect "*assword: "
send "SWIN_PASSWORD\r"
expect "$ "

#Download tout.dat
spawn scp mmckenzi@ozstar.swin.edu.au:/home/mmckenzi/$oz_direct/tout.dat $direct/tout.dat
expect "*assword: "
send "SWIN_PASSWORD\r"
expect "$ "

#Download anim.dat (will continue if not avaliable)
spawn scp mmckenzi@ozstar.swin.edu.au:/home/mmckenzi/$oz_direct/anim.dat $direct/anim.dat
expect "*assword: "
send "SWIN_PASSWORD\r"
expect "$ "

