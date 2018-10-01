import sys
import os

if len(sys.argv[:]) < 2:
    exit("Supply an argument!")

print("Goal:\nArbitrary Command Execution.")
command='echo '+str(sys.argv[1])
os.system(str(command))
