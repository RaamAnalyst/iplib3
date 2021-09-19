.. iplib3 documentation master file, created by
   sphinx-quickstart on Sun Sep 19 18:59:04 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Usage
=====

The module mainly provides a single class, `iplib3.IPAddress`, which can be used to initialise IP address objects of any supported type. However, it is possible to use the provided `iplib3.IPv4` and `iplib3.IPv6` classes directly if needed.

The primary class has the advantage that it also supports raw numbers; you can initialise it with any positive integer in addition to stringified addresses, and since you can directly convert between the two sub-classes at any time you can use all functionality with just `iplib3.IPAddress`. Since `iplib3.IPv4` and `iplib3.IPv6` are subclasses of `iplib3.IPAddress`, you can use `isinstance` to recognise any of the three types.

Some basic usage examples:

.. code-block::python

from iplib3 import IPAddress, IPv6

address = IPAddress('222.173.190.239')

print(address) 

*# 222.173.190.239*

print(address.port) 

*# None, because we never specified one*

address.port = 80

print(address) 

*# 222.173.190.239:80*

print(repr(address)) 

*# iplib3.IPv4('222.173.190.239:80')*

ipv6_address = address.as_ipv6

print(ipv6_address) 

*# [0:0:0:0:0:0:DEAD:BEEF]:80*

ipv6_address.port = None

print(ipv6_address) 

*# 0:0:0:0:0:0:DEAD:BEEF*

print(repr(ipv6_address)) 

*# iplib3.IPv6('0:0:0:0:0:0:DEAD:BEEF')*

foo = IPv6('[::1337:1337:1337:1337]:25565')

bar = IPv6('::1337:1337:1337:1337', 25565)

baz = IPv6('::1337:1337:1337:1337', port_num=25565)

print(f"Addresses are {'equal' if foo == bar == baz else 'not equal'}")

print(baz) 

*# [::1337:1337:1337:1337]:25565*

print(baz.as_ipv4.as_ipv6 == baz)

*# If the string contains a port number and you also provide a port separately, then the separately provided port takes precedence*

spam = IPv6('[::1337:1337:1337:1337]:80', port_num=25565)

print(spam) 

*# [::1337:1337:1337:1337]:25565*

print(address.hex) 

*# 0xDEADBEEF*

print(address.num)
 
*# 3735928559*



