import ipaddress
addr4 = ipaddress.ip_address('192.0.2.1')
print(addr4)

addr6 = ipaddress.ip_address('2001:A8::1')
print(addr6)

print(addr4.version)
print(addr6.version)

net = ipaddress.ip_network('114.71.220.0/24')

print(net)

net.with_netmask

net = ipaddress.ip_network('114.71.220.0/24')
for x in net.hosts():
    print(x)