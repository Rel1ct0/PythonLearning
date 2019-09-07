#!/usr/bin/python3

print("How many routers do you have?")
routers_num = int(input())

if (routers_num <= 0):
	print("Nothing to do here")
	exit()

AllLinks = []

router = 0
while (router < routers_num - 1):
	secondrouter = router + 1
	while (secondrouter < routers_num):
		print("How many links do you have between R" + str(router+1) + " and R" + str(secondrouter+1) + "?")
		links_num = int(input())
		link = 0
		while (link < links_num):
			NewLink = []
			print("Link " + str(link+1) + ":")
			print("Input IP address of R" + str(router+1))
			firstaddress = input()
			NewLink.append([router , firstaddress])
			print("Input IP address of R" + str(router+2))
			secondaddress = input()
			NewLink.append([secondrouter , secondaddress])
			print("Input netmask")
			netmask = input()
			NewLink.append(netmask)
			link = link +1
		AllLinks.append(NewLink)
		secondrouter = secondrouter + 1
	router = router + 1
print(AllLinks)

	