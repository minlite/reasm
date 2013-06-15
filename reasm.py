#!/usr/bin/python

__author__ = 'miro'
import sys
import getopt
import re


def main():
    mode = 0
    src = None
    target = None
    n = 3
    try:
        myopts, args = getopt.getopt(sys.argv[1:],"i:o:n:")
    except getopt.GetoptError as e:
        print (str(e))
        print("Usage: %s -i Input [ -o Output (default is the source file) ] [ -n Number of spaces to skip (default is 3) ]" % sys.argv[0])
        sys.exit(2)
    for o, a in myopts:
        if o == '-i':
            src=open(a, "r")
            target=open(a, "r+")
        elif o == '-o':
            target=open(a, "w")
        elif o == '-n':
            n=a
    if src is None:
        print "No Input Given... Hint: Use the -i option to specify your input."
        print("Usage: %s -i Input [ -o Output (default is the source file) ] [ -n Number of spaces to skip (default is 3) ]" % sys.argv[0])
        sys.exit(2)
    # Iterate over the lines in the source file
    for readBuffer in src:
        # Hello there. Lets start doing this sh*t
        # 1. Remove any space in the beginning just to make sure someone won't play with us
        procString = ""
        for i in range(len(readBuffer)):
            if readBuffer[i] is not " ":
                for j in range(i, len(readBuffer)):
                    procString += readBuffer[j]
                break
        readBuffer = procString
        # 2. Remove any TAB in the beginning.. Who knows? There maybe some...
        procString = ""
        for i in range(len(readBuffer)):
            if readBuffer[i] is not "\t":
                for j in range(i, len(readBuffer)):
                    procString += readBuffer[j]
                break
        readBuffer = procString
        if readBuffer[0] is "=":
            # We should delete this whole line it's because it's invalid.
            continue
        if readBuffer[0] is "0":
            # 3. Try to remove the required number of spaces from the instructions...
            procString = ""
            p = 0
            i = 0
            while i < len(readBuffer)-1:
                if p == n:
                    procString += readBuffer[i]
                elif readBuffer[i] is " ":
                    p += 1
                    while readBuffer[i] is " ":
                        i += 1
                    i -= 1
                i += 1
            readBuffer = procString + "\n"
        # Thank GOD...We have hopefully finished processing this line. Write the line to the target and get rid of it...
        target.write(readBuffer)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()