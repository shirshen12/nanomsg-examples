#!/usr/bin/env python

import os
import sys
import time
import pdb

import nanomsg as nn

# deploy 2 sockets for intra process communication
s1 = nn.Socket(domain=nn.AF_SP, protocol=nn.REP)
s2 = nn.Socket(domain=nn.AF_SP, protocol=nn.REQ)
s3 = nn.Socket(domain=nn.AF_SP, protocol=nn.REQ)

# bind the two sockets to respective endpoints
s1.bind("inproc://test-1")

# connect the socket
s2.connect("inproc://test-1")
s3.connect("inproc://test-1")

while(1):

  # start communicating
  s2.send("hello from socket, s2")
  s3.send("hello from socket, s3")

  # field the request
  req = s1.recv()
  print req  

  time.sleep(1)  






