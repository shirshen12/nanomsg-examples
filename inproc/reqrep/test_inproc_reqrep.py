#!/usr/bin/env python

import os
import sys
import time
import random
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

client_list = ["s2", "s3"]
while(1):

  # choose the client to communicate
  client = random.choice(client_list)

  if client == 's2':

    # start communicating
    s2.send("hello from socket, s2")
    # field the request
    print s1.recv()
    # send a reponse back
    resp = 'hello from socket, s1'
    s1.send(resp)
    print s2.recv()

  elif client == 's3':

    # start communicating
    s3.send("hello from socket, s3")
    # field the request
    print s1.recv()
    # send a reponse back
    resp = 'hello from socket, s1'
    s1.send(resp)
    print s3.recv()

  time.sleep(1)  






