# Task 4
A number of OOPS employees fell victim to the same attack, and we need to figure out what's been compromised! Examine the malware more closely to understand what it's doing. Then, use these artifacts to determine which account on the OOPS network has been compromised.

Downloads:
- OOPS forensic artifacts (artifacts.zip)

## Solution
1. look at the fullpowershell.txt from last and identify what it is doing
	
    a. you see that it is going into specific registries (PuTTY and WinSCP)
	
    b. identify what is being taken for each registry

    -  PuTTY -> Source, Session, Hostname, Keyfile
		
    -  WinSCP -> Source, Session, Hostname, Username, Password

2. So now you know what is being taken and you know that the prettyXML.xml contains the registries -> next need to figure out how to find the right data
	
    a. looking at the differences amongst the artifacts (only the ppks bc those are PuTTY private keys), you notice that some do NOT use any encryption -> this means that it is easier for a hacker to exploit (dkr_prd93, dkr_prd54, dkr_tst67, dkr_tst70, dkr_tst76)

3. looking into the XML file, we search for the dkr that are not encrypted, you find a node within with dkr_prd93 yayyyy (builder07@dkr_prd93)
	
    a. machine name = dkr_prd93

	b. builder07
