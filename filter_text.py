#!/usr/bin/python
import re
import nltk

'''
this script reads a file containing text of one tweet per line
Filters out stop-words, stems words, etc, writes words to outfile (again, one tweet per line)
'''

datafile1 = 'training.tweetext.raw'
outfile1 = 'training.tweetext'

#datafile2 = 'validation.tweetext.raw'
#outfile2 = 'validation.tweetext'

datafile2 = 'test.tweetext.raw'
outfile2 = 'test.tweetext'


#Stopword Creation
stopwordfile = 'stopwords_big.txt'

stoplist = []

def createStopwordList(f):
	words = open(f, 'r').read().split(',')
	for w in words:
		w = w.lower()
		stoplist.append(w)
	# end for
# end createStopwordList()

stopword_small_file = 'stopwords_small.txt'

stoplist_small = []

def createStopwordSmallList(f):
	words = open(f, 'r').read().split(',')
	for w in words:
		w = w.lower()
		stoplist_small.append(w)
	# end for

# end createStopwordSmallList()


stopslangfile = 'stop_slang.txt'

stop_slang_list = []

def createStopSlangList(f):
	words = open(f, 'r').read().split()
	for w in words:
		w = w.lower()
		stop_slang_list.append(w)
	# end for
# end createStopSlangList()

stopemotfile = 'emoticon_simple.txt'

stop_emot_list = []

def createStopEmotList(f):
	words = open(f, 'r').read().split()
	for w in words:
		w = w.lower()
		stop_emot_list.append(w)
	# end for
# end createStopEmotList()


pronounfile = 'person_pronoun.txt'

pronounlist = []

def createPronounList(f):
	words = open(f, 'r').read().split()
	for w in words:
		w = w.lower()
		pronounlist.append(w)
	# end for
# end createPronounList()


_digits = re.compile('\d')
def contains_digits(d):
    return bool(_digits.search(d))	

def tag_words(x):
	#Tagging appropriately for feature extraction
	if (x != "PUNC") and (x != "LINE") and (x != "EMOT") and ( x != "USER") and ( x != "HASHTAG") and ( x != "RETWEET" ) and (x != "URL" ) and ( x != "PRONOUN" ) and (x != "SLANG") and (x != "NUM") and (x != "DATETIME") and (x != "QUOTE") and ( x != "ALNUM"):
		tag_of_word = nltk.pos_tag(nltk.word_tokenize(x))[0][1]
	
		if re.match(r'W[A-Z]+', tag_of_word) != None:
			text = re.sub(r'W[A-Z]+',' WHWORD',tag_of_word)
		elif re.match(r'N[A-Z]*P', tag_of_word) != None:
			text = re.sub(r'N[A-Z]*P',x,tag_of_word)
			#print text
		elif re.match(r'N[A-Z]+', tag_of_word) != None:
			text = re.sub(r'N[A-Z]+',x,tag_of_word)
		elif re.match(r'I[A-Z]+', tag_of_word) != None:
			text = re.sub(r'I[A-Z]+',' ',tag_of_word)
		elif re.match(r'J[A-Z]+', tag_of_word) != None:
			text = re.sub(r'J[A-Z]+',' ',tag_of_word)
		elif re.match(r'MD', tag_of_word) != None:
			text = re.sub(r'MD',' MODAL',tag_of_word)
		elif re.match(r'V[A-Z]+', tag_of_word) != None:
			text = re.sub(r'V[A-Z]+',' VERB',tag_of_word)
		else:
			text = tag_of_word

		return text
	else:
		return x

def processText(text):
	
	#Removing Punctuation Marks
	original_text = text
	text = text.strip()
	text = text.lower()			#Casefolding is done
	text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' URL ', text)
	text = re.sub('((19|20)\\d\\d)|(\\d{1,2}\\s*(th)+)|(\\d+[/]\\d+)|([3]\\s*(rd)+)|([2]\\s*(nd)+)|(\\d{1,2}[-/ ]{1}\\d{1,2}[-/]{1}\\d{1,4})', ' DATETIME ', text)
	text = re.sub('([1-2]?[0-9](:)+[0-5][0-9]\\s*(am|pm)?)|([1-2]?[0-9][0-5][0-9]\\s*(am|pm)+)|((([1][012])|([1-9]))\\s*(am|pm))', ' DATETIME ', text)
	text = re.sub('\s+', ' ', text)
	words = text.split()
	
	words = map( lambda x: ' EMOT ' if x in stop_emot_list else x, words )

	#words = filter( lambda x: not 'http' in x, words )
	#words = filter( lambda x: not 'https' in x, words )
        for i in range(len(words)):
                words[i] = words[i].replace('-',' ').replace(':',' PUNC ').replace(',',' PUNC ').replace(';',' LINE ').replace('%',' ').replace('[',' ').replace(']',' ')
                words[i] = words[i].replace('.',' ').replace('?',' ').replace('!',' EMOT ').replace('*', ' ').replace('$', ' ').replace('_',' ').replace('=',' ')
                words[i] = words[i].replace('"',' QUOTE ').replace('(', ' ').replace(')', ' ').replace("&", ' ').replace('`',' ').replace('\'',' ')
                words[i] = words[i].replace('+','').replace('\\',' ').replace('/',' ').replace('|',' LINE ').replace('{',' ').replace('}',' ').replace('~',' ')
                words[i] = words[i].replace('#', ' HASHTAG ').replace('rt', ' RETWEET ').replace('@', ' USER ') #considering hashtag any word
		words[i] = words[i].replace("\\t",' ').replace("\\u",' ').replace("\\r",' LINE ').replace("\\x",' ').replace("\\n",' LINE ').replace("\\u", ' ')
                words[i] = words[i].strip()
        # end for

	temp = ' '.join(words)
	temp = re.sub('\s+', ' ', temp)
        words = temp.split()

 
	#words = filter( lambda x: not '@' in x, words ) #removing names does not help in accuracy
		
	#words = map( lambda x: ' PRONOUN ' if x in pronounlist else x, words )
	words = filter( lambda x: not x in pronounlist, words )
	#words = filter( lambda x: not x in stoplist_small, words )
	words = filter( lambda x: not x in stoplist, words )

	temp = ' '.join(words)
	temp = re.sub('\s+', ' ', temp)
        words = temp.split()
	words = map( tag_words , words )
	temp = ' '.join(words)
	#temp = re.sub('(?=[mdclxvi])m*(c[md]|d?c*)(x[cl]|l?x*)(i[xv]|v?i*)', ' ROMAN ', temp )
	temp = re.sub('\s+', ' ', temp)
        words = temp.split()

	#words = map( lambda x: not x in stoplist, words )
	words = map( lambda x: ' SLANG ' if x in stop_slang_list else x, words )
        words = map( lambda x: ' NUM '  if x.isdigit() else x, words ) 
        #words = filter( lambda x: not x.isdigit() , words ) 
        words = map( lambda x: ' ALNUM ' if contains_digits(x) else x, words ) 
	
	temp = ' '.join(words)
	temp = re.sub('\s+', ' ', temp)
	temp = re.sub('-NONE-', '', temp)
        words = temp.split()

	if not words:
		final = original_text
		print 'Tweet becomes blank after MORE filtering:', original_text
	else:
		final = ' '.join(words)
	# end if

	return final
# end processText()


#### main process ####

createStopwordList(stopwordfile)
createStopwordSmallList(stopword_small_file)
createStopSlangList(stopslangfile)
createStopEmotList(stopemotfile)
createPronounList(pronounfile)

#print stop_emot_list

fin = open(datafile1, 'r')
fout = open(outfile1, 'w')

for line in fin:
	line = line.strip()
	p = processText(line)
	#if p != "":
	fout.write(p + '\n')
# end for

fin.close()
fout.close()

fin = open(datafile2, 'r')
fout = open(outfile2, 'w')

for line in fin:
	line = line.strip()
	p = processText(line)
	#if p != "":
	fout.write(p + '\n')
# end for

fin.close()
fout.close()
