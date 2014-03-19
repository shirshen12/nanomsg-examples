#!/usr/bin/env python

import os
import sys
import nanomsg as nn

import time

def main():

  # sockets who will communicate among themselves
  s1 = nn.Socket(domain=nn.AF_SP, protocol=nn.PAIR)

  # bind to an endpoint
  s1.bind("ipc://test-ipc-pair")

  # global counters on msgs prrocessed by both peers
  s1_msg_processed = 0

  start_time = time.time()

  try:

    while (1):
    
      s1.send("Hi! from s1")
      print s1.recv()
      s1_msg_processed = s1_msg_processed + 1

  except KeyboardInterrupt, e:
    end_time = time.time()
    print 'total messages processed by s1: %s' % s1_msg_processed
    print 'total messages processed by s1 per sec: %s' % str(int(s1_msg_processed / (end_time - start_time)))

if __name__ == '__main__':
  main()
