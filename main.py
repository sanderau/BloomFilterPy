import math
import time
import sys
import hashlib
from bitarray import bitarray

# ============ BLOOM FILTER CLASS ============== #

class BloomFilter:
	
	def __init__(self, passwordSize, numberOfHashes):
		self.fp = .01 # the acceptable false postivie rate. You could get more precise, but then the program would begin taking up MB's of memory :(
		self.hashes = numberOfHashes # the number of hashes this bloom filter will use
		self.size = passwordSize # the number of passwords stored
		self.m_bits =  int(math.ceil((self.size*math.log(.01)) / math.log(1 / (2**math.log(2))))) # this value was calculate based on the input file. It is the number of optimal bits inside the array
		self.bit_array = bitarray(self.m_bits) # this is the bit array. The number of bits needed was optimized using a formula linked in the readme
		self.bit_array.setall(0) #set all bits to 0 or false

	def addItem(self, item):
		hashed = hashlib.sha256(item) #hash it the first time
		for i in range(0, self.hashes):
			num = int(hashed.hexdigest(), hashed.digest_size)
			index = int(num % self.m_bits) 
			self.bit_array[index] = True #calculate its index and set the bit to true
			hashedTwo = hashlib.sha256()
			hashedTwo.update(hashed.digest())
			hashedTwo.hexdigest()
			hashed = hashedTwo #hash it again and set the original hash to the new hash
	
	def checkItem(self, item):
		hashed = hashlib.sha256(item)
		for i in range(0, self.hashes):
			num = int(hashed.hexdigest(), hashed.digest_size)
			index = int(num % self.m_bits) 

			if(self.bit_array[index] == True): #if the item is in the array return true!
				return True #the item is probably in the list

			hashedTwo = hashlib.sha256()
			hashedTwo.update(hashed.digest())
			hashedTwo.hexdigest()
			hashed = hashedTwo #hash it again and set the original hash to the new hash
	
		return False # the item is NOT in the list


# ========== HELPER FUNCTIONS ======== #

def calculate_hash(toHash, size, numOfHashes):
	if(numOfHashes == 3): #triple hash the input
		h1 = hashlib.sha1(toHash)
		num = int(h1.hexdigest(), h1.digest_size)
	
def getNumber(pFile):
	with open(pFile) as f:
		for i, l in enumerate(f):
			pass
	return i+1


# ========== MAIN =========== #
if(len(sys.argv) != 8 ):
	print("not enough command line arguments")
	exit(1)

dictionary = sys.argv[2]
inputFile = sys.argv[4]
outOne = sys.argv[6]
outTwo = sys.argv[7]

outFileOne = open(outOne, 'w')
outFileTwo = open(outTwo, 'w')

numberOfPasswords = getNumber(dictionary) # get the number of passwords to store.

three = BloomFilter(numberOfPasswords, 3)
five = BloomFilter(numberOfPasswords, 5)

with open(dictionary, 'r') as inFile: #populate both of the bloom filters
	for line in inFile:
		for word in line.split():
			three.addItem(word)
			five.addItem(word)

with open(inputFile, 'r') as inFile:
	for line in inFile:
		for word in line.split():
			threeBool = three.checkItem(word)
			fiveBool = five.checkItem(word)
			if(threeBool):
				outFileOne.write('maybe.\n')
			else:
				outFileOne.write('no.\n')
			if(fiveBool):
				outFileTwo.write('maybe.\n')
			else:
				outFileTwo.write('no.\n')
