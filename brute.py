import platform,os,time
os.system('git pull')
os.system('clear')


arc = str(platform.uname().machine)
if 'arm' in arc:
	print('Join Our Facebook Group');time.sleep(2)
	os.system("xdg-open https://www.facebook.com/groups/1247184652736578")
	print('32 bit is old version');time.sleep(2)
	__import__("brute32").login()
elif 'aarch' in arc:
	print('Join Our Facebook Group');time.sleep(2)
	os.system("xdg-open https://www.facebook.com/groups/1247184652736578")
	__import__("brute4").login()

else:
	print('Join Our Facebook Group');time.sleep(2)
	os.system("xdg-open https://www.facebook.com/groups/1247184652736578")
	print('Your Device is not supported')
