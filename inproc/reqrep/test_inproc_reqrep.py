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

# global counters messages processed by s1, s2 and s3
s1_msg_processed = 0
s2_msg_processed = 0
s3_msg_processed = 0

try:

  start_time = time.time()

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

      s1_msg_processed = s1_msg_processed + 1

      print s2.recv()

      s2_msg_processed = s2_msg_processed + 1

    elif client == 's3':

      # start communicating
      s3.send("hello from socket, s3")

      # field the request
      print s1.recv()

      # send a reponse back
      resp = 'hello from socket, s1'
      s1.send(resp)

      s1_msg_processed = s1_msg_processed + 1

      print s3.recv()

      s3_msg_processed = s3_msg_processed + 1

except KeyboardInterrupt, e:
  end_time = time.time()

  delta = end_time - start_time

  print 'total messages processed by s1: %s' % s1_msg_processed
  print 'total messages processed by s2: %s' % s2_msg_processed
  print 'total messages processed by s3: %s' % s3_msg_processed

  print 'messages processed by s1 per second: %s' % str(int(s1_msg_processed / delta))
  print 'messages processed by s2 per second: %s' % str(int(s2_msg_processed / delta))
  print 'messages processed by s3 per second: %s' % str(int(s3_msg_processed / delta))

