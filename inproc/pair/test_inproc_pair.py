#!/usr/bin/env python

import os
import sys
import time
import pdb

import nanomsg as nn

# deploy 2 sockets for intra process communication
s1 = nn.Socket(domain=nn.AF_SP, protocol=nn.PAIR)
s2 = nn.Socket(domain=nn.AF_SP, protocol=nn.PAIR)

# bind the two sockets to respective endpoints
s1.bind("inproc://test-1")

# connect the socket
s2.connect("inproc://test-1")

# start communicating
while (1):

  s1.send("hello from socket, s1")
  s2.send("hello from socket, s2")

  print s1.recv()
  print s2.recv()

  time.sleep(1)


