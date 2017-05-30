import os
import getpass
import json
import requests
import cookielib
import urllib
import urllib2
import gzip
import StringIO
import time

import data_encode

class SinaClient(object):

	def __init__(self, username = None, password = None):
		self.username = username
		self.password = password

		#some other important parameter for rsa
		self.servertime = None
		self.nonce = None
		self.public_key = None
		self.rsakv = None

		#parameters for post request
		self.post_data = None
		self.headers = data_encode.headers

		#session info
		self.cookiejar = None
		self.session = None

		#status
		self.status = False


	def set_account(self, username, password):
		if username is None or password is None:
			return
		self.username = username
		self.password = password

	def set_post_data(self):
		self.servertime, self.nonce, self.pubkey, self.rsakv = data_encode.get_prelogin_info()
		self.post_data = data_encode.encode_post_data(self.username, self.password, self.servertime, self.nonce, self.pubkey, self.rsakv)

	def login(self, username=None, password = None):

		self.set_account(username, password)
		self.set_post_data()

		login_url = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
		session = requests.Session()
		response = session.post(login_url, data = self.post_data)
		json_text = response.content.decode('gbk')
		res_info = json.loads(json_text)
		try:
			if res_info['retcode'] == '0':
				print('Login successfully!')
				self.status = True
				#add cookies to headers
				cookies = session.cookies.get_dict()
				cookies = [key + '=' +value for key, value in cookies.items()]
				cookies = '; '.join(cookies)
				session.headers['Cookie'] = cookies
			else:
				print('Failed to login! |'+res_info['reason'])
		except Exception as e:
			print('Loading error --> '+e)

		self.session = session
		return session

def testLogin():
	client = SinaClient()
	username = raw_input("Please input username: ")
	password = getpass.getpass("Please input your password: ")   
	session = client.login(username, password)

if __name__ is '__main__':
	testLogin()