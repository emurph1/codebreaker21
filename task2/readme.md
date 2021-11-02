# task 2
1. Using the ip from the previous task and under the subnet defined in the oops_subnet.txt, run a grep to look within the proxy.log (where the ip is the listening post)

    `grep 10.120.14.143 proxy.log`

    ```
    2021-03-16 08:34:49 40 10.210.95.77 200 TCP_MISS 12734 479 GET http xomtq.invalid analysis - - DIRECT **10.120.14.143** application/octet-stream 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' PROXIED none - 10.210.94.189 SG-HTTP-Service - none -
    ```

2. Create a Python script to parse through the JSON data to find the logons and log offs and see which LogonIds are associated with the time found from step 1
    ```
    0X339534
    0X339757
    0X33946D
    0X339870
    0X339989
    0X339A8A 
    ```

3. use a grep to in the json to find the specific LogonId with the IP from step 1

    `grep -iE "0X339534|0X339757|0X33946D|0X339870|0X339989|0X339A8A" narrowed.json | grep "10.210.95.77"`

    ```
    {"PayloadData1": "Target: OOPS.NET\\chambers.jennifer", "PayloadData2": "LogonType 3", "PayloadData3": "LogonId: 0X33946D", "UserName": "-\\-", "RemoteHost": "- (10.210.95.77)", "ExecutableInfo": "-", "MapDescription": "Successful logon", "ChunkNumber": 0, "Computer": "OOPS-DC.oops.net", "Payload": "{\"EventData\": {\"Data\": [{\"@Name\": \"SubjectUserSid\", \"#text\": \"S-1-0-0\"}, {\"@Name\": \"SubjectUserName\", \"#text\": \"-\"}, {\"@Name\": \"SubjectDomainName\", \"#text\": \"-\"}, {\"@Name\": \"SubjectLogonId\", \"#text\": \"0x0\"}, {\"@Name\": \"TargetUserSid\", \"#text\": \"S-1-5-21-3521346-774097835-5683131894-1126\"}, {\"@Name\": \"TargetUserName\", \"#text\": \"chambers.jennifer\"}, {\"@Name\": \"TargetDomainName\", \"#text\": \"OOPS.NET\"}, {\"@Name\": \"TargetLogonId\", \"#text\": \"0X33946D\"}, {\"@Name\": \"LogonType\", \"#text\": \"3\"}, {\"@Name\": \"LogonProcessName\", \"#text\": \"Kerberos\"}, {\"@Name\": \"AuthenticationPackageName\", \"#text\": \"Kerberos\"}, {\"@Name\": \"WorkstationName\", \"#text\": \"-\"}, {\"@Name\": \"LogonGuid\", \"#text\": \"c5dfa92b-9ee6-4b7b-9029-207959f780e7\"}, {\"@Name\": \"TransmittedServices\", \"#text\": \"-\"}, {\"@Name\": \"LmPackageName\", \"#text\": \"-\"}, {\"@Name\": \"KeyLength\", \"#text\": \"0\"}, {\"@Name\": \"ProcessId\", \"#text\": \"0x0\"}, {\"@Name\": \"ProcessName\", \"#text\": \"-\"}, {\"@Name\": \"IpAddress\", \"#text\": \"10.210.95.77\"}, {\"@Name\": \"IpPort\", \"#text\": \"39845\"}, {\"@Name\": \"ImpersonationLevel\", \"#text\": \"%%1833\"}, {\"@Name\": \"RestrictedAdminMode\", \"#text\": \"-\"}, {\"@Name\": \"TargetOutboundUserName\", \"#text\": \"-\"}, {\"@Name\": \"TargetOutboundDomainName\", \"#text\": \"-\"}, {\"@Name\": \"VirtualAccount\", \"#text\": \"%%1843\"}, {\"@Name\": \"TargetLinkedLogonId\", \"#text\": \"0x0\"}, {\"@Name\": \"ElevatedToken\", \"#text\": \"%%1842\"}]}}", "Channel": "Security", "Provider": "Microsoft-Windows-Security-Auditing", "EventId": 4624, "EventRecordId": "5378", "ProcessId": 693, "ThreadId": 5958, "Level": "LogAlways", "Keywords": "Audit success", "SourceFile": "C:\\Windows\\system32\\winevt\\Logs\\Security.evtx", "ExtraDataOffset": 0, "HiddenRecord": false, "TimeCreated": "2021-03-16T12:09:22.6771601+00:00", "RecordNumber": "5378"}

    ```

5. **LogonId: 0X33946D**