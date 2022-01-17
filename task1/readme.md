# Task 1
The NSA Cybersecurity Collaboration Center has a mission to prevent and eradicate threats to the US Defense Industrial Base (DIB). Based on information sharing agreements with several DIB companies, we need to determine if any of those companies are communicating with the actor's infrastructure.

You have been provided a capture of data en route to the listening post as well as a list of DIB company IP ranges. Identify any IPs associated with the DIB that have communicated with the LP.

Downloads:
- Network traffic heading to the LP (capture.pcap)
- DIB IP address ranges (ip_ranges.txt)

## Solution
1. taking the ip_ranges.txt, use tshark to extract the unique ip addresses

    `tshark -r capture.pcap -T fields -e ip.src | sort | uniq > output.csv`

    b. make sure to get rid of the malicious LP (10.120.14.143)

2. from there, make a script that will go through each of the ips and using ipaddress library and csv library, check to see if any of the ip subnets noted in the ip_ranges.txt 

3. output of the file

    ```
    192.168.19.21
    198.18.79.146
    198.19.39.130
    198.19.206.53
    ```


## Alternate way to solve
1. go into vim -> visual block mode to add the filter

    ```
    ip.src==198.18.152.0/23
    || ip.src==10.226.176.0/21
    || ip.src==192.168.20.128/25
    || ip.src==10.36.0.0/18
    || ip.src==10.147.88.0/22
    || ip.src==192.168.19.0/27
    || ip.src==198.19.122.144/28
    || ip.src==198.18.23.160/29
    || ip.src==10.198.78.0/26
    || ip.src==10.147.176.0/22
    || ip.src==10.244.177.128/26
    || ip.src==10.44.192.0/20
    || ip.src==10.28.176.0/20
    || ip.src==10.0.0.0/18
    || ip.src==198.19.39.128/25
    || ip.src==198.18.79.144/28
    || ip.src==10.57.162.0/24
    || ip.src==198.19.246.160/27
    || ip.src==192.168.131.0/28
    || ip.src==10.201.15.0/24
    || ip.src==198.18.92.136/29
    || ip.src==198.19.206.0/25
    || ip.src==10.254.178.104/29
    || ip.src==10.47.0.0/16
    || ip.src==10.233.93.0/24
    || ip.src==10.246.32.0/19
    !(ip.src==10.120.14.143)
    ```
2. Go into wireshark and paste that input in the filter field

3. go into statistics (from the menu bar) -> endpoints -> check the "limit to display filter" -> go to IPv4 tab -> IPs are there!
