#!/usr/bin/python

import sys, getopt, subprocess, os

def main(argv):
   reffile = ''
   pair1 = ''
   pair2 = ''
   output = ''
   try:
      opts, args = getopt.getopt(sys.argv[1:],"hr:L:R:", "['reference=','leftfq=','rightfq=']")
      if len(opts) < 3:
          print "Error: Missing some options"
          print 'bwa.py -r <reference_file> -L <paired_end_left> -R <paired_end_right>'
          sys.exit(2)
   except getopt.GetoptError:
      print 'Error: Unrecognized parameter'
      print 'bwa.py -r <reference_file> -L <paired_end_left> -R <paired_end_right>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'bwa.py -r <reference_file> -L <paired_end_left> -R <paired_end_right>'
         sys.exit()
      elif opt == '-r':
         reffile = arg
      elif opt == '-L':
         pair2 = arg
      elif opt == '-R':
         pair1 = arg
   output = os.path.basename(pair1)+'.sam'
   bwa_cl = ['bwa', 'mem', reffile, pair1, pair2]
   if len(bwa_cl) != 5:
      print "Error: Missing parameters"
      print 'bwa.py -r <reference_file> -L <paired_end_left> -R <paired_end_right>'
      sys.exit(2)
   print 'The command line run was "$ %s"' % (' ').join(bwa_cl)
   with open(output, 'w') as f_output:
      proc = subprocess.call(bwa_cl, stdout=f_output)
      print proc

if __name__ == "__main__":
   main(sys.argv[1:])
