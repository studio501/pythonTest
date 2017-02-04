# -*-coding:UTF-8-*-
import sys,getopt,time,calendar,os

def main(argv):
	inputfile = ""
	outputfile = ""
	try:
		opts,args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print "test.py -i <inputfile> -o <outputfile>"
		sys.exit(2)
	for opt,arg in opts:
		if opt == "-h":
			print "test.py -i <inputfile> -o <outputfile>"
			sys.exit()
		elif opt in ("-i","--ifile"):
			inputfile = arg
		elif opt in ("-o","--ofile"):
			outputfile = arg
	print "inputfile:",inputfile
	print "outputfile:",outputfile

def func():
	for num in range(10,20):
		for i in range(2,num):
			if num % i == 0:
				j = num/i
				print "%d is %d*%d" % (num,i,j)
				break
		else:
			print num,"is a prime number "

def timetest():
	print "now time is:",time.time()
	print "local time :",time.localtime(time.time())
	print "format local time :",time.asctime(time.localtime(time.time()))
	print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
	print calendar.month(2016,12)

def filetest():
	print os.getcwd()
	print "dir is : %s" %os.listdir(os.getcwd())
	# os.removedirs("./tp")
	# os.mkdir("tp")
	# os.chdir("./tp")
	# os.mkdir("inner")
	# os.remove("test1.txt")
	# os.rename("test.txt","test1.txt")
	# fo = open("test.txt","r+")
	# str = fo.read(10)
	# print "s1==>",str

	# position = fo.tell()
	# print "cur pos is ",position

	# position = fo.seek(0,1)
	# str = fo.read(10)
	# print "read again ",str
	# fo.close()

	# fo = open("data.json")
	# print "file name : ",fo.name
	# print "is closed : ",fo.closed
	# print "access mode: ",fo.mode
	# print "force space at end of line : ",fo.softspace
	# print fo.read()
	# fo.close()

	

	# print "is closed : ",fo.closed

	# fo = open("test.txt","a+")
	# fo.write("good day\ngood night\n")
	# fo.close()



	# str = raw_input("please input :")
	# print "what's your input is ",str

	# str = input("input agian: ")
	# print "result of your input is ",str


filetest()

# timetest()
# __name__ = "__timetest__"
# if __name__ == "__main__":
# 	main(sys.argv[1:])
# elif __name__ == "__func__":
# 	func()
# elif __name__ == "__timetest__":
# 	timetest()



