#coding=utf-8
from os import system,environ,getlogin,mkdir
from time import sleep,ctime
from shutil import *
from os.path import *
from sys import argv,platform,version,stdout
from urllib.request import urlopen as buka
from random import choice 
from json import load

def main():
	system('clear')
	try:
		print ('\033[94m[\033[91m1\033[94m] \033[92mTambahkan Tombol Termux\n\033[94m[\033[91m2\033[94m] \033[96mInformation\n\033[94m[\033[91m0\033[94m] \033[91mexit')
		nanya = int(input('\033[97m>>> '))
		if nanya == 1:
			tombol()
		elif nanya == 2:
			Info()
		elif nanya == 0:
			exit()
	except ValueError as bulat:
		print ('[!]',bulat)
		sleep(2)
		main()
	except Exception as err:
		print (err)
		
def tombol():
	info = "Tekan CTRL + t untuk buat-sesi\nTekan CTRL + 5 untuk sesi berikutnya\nTekan CTRL + 4 untuk sesi sebelumnya"
	data = "extra-keys = [ ['ESC','|','/','HOME','UP','END','PGUP','DEL'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP']]"
	try:
		print ('\033[94m[\033[91m!\033[94m] \033[93mMembuat Folder')
		try:
			mkdir('/data/data/com.termux/files/home/.termux')
		except:
			pass
		file = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
		print ('\033[94m[\033[91m!\033[94m] \033[93mMembuka',basename(file.name))
		file.write("shortcut.create-session = ctrl + t\n")
		file.write("shortcut.next-session = ctrl + 5\n")
		file.write("shortcut.previous-session = ctrl + 4\n")
		file.write(data)
		file.close()
		try:
			with open('Informasi.txt','w') as my:
				my.write(info)
		except:
			pass
		print ('\033[94m[\033[91m✓\033[94m] \033[93mSukses')
		system('termux-reload-settings')
		print ('\n\033[92mINFO TAMBAHAN')
		print (20* '\033[96m=')
		print (info)
		exit()
	except KeyboardInterrupt:
		exit ('\033[94m[\033[91m!\033[94m] \033[91mExit')
		
def storage():
	anjay = environ["EXTERNAL_STORAGE"]
	try:
		total, used, free = disk_usage(anjay)
		print ('\033[92m[✓] DISK USAGE : ')
		print("   \033[93m- Total: %d GiB" % (total // (2**30)))
		print("   \033[94m- Used: %d GiB" % (used // (2**30)))
		print("   \033[95m- Free: %d GiB" % (free // (2**30)))
	except Exception as err:
		print (err)
		
def info_lainnya():
	data = []
	try:
		for a in environ:
		   data.append(a)
		data.remove('LS_COLORS')
		for b in data:
		   warna = ["\033[91m","\033[92m","\033[93m","\033[94m","\033[95m","\033[96m","\033[97m"]
		   acak =choice(warna)
		   print('\033[92m[✓]',b,':',acak,environ[b])
	except Exception as err:
		print(err)
		
def Info():
	system('clear')
	animasi = ['.   ','..  ','... ']
	for me in animasi:
		print("\r\033[94m[\033[91m!\033[94m] \033[92mMemuat"+me, end = ''),;stdout.flush();sleep(0.1)
	system('clear')
	
	url = "https://api.myip.com"
	ip = []
	try:
		a = buka(url)
		b = load(a)
		c = b['ip']
		ip.append(c)
	except:
		ip.append(None)
	print ('\033[92m[✓] Date : \033[97m',ctime())
	print ('\033[92m[✓] OS   :\033[91m',platform)
	print ('\033[92m[✓] Script :\033[96m',basename(argv[0]))
	print ('\033[92m[✓] python : \033[95m',version[0])
	print ('\033[92m[✓]',get_terminal_size())
	print ('\033[92m[✓] IP     :',ip[0])
	print ('\033[92m[✓] AUTHOR : \033[93mRahmat adha')
	info_lainnya()
	storage()
	print ('\n\033[96m\t___Contact me___')
	print ('  \033[97mEmail    : \033[97mrahmadadha11@gmail.com')
	print ('  \033[97mGithub   : \033[90mMR-X-Junior')
	print ('  \033[97mWhatsApp : \033[92m6285754629509')
	print ('  \033[97mFacebook : \033[94mhttps://www.facebook.com/Anjay.pro098')
	exit()
		
if __name__=="__main__":
	if platform == "'linux2'" or platform == "linux":
		main()
	else:
		exit(f'\033[91mProgram tidak di dukung pada {platform}')