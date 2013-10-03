#!/usr/bin/python

classval_ids = { 1:'Politics', 2:'Sports' }

decisionfile = 'output'	# each line should conain a class-value (one of the keys in the classval_ids dict)
outputfile = 'results.txt'
tweetidsfile = 'test.txt'		# the first field in this file should contain the tweet-ids


tweetids = []
fin = open(tweetidsfile, 'r')
for line in fin:
	v = line.find(' ')
	tid = line[:v]
	tweetids.append(tid)
# end for
fin.close()


fin = open(decisionfile, 'r')
fout = open(outputfile, 'w')
count = 0
for line in fin:
	v = line.strip()
	v = int(v)
	classval = classval_ids[v]
	fout.write( str(tweetids[count]) + ' ' + str(classval) + '\n' )
	count += 1
# end for

fin.close()
fout.close()


