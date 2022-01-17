# Task 5
A forensic analysis of the server you identified reveals suspicious logons shortly after the malicious emails were sent. Looks like the actor moved deeper into OOPS' network. Yikes.

The server in question maintains OOPS' Docker image registry, which is populated with images created by OOPS clients. The images are all still there (phew!), but one of them has a recent modification date: an image created by the Prevention of Adversarial Network Intrusions Conglomerate (PANIC).

Due to the nature of PANIC's work, they have a close partnership with the FBI. They've also long been a target of both government and corporate espionage, and they invest heavily in security measures to prevent access to their proprietary information and source code.

The FBI, having previously worked with PANIC, have taken the lead in contacting them. The FBI notified PANIC of the potential compromise and reminded them to make a report to DC3. During conversations with PANIC, the FBI learned that the image in question is part of their nightly build and test pipeline. PANIC reported that nightly build and regression tests had been taking longer than usual, but they assumed it was due to resourcing constraints on OOPS' end. PANIC consented to OOPS providing FBI with a copy of the Docker image in question.

Analyze the provided Docker image and identify the actor's techniques.

Downloads:
- PANIC Nightly Build + Test Docker Image (image.tar)

## Solution
1. look at the manifest.json to find "maintainer" email (use "cat manifest.json | jq")
	
    a. jq is a nice thing to show json in pretty format (can pipe output to a new json)

2. tar -xf all the layer.tar files in each folder
	
    a. rg 'git clone' and look for the git clone url that is connected to a sus file "build_test.sh"

3. so most malicious files are binaries, so you are probably gonna be looking in "bin" directories
	
    a. after searching around the different directories, you find the 8e... folder because it has a lot of folders

	b. you check out bin from the main directory, but find nothing in there
	
    c. since you didn't find anything, you look into usr/bin
	
    	1. interesting, you find a lot of files
		
        2. since you know malicious files/payloads are usually pretty big, you do "ls -lh" to see the file size and notice
		that the "make" file is 8.4M so that's probs the malicious file -> path is usr/bin/make
