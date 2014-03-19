#!/usr/bin/env python

import os
import sys
import nanomsg as nn

import time

def main():

  # sockets who will communicate among themselves
  s2 = nn.Socket(domain=nn.AF_SP, protocol=nn.PAIR)

  # connect to the above declared endpoint
  s2.connect("tcp://127.0.0.1:50000")

  # global counters on msgs prrocessed by both peers
  s2_msg_processed = 0

  start_time = time.time()

  try:

    while (1):
    
      print s2.recv()
      s2_msg_processed = s2_msg_processed + 1
      s2.send("Hi! from s2")

  except KeyboardInterrupt, e:
    end_time = time.time()
    print 'total messages processed by s2: %s' % s2_msg_processed
    print 'total messages processed by s2 per sec: %s' % str(int(s2_msg_processed / (end_time - start_time)))

if __name__ == '__main__':
  main()
