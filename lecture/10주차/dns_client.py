import socket
import struct
import sys

class DnsClient:
    def __init__(self, domainName):
        self.domainName = domainName
        # DNS Query Header
        self.TransactionId = 1
        self.Flag = 0x0100
        self.Questions = 1
        self.AnswerRRs = 0
        self.AuthorityRRs = 0
        self.AdditionalRRs = 0

    def response(self, packet):  # Processing DNS response
        dnsHeader = packet[:12]
        dnsData = packet[12:].split(b'\x00', 1)
        ansRR = packet[12+len(dnsData[0])+5:12+len(dnsData[0])+21]
        rr_unpack = struct.unpack('!2sHHIH4s', ansRR)
        ip_addr = socket.inet_ntoa(rr_unpack[5])
        print(self.domainName, ip_addr)

    def query(self):  # Create DNS query
        # DNS header packing
        query = struct.pack('!HH', self.TransactionId, self.Flag)
        query += struct.pack('!HH', self.Questions, self.AnswerRRs)
        query += struct.pack('!HH', self.AuthorityRRs, self.AdditionalRRs)

        # Packing domain name
        part = self.domainName.split('.')
        for i in range(len(part)):
            query = query + struct.pack('!B', len(part[i]))
            query = query + part[i].encode()
        query = query + b'\x00'

        # Type and class fields
        query_type = 1  # Type: A
        query_class = 1  # Class: IN
        query = query + struct.pack('!HH', query_type, query_class)

        # Sending DNS query
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = ('220.69.193.130', 53)  # 순천향대학교 DNS 서버 주소
        sock.sendto(query, addr)
        
        # Receiving DNS response
        packet, address = sock.recvfrom(65535)
        self.response(packet)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        client = DnsClient(sys.argv[1])
        client.query()
    else:
        print("Usage: python dns_client.py <domain_name>")
