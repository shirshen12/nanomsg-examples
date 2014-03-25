#!/usr/bin/env python

import os
import sys
import time
import nanomsg as nn

msg_processed = 0

def main():

  global msg_processed
  
  # declare a socket
  survey_sock = nn.Socket(domain=nn.AF_SP, protocol=nn.SURVEYOR)

  # bind the sock
  survey_sock.bind("tcp://127.0.0.1:50000")
  survey_sock.set_int_option(level=nn.SURVEYOR, option=nn.SURVEYOR_DEADLINE, value=1000)

  try:

    start_time = time.time()

    while (1):

      # send a response back
      survey_sock.send("What service do you provide: ")

      # read the message which the client has sent

      try:
        while (1):
          print survey_sock.recv()
      
          msg_processed = msg_processed + 1

      except Exception, e:
        continue

  except KeyboardInterrupt, e:

    end_time = time.time()

    print 'total messages processed: %s' % str(msg_processed)
    print 'messages processed per second: %s' % str(int(msg_processed/(end_time - start_time)))
    print 'messages processed per minute: %s' % str(int(msg_processed/(end_time - start_time)) * 60) 

if __name__ == '__main__':
  main()
