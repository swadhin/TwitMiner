
DEPENDENCY:
----------
1. libsvm 3.14 or higher
2. python 2.6 or higher
3. nltk latest version

------------------------
  INSTRUCTIONS TO RUN
------------------------

YOU can run the Script run.sh to get results.txt which you can upload.
                       ------
OR ( Can also do sequentially :)

1. Input files: training.txt and validation.txt/test.txt

2. Parse the input files using parse_input_files.py ( Give the parameters )
produces two files for each input file: one containing the tweet-texts, the other containing the class-values (if known)
Files produced: training.tweetext, training.classval and validation.tweetext/test.tweettext


3. Filter the tweet-texts using filter_text.py ( This file also help in Feature Extraction)
Takes one tweet-text file and produces a filtered tweet-text file
(must be done for each tweet-text file individually)


4. Prepare the dictionary containing all distinct terms: prepare_word_dict.py
works on all tweetext files to produce a dictionary file containing the distinct terms and ids for each
Files produced: dictionary.tweetext


5. Write the training and validation / testing files in libsvm format, using write_libsvm_format.py
reads a tweetext file and the corresponding class file (if known)
also reads the dictionary file
produces a file in libsvm input format, e.g., validation.tweetext.libsvm/test.tweettext.libsvm and training.tweetext.libsvm


6. Use LibSVM (svm-train and svm-predict) on the training and validation / testing files
i.e., on training.tweetext.libsvm and validation.tweetext.libsvm/test.tweettext.libsvm


7. Prepare final output file to upload to website, using prepare_output.py
reads 'validation.txt' for the tweetids and the decision file produced by libsvm
to give one output file, which can be uploaded directly


-------------------
  HELPING FILES :
-------------------
1. stopwords_small.txt --> Small stopwords list
2. stopwords_big.txt -->  Big stopwords list
3. emoticon_simple.txt --> Emoticon list
4. person_pronoun.txt --> Pronoun list
5. stop_slang.txt --> Tweeter common slang list
