#!/usr/bin/env python

import os
import sys
import time
import nanomsg as nn

msg_processed = 0

def main():

  global msg_processed
  
  # declare a socket
  respondent_sock = nn.Socket(domain=nn.AF_SP, protocol=nn.RESPONDENT)

  # bind the sock
  respondent_sock.connect("tcp://127.0.0.1:50000")

  try:

    start_time = time.time()

    while (1):

      print respondent_sock.recv()

      # read the message which the client has sent
      respondent_sock.send("I provide payments: %s" % str(os.getpid()))
      msg_processed = msg_processed + 1


  except KeyboardInterrupt, e:

    end_time = time.time()

    print 'total messages processed: %s' % str(msg_processed)
    print 'messages processed per second: %s' % str(int(msg_processed/(end_time - start_time)))
    print 'messages processed per minute: %s' % str(int(msg_processed/(end_time - start_time)) * 60) 

if __name__ == '__main__':
  main()
