#!/usr/bin/python3

print("How many routers do you have?")
routers_num = int(input())

if (routers_num <= 0):
	print("Nothing to do here")
	exit()

AllLinks = []

for router in range(0, routers_num - 1):
	for secondrouter in range(router+1, routers_num):
		print("How many links do you have between R" + str(router+1) + " and R" + str(secondrouter+1) + "?")
		links_num = int(input())
		for link in range (0, links_num):
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
			print("Input cost")
			cost = int(input())
			NewLink.append(cost)
		AllLinks.append(NewLink)
print(AllLinks)

	