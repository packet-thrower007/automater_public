import urllib.request
import re

USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Geko) Chrome/83.0.4103.101 Mobile Safari/537.26'

url = input("Enter URL: ")
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', USER_AGENT)]

urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html_content = response.read()

pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9._]+.[-a-zA-Z0-9._]")

mails = re.findall(pattern,str(html_content))

print(mails)
