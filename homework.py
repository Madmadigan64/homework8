
#!/usr/bin/env python3
from scapy.all import DNS, DNSQR, IP, sr1, UDP
import sys
queryhost = sys.argv[1]

dnsRequest = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="queryhost"))
dnsresponse = sr1(dnsRequest)
print(dnsresponse[DNS].summary())
