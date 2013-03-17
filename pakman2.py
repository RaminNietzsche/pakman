#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------#
#	 ____       _                          					#
#	|  _ \ __ _| | ___ __ ___   __ _ _ __  					#
#	| |_) / _` | |/ / '_ ` _ \ / _` | '_ \ 					#
#	|  __/ (_| |   <| | | | | | (_| | | | |					#
#	|_|   \__,_|_|\_\_| |_| |_|\__,_|_| |_|					#
#										#
#										#
#  Copyright 2013 ramin <ramin.Najjarbashi@Gmail.com>				#
#										#
#  This program is free software; you can redistribute it and/or modify		#
#  it under the terms of the GNU General Public License as published by		#
#  the Free Software Foundation; either version 2 of the License, or		#
#  (at your option) any later version.						#
#										#
#  This program is distributed in the hope that it will be useful,		#
#  but WITHOUT ANY WARRANTY; without even the implied warranty of		#
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the		#
#  GNU General Public License for more details.					#
#										#
#  You should have received a copy of the GNU General Public License		#
#  along with this program; if not, write to the Free Software			#
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,			#
#  MA 02110-1301, USA.								#
#										#
#--------------------------------------------------------------------------------


import subprocess
import CheckUrl
from threading import Thread
import threading
import Config
import signal
import sys
from bcolor import bcolors
import YesNoQ

DownloadList=[]
DownloadSize=[0]

MAXTHREAD = Config.MAXTHREAD

def DownloadUrl(url):
    p = subprocess.Popen(["axel -a "+ url], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print url 

def signal_handler(signal, frame):
        print bcolors.FAIL + 'You pressed Ctrl+C!' + bcolors.ENDC
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size

def main(argv):
     try:
	    print "Loading PKGs list ..."
	    if argv[1] == "-Syu":
    		p = subprocess.Popen(["pacman -Syup | tac | head -n -5"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	    elif argv[1] == "-S" and len(argv) > 2:
	    	p = subprocess.Popen(["pacman -Sp "+ argv[2]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	    elif len(argv) > 2:
		p = subprocess.Popen(["pacman "+ argv[1] +" "+ argv[2]], shell=True, stderr=subprocess.STDOUT)
		exit()
	    else:
                p = subprocess.Popen(["pacman "+ argv[1]], shell=True, stderr=subprocess.STDOUT)
                exit()
	    for line in p.stdout.readlines():
	    	if CheckUrl.checkURL(line) == 0:
		    return
	    #print CheckUrl.DownloadList
	    print "You must download : " + convert_bytes(CheckUrl.DownloadSize[0])
	    if YesNoQ.query_yes_no("Proceed with installation? "):
		for item in CheckUrl.DownloadList:
		     while threading.activeCount() >= MAXTHREAD+1:
		     	pass
		     GoGoGo = Thread(target=DownloadUrl, args=(item,))
    		     GoGoGo.start()
		GoGoGo.join()
	    else:
		print "BYE BYE :D"
		exit(1)
	    if len(sys.argv) == 2:
	    	pacman = subprocess.Popen(["pacman "+ argv[1]], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	    elif len(sys.argv) > 2:
	    	pacman = subprocess.Popen(["pacman -S "+ argv[2]], shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	    else:
	    	print bcolors.FAIL + "invalid args!" + bcolors.ENDC
		exit(1)
	    stdout_data = pacman.communicate(input='y')[0]
            print bcolors.OKBLUE + "FIN! ;) (PA|< Man)" + bcolors.ENDC
     except ValueError:
	    print bcolors.FAIL + "What happend? Report it (Ramin.Najarbashi@Gmail.com)" + bcolors.ENDC

if __name__ == '__main__':
    import sys
    main(sys.argv)

