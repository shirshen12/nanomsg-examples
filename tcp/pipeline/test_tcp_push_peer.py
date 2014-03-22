#!/usr/bin/env python

import os
import sys
import time
import nanomsg as nn

msg_processed = 0

def main():

  global msg_processed
  
  # declare a socket
  push_sock = nn.Socket(domain=nn.AF_SP, protocol=nn.PUSH)

  # bind the above socket to an endpoint
  push_sock.bind("tcp://127.0.0.1:50000")

  try:

    start_time = time.time()

    while (1):

      # send a message
      push_sock.send("Hi! from push_sock at: tcp://127.0.0.1:50000")

      msg_processed = msg_processed + 1

  except KeyboardInterrupt, e:

    end_time = time.time()

    print 'total messages processed: %s' % str(msg_processed)
    print 'messages processed per second: %s' % str(int(msg_processed/(end_time - start_time)))
    print 'messages processed per minute: %s' % str(int(msg_processed/(end_time - start_time)) * 60) 

if __name__ == '__main__':
  main()
