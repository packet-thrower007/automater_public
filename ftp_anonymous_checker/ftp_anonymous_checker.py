import ftplib


def anonymouslogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		response = ftp.login('anonymous', 'anonymous')
		if "230 Anonymous access granted" in response:
			print('\n[*] ' + str(hostname) +' FTP Anonymous Login Succeeded.')
			print(ftp.getwelcome())
			ftp.dir()
	except Exception as exception:
		print(str(exception))
		print('\n[-] ' + str(hostname) +' FTP Anonymous Login Failed.')


hostname = '8.8.8.8'

anonymouslogin(hostname)
