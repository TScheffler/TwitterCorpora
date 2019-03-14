# TwitterCorpora

Stuff on extracting Twitter corpora and working with them. 

## `get-emoji-tweets-fromtext.py`

Python script for extracting all tweets (really, lines) containing emoji and sorting them into files by emoji.

### Usage

`get-emoji-tweets-fromtext.py [-h] indir outdir`

### Input

`indir` = input directory of files with tweet texts (one tweet per line)

### Output

The script creates output files in `outdir`, one file per emoji found in the data (and named with that emoji). Each file contains all the tweets from the input which contain that emoji. Note that a tweet with several different emoji will appear in each of the output files.

## `twitter_stopwords_German.txt`

List of useful German stop words for filtering tweets. Language identification must be used afterwards. Format: ['word', # of all tweets containing the word in sample, # of German tweets containing word in sample, German/all ratio]. Thanks to Nikolas Zoeller, FH Potsdam.

## April 2013 German Corpus

The Twitter corpus can be found in its own repository: [https://github.com/TScheffler/GermanTwitterApril2013](https://github.com/TScheffler/GermanTwitterApril2013) (ids only)
