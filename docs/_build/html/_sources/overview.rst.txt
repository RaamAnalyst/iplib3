.. iplib3 documentation master file, created by
   sphinx-quickstart on Sun Sep 19 18:59:04 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Overview
========

**iplib3** is a `pathlib.Path`-equivalent for IP addresses. 

This module was heavily inspired by the built-in `pathlib` module to provide a similar, flexible interface for IP addresses. `iplib3` can effortlessly convert between IPv4, IPv6, raw numbers and hex values and it can also verify IP address syntax. It can recognise optional port numbers and store them separately from the main address. The `iplib.IPAddress` class works like `pathlib.Path` in that it accepts both IPv4 and IPv6 addresses, returning an object representing whichever format was used. The module also uses some unit tests, and these will be added more over time as functionality grows and becomes more set in stone.

The module is currently lacking in long-term vision as I used it as a practice project, but there are some plans to further flesh it out. It could incorporate URL support in the future and may be extended with `requests` integration.

This project is not affiliated with `iplib`, the naming similarity is merely a coincidence.

