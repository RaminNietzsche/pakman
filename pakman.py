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


DownloadList=[]
DownloadSize=[0]

MAXTHREAD = 8

def DownloadUrl(url):
    p = subprocess.Popen(["axel -a "+ url], shell=True)

def main(argv):
    if argv[1] == "-Syu":
    	p = subprocess.Popen(["pacman -Syup | tac | head -n -5"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else:
    	p = subprocess.Popen(["pacman -Sp "+ argv[1]], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
    	if CheckUrl.checkURL(line) == 0:
	    return
    print CheckUrl.DownloadList
    print CheckUrl.DownloadSize
    for item in CheckUrl.DownloadList:
	print item
	while threading.activeCount() >= MAXTHREAD+1:
	     pass
	GoGoGo = Thread(target=DownloadUrl, args=(item,))
    	GoGoGo.start()


if __name__ == '__main__':
    import sys
    main(sys.argv)

