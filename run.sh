#!/bin/sh

echo "Running the input parsers ...."
echo ""
echo " ..... training file generation ....."
python parse_input_files.py training.txt training.tweetext.raw 1
echo ""
echo " ..... test file generation ....."
python parse_input_files.py test.txt test.tweetext.raw 0

echo "Filtering text files ..."
python filter_text.py

echo "Preparing word dictionary ..."
python prepare_word_dict.py

echo "Writing files in libsvm format ..."
python write_libsvm_format.py

echo "Using svm ..."
#svm-scale -l 0 -u 1 training.tweetext.libsvm
svm-train -t 0  training.tweetext.libsvm
svm-predict  tests.tweetext.libsvm training.tweetext.libsvm.model output

echo "preparing final output ..."
python prepare_output.py


