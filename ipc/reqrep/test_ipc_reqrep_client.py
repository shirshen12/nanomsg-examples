#!/usr/bin/env python

import os
import sys
import time
import nanomsg as nn

def main():
  
  # declare a socket
  client_sock = nn.Socket(domain=nn.AF_SP, protocol=nn.REQ)

  # bind the above socket to an endpoint
  client_sock.connect("ipc://test-ipc-sock")

  # status message for declaring server comming up online
  print "An REQ client is connecting to REP server at ipc://test-ipc-sock"

  # global counters for messaging stats
  client_sock_msg_processed = 0

  try:

    start_time = time.time()

    while (1):

      # send a message to the server
      msg = 'Hi! from a client with os level PID: %s' % os.getpid()
      msg = client_sock.send(msg)

      # process the response from the server
      print client_sock.recv()

      client_sock_msg_processed = client_sock_msg_processed + 1

  except KeyboardInterrupt, e:
    end_time = time.time()
    delta = end_time - start_time

    print 'total messages processed by client_sock: %s' % client_sock_msg_processed
    print 'messages processed by client_sock per second: %s' % str(int(client_sock_msg_processed / delta))

if __name__ == '__main__':
  main()
