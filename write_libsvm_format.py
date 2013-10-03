'''
Takes two input files
- one containing text documents (one per line)
- the other containing class-values (one per line)
class-value of document i (in the i-th line in first file) is in i-th line in second file

writes outfile in libsvm format
<label> <index1>:<value1> <index2>:<value2> ...
...
...

To generate the index values, a dictionary of all distinct words is required as input;
this must be specified as dictfile.

Also, the different possible class-values must be specified in the classval_ids dict, along with what numeric id to write for each class-value.
'''


dictfile = 'dictionary.tweetext'
distinct_words = {}

classval_ids = { 'Politics':1, 'Sports':2 }
defaultclassval = 0


def read_dictionary( dictfile ):
	'''	
	read the dictionary file (distinct words and their indices)
	'''

	fin = open(dictfile, 'r')
	for line in fin:
		v = line.strip().split()
		word = v[0]
		wordid = int(v[1])
		distinct_words[word] = wordid
	# end for
	fin.close()
# end read_dictionary()


def process_file( infile_text, infile_classvals, outfile ):
	'''	
	read the text file and class file, write outfile in libsvm format
	'''

	print 'Processing text file', infile_text, 'and class value file', infile_classvals
	fin_text = open(infile_text, 'r')
	if infile_classvals:	fin_classval = open(infile_classvals, 'r')
	fout = open(outfile, 'w')


	for line in fin_text:		# note that each line is a document
		words = line.strip().split()

		# build two dicts for this document, 
		# one containing the frequency of the words, the other containing the ids
		wordfreqs = {}
		for w in words:
			try:	wordfreqs[w] += 1
			except:	wordfreqs[w] = 1
		# end for

		wordids = {}
		for w in wordfreqs:	
			wordids[w] = distinct_words[w]		# get the id of the word from the global dictionary
		# end for

		# libsvm requires that the attribute ids be written in increasing order (here, attributes are the words)
		temp = wordids.items()
		temp.sort( lambda x, y: x[1] - y[1] )

		# build the line to write to outfile
		if infile_classvals:
			c = fin_classval.readline().strip()
			classval = classval_ids[c]
			outstr = str(classval)
		else:
			outstr = str(defaultclassval)
		# end if

		for w, wid in temp:
			wf = str(wordfreqs[w])
			wid = str(wid)
			outstr += ' ' + wid + ':' + wf
		# end if

		fout.write(outstr + '\n')
	#end for each line in input file (i.e., for each document)


	fin_text.close()
	if infile_classvals:	fin_classval.close()
	fout.close()
	print 'Output written in libsvm format to file', outfile

# end process_file()


read_dictionary( dictfile )


infile_text = 'training.tweetext'
infile_classvals = 'training.classval'		# put as None if class-values are not known
outfile = 'training.tweetext.libsvm'

process_file( infile_text, infile_classvals, outfile )

'''
infile_text = 'validation.tweetext'
infile_classvals = None		# put as None if class-values are not known
outfile = 'validation.tweetext.libsvm'
'''

infile_text = 'test.tweetext'
infile_classvals = None		# put as None if class-values are not known
outfile = 'tests.tweetext.libsvm'

process_file( infile_text, infile_classvals, outfile )

