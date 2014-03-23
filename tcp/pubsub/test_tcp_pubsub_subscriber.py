#!/usr/bin/env python

import os
import sys
import time
import nanomsg as nn

def main():
  
  # declare a socket
  subscriber_sock = nn.Socket(domain=nn.AF_SP, protocol=nn.SUB)
  subscriber_sock.set_string_option(level=nn.SUB, option=nn.SUB_SUBSCRIBE, value="")

  # bind the above socket to an endpoint
  subscriber_sock.connect("tcp://127.0.0.1:50000")

  # global counters for messaging stats
  subscriber_sock_msg_processed = 0

  try:

    start_time = time.time()

    while (1):

      print subscriber_sock.recv()

      subscriber_sock_msg_processed = subscriber_sock_msg_processed + 1

  except KeyboardInterrupt, e:
    end_time = time.time()
    delta = end_time - start_time

    print 'total messages processed by subscriber_sock: %s' % subscriber_sock_msg_processed
    print 'messages processed by subscriber_sock per second: %s' % str(int(subscriber_sock_msg_processed / delta))

if __name__ == '__main__':
  main()
