# python3.5
# Testing

import sys

filename = str(sys.argv[1])
sys.stdout=open(filename,"w")

count = 0
while count < 42:
	print("All work and no play makes...")
	count = count + 1
	
sys.stdout.close()
