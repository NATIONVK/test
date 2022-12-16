#!/usr/bin/python3
#-*- coding: utf-8 -*-
#marshal py3

'''
PyMarshal - Compile Python Script
This project was created by Dfv47 with Black Coder Crush. 
Copyright 12 - 07 - 2k19 @m_d4fv
'''

try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '2':
        exit("[sorry] use python version 3")
       
import os
import time
os.system("xdg-open https://www.facebook.com/DEVIL.NAJMUL")
time.sleep(1)
os.system('clear')
print("\033[1;31m TOOL IS OPENING :")


animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["\033[0;93m[■□□□□□□□□□]","\033[0;94m[■■□□□□□□□□]", "\033[0;92m[■■■□□□□□□□]", "\033[0;91m[■■■■□□□□□□]", "\033[0;97m[■■■■■□□□□□]", "\033[0;32m[■■■■■■□□□□]", "\033[0;94m[■■■■■■■□□□]", "\033[0;93m[■■■■■■■■□□]", "\033[0;91m[■■■■■■■■■□]", "\033[0;92m[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


os.system("xdg-open https://www.facebook.com/groups/2282442651904924/")
time.sleep(1)

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy3 = """
\033[1;32m╔══════════════════════════════════════════════════════════╗\033[1;93m
\033[1;32m║	         \033[1;93m ─━㋱ASSALAMUALAIKUM㋱━─\033[1;32m	           ║
\033[1;32m╔══════════════════════════════════════════════════════════╗
\033[1;32m║   \033[1;93m  _____  ________      _______ _ \033[1;32m                      ║
\033[1;32m║   \033[1;93m |  __ \|  ____\ \    / /_   _| |     \033[1;32m                 ║
\033[1;32m║   \033[1;93m | |  | | |__   \ \  / /  | | | |     \033[1;32m                 ║
\033[1;32m║   \033[1;93m | |  | |  __|   \ \/ /   | | | |     \033[1;32m                 ║
\033[1;32m║   \033[1;93m | |__| | |____   \  /   _| |_| |____ \033[1;32m                 ║
\033[1;32m║   \033[1;93m |_____/|______|   \/   |_____|______|\033[1;32m                 ║
\033[1;32m╚══════════════════════════════════════════════════════════╝
\033[1;32m╔══════════════════════════════════╗╔══════════════════════╗
\033[1;32m║NOTE : \033[37;41mTHIS TOOLS IS FREE\033[0;m\033[1;32m         ║║        \x1b[1;91m___T_\033[1;32m         ║
\033[1;32m║══════════════════════════════════║║       \x1b[1;91m| o o |\033[1;32m        ║
\033[1;32m║AUTHOR    : DEVIL NAJMUL          ║║       \x1b[1;91m|__-__|\033[1;32m        ║
\033[1;32m║══════════════════════════════════║║       \x1b[1;91m/| []|'\033[1;32m        ║
\033[1;32m║WHATSAPP  : +8801977073308        ║║     \x1b[1;91m()/|___|\()\033[1;32m      ║
\033[1;32m║══════════════════════════════════║║        \x1b[1;91m|_|_|\033[1;32m         ║
\033[1;32m║GITHUB    : N41M01                ║║       \x1b[1;91m|_| |_|\033[1;32m        ║
\033[1;32m║══════════════════════════════════║║                      ║
\033[1;32m║SERVER    : DATA -  WORKING       ║╚══════════════════════╝
\033[1;32m║══════════════════════════════════════════════════════════╗
\033[1;32m║FACEBOOK LINK : \x1b[1;91mhttps://www.facebook.com/N41M01\033[1;32m           ║
\033[1;32m║══════════════════════════════════════════════════════════║
\033[1;32m║FB PAGE LINK  : \x1b[1;91mhttps://www.facebook.com/DEVIL.NAJMUL\033[1;32m     ║
\033[1;32m╚══════════════════════════════════════════════════════════╝\033[1;37m
""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

os.system('clear')
try:
    print(bannerpy3)
    print (y+' ['+w+'#'+y+'] '+w+'\033[0;93m➣Example '+y+':'+w+'\033[0;94m /sdcard/DEVIL.py\n')
    file = input(y+' ['+w+'?'+y+'] '+w+'Input Your File Location'+y+' :'+w+' ')
    print()
    nn = input(y+' ['+w+'?'+y+'] '+w+'\033[0;92mInter Output File Name'+y+' :'+w+' ')
    o = nn.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print (r+'\n ['+w+'!'+r+'] '+r+'[ '+w+'Error '+r+'] '+w+'No such file or directory '+r+': '+w+'"'+file+'"\n')
        os.system("xdg-open https://github.com/N41M01")
        sys.exit()
    try:
        code = compile(strng,'','exec')
        data = marshal.dumps(code)
    except TypeError:
        print (R + '   ['+W+'!'+R+'] '+R+'[ '+W+'File already to compiled\n') 
        sys.exit()

fileout = open(o + '.py', 'w')
fileout.write('#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
fileout.write('#Compiled By DEVIL\n')
fileout.write('#github : https://github.com/N41M01\n')
fileout.write('#Facebook : https://www.facebook.com/DEVIL.NAJMUL\n')
fileout.write('#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(3)
os.system('clear')
print(bannerpy3)
print('\033[0;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print ('This Tool Made By DEVIL')
print('\033[0;92mOwner Fb : DEVIL NAJMUL')
print ('Source File : '+file)
print (y+'\n ['+w+'+'+y+'] '+w+'File succes to compile   '+y+': ' + w + o + '.py')
print('\033[0;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

