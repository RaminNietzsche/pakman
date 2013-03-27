from bcolor import bcolors
import urllib
import Config

CHECKURL = Config.CHECKURL

DownloadList=[]
DownloadSize=[0]

def checkURL(url):
   try:
     if CHECKURL:
     	File = urllib.urlopen(url)
     	meta = File.info()
     	print bcolors.OKGREEN + "OK! this file is ok ;) : "+ url +""+ bcolors.ENDC
     	DownloadSize[0] = DownloadSize[0] + (int)(meta.getheaders("Content-Length")[0])
     DownloadList.append(url)
   except: 
	print bcolors.FAIL + "sry man! use pacman -Syu or change you'r mirror! : "+ url +""+ bcolors.ENDC
	return 0

