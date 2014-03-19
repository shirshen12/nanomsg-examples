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

# counters for message processing
s1_msg_processed = 0
s2_msg_processed = 0

try:

  start_time = time.time()

  # start communicating
  while (1):

    s1.send("hello from socket, s1")
    s2.send("hello from socket, s2")

    print s1.recv()
    print s2.recv()

    s1_msg_processed = s1_msg_processed + 1
    s2_msg_processed = s2_msg_processed + 1

except KeyboardInterrupt, e:

  end_time = time.time()
  
  print 'total message processed by s1: %s' % str(s1_msg_processed) 
  print 'total message processed by s2: %s' % str(s2_msg_processed) 

  print 'message processed by s1 per second: %s' % str(int(s1_msg_processed / (end_time - start_time)))
  print 'message processed by s2 per second: %s' % str(int(s2_msg_processed / (end_time - start_time)))

