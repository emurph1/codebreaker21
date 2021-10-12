import ipaddress
import csv

ips = ["198.18.152.0/23",
"10.226.176.0/21",
"192.168.20.128/25",
"10.36.0.0/18",
"10.147.88.0/22",
"192.168.19.0/27",
"198.19.122.144/28",
"198.18.23.160/29",
"10.198.78.0/26",
"10.147.176.0/22",
"10.244.177.128/26",
"10.44.192.0/20",
"10.28.176.0/20",
"10.0.0.0/18",
"198.19.39.128/25",
"198.18.79.144/28",
"10.57.162.0/24",
"198.19.246.160/27",
"192.168.131.0/28",
"10.201.15.0/24",
"198.18.92.136/29",
"198.19.206.0/25",
"10.254.178.104/29",
"10.47.0.0/16",
"10.233.93.0/24",
"10.246.32.0/19"]

ranges = []
for ip in ips:
	ranges.append(ipaddress.IPv4Network(ip))

with open('output.csv', 'rt') as f:
	reader = csv.reader(f)
	for i in reader:
		if any(ipaddress.IPv4Address(i[0]) in x for x in ranges):
			print(i[0])
			
			

