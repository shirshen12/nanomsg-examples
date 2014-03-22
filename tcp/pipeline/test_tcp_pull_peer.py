#!/usr/bin/env python

import os
import sys
import time
import nanomsg as nn

def main():
  
  # declare a socket
  pull_sock = nn.Socket(domain=nn.AF_SP, protocol=nn.PULL)

  # bind the above socket to an endpoint
  pull_sock.connect("tcp://127.0.0.1:50000")

  # global counters for messaging stats
  pull_sock_msg_processed = 0

  try:

    start_time = time.time()

    while (1):

      # process the response from the server
      print pull_sock.recv()

      pull_sock_msg_processed = pull_sock_msg_processed + 1

  except KeyboardInterrupt, e:
    end_time = time.time()
    delta = end_time - start_time

    print 'total messages processed by pull_sock: %s' % pull_sock_msg_processed
    print 'messages processed by pull_sock per second: %s' % str(int(pull_sock_msg_processed / delta))

if __name__ == '__main__':
  main()
