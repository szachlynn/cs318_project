import struct

def methodCall():
	pass

def main():
	f = open('/Accounts/stephanc/cs318/dti.trk', mode='rb')
	binContent = f.read()
	
	idString=();
	for i in range(6):
		idString=idString + struct.unpack("c", binContent[i:i+1])
	#methodCall()
	print ''.join(idString)

	
	

if __name__ == '__main__':
	main()