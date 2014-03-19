#!/usr/bin/env python

import os
import sys
import nanomsg as nn

def main():
  
  # declare a socket
  client_sock = nn.Socket(domain=nn.AF_SP, protocol=nn.REQ)

  # bind the above socket to an endpoint
  client_sock.connect("ipc://test-ipc-sock")

  # status message for declaring server comming up online
  print "An REQ client is connecting to REP server at ipc://test-ipc-sock"

  while (1):

    # send a message to the server
    msg = 'Hi! from a client with os level PID: %s' % os.getpid()
    msg = client_sock.send(msg)

    # process the response from the server
    print client_sock.recv()


if __name__ == '__main__':
  main()
