#!/usr/bin/python2.7

#from httplib import HTTP
#from urlparse import urlparse
from bcolor import bcolors
import urllib

DownloadList=[]
DownloadSize=[0]

def checkURL(url):
     '''
     p = urlparse(url)
     h = HTTP(p[1])
     h.putrequest('HEAD', p[2])
     h.endheaders()
     if h.getreply()[0] == 200:
	DownloadList.append(url)
	print bcolors.OKGREEN + "OK! this file is ok ;) : "+ url +""+ bcolors.ENDC
	print h.getheaders(Content-Length)
	return 1
     '''
 #    try:
     File = urllib.urlopen(url)
     meta = File.info()
     DownloadList.append(url)
     print bcolors.OKGREEN + "OK! this file is ok ;) : "+ url +""+ bcolors.ENDC
     DownloadSize[0] = DownloadSize[0] + (int)(meta.getheaders("Content-Length")[0])
     #except: 
#	print bcolors.FAIL + "sry man! use pacman -Syu or change you'r mirror! : "+ url +""+ bcolors.ENDC
#	return 0

