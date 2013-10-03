#!/usr/bin/python
'''
This script parses input file written in the format
tweetid  class  tweet-text
The tweet-text can be enclosed within "" or within ''.

Writes two output files:
in one file, the tweet-texts are written, one per line
in another file, the classes are written in corresponding lines

'''

import sys

if len(sys.argv) != 4:
        print "Usage: <Program_name> <IN:input_file> <OUT: Raw tweet Out File> <IN: Training Flag(1)>"
        exit(0)

inputfile = sys.argv[1] # training.txt/validation.txt/test.txt
outfile_tweets = sys.argv[2] #training.txt.raw/validation.txt.raw/test.txt.raw
flag = int(sys.argv[3])

if flag == 1: #for training set
	outfile_classes = 'training.classval'		# put for training.txt
else:
	outfile_classes = None		# put as None if there are no class values


fin = open(inputfile, 'r')
fout_tweets = open(outfile_tweets, 'w')
if outfile_classes:	fout_classes = open(outfile_classes, 'w')

for line in fin:
	line = line.strip()
	delim = line[-1]	# the tweet-text is enclosed within this character(may be ' or " )

	#left_occurrence = line.rfind(delim, 0, -1)
	left_occurrence = line.find(delim) #Get the first left occurence of delimeter character

	text = line[left_occurrence + 1: -1]	# the tweet text
	#print text
	fout_tweets.write(text + '\n')

	if outfile_classes:
		v = line[:left_occurrence].split()
		classval = v[1]
		fout_classes.write(classval + '\n')
	# end if
# end for each line in fin

fin.close()
fout_tweets.close()
if outfile_classes:	fout_classes.close()

