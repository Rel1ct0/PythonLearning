#!/usr/bin/python3

print("How many routers do you have?")
routers_num = int(input())

if (routers_num <= 0):
	print("Nothing to do here")
	exit()

router = 0
while (router < routers_num - 1):
	print("How many links do you have between R" + str(router+1) + " and R" + str(router+2) + "?")
	links_num = int(input())
	link = 0
	while (link < links_num):
		print("Link " + str(link+1) + ":")
		print("Input IP address of R" + str(router+1))
		firstaddress = input()
		print("Input IP address of R" + str(router+2))
		secondaddress = input()
		print("Input netmask")
		netmask = input()
		link = link +1
	router = router + 1