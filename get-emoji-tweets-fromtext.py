#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Tatjana Scheffler <tatjana.scheffler@uni-potsdam.de>'

# usage: get-emoji-tweets-fromtext.py [-h] indir outdir

#read in tweets and get data for emoji

import fileinput
import sys
import codecs
import csv

#import datetime
#import math
#import os
import argparse

import glob
from pprint import pprint

import emoji
from collections import defaultdict

OUTDIR = ""   # directory where the emoji-tweet files are to be saved
INDIR = "" # directory with tweet text files, one tweet per line


def find_emoji(text, emojitweets):
    # arguments: line, hashtable of tweets by emoji
    emojis_found=[]
    for c in text:
        if c in emoji.UNICODE_EMOJI and not c in emojis_found:
            emojitweets[c].append(text)
            emojis_found.append(c)

                        
def initialize_results_table():
    twit_emoji = defaultdict(list)
    return twit_emoji


def print_emoji_tweets(table,dir):
    for emoji in table:
        with open(dir+emoji, 'w') as ofile:
            for line in table[emoji]:
                ofile.write(line)


####### Twitter #######

def process_twitter(INDIR):
    twit_emoji = initialize_results_table()

    twitfiles = glob.glob(INDIR + "*.txt")
    for ifile in twitfiles:

        for tw in fileinput.input(ifile):

            find_emoji(tw, twit_emoji)
    return twit_emoji

### MAIN

parser = argparse.ArgumentParser(description='Sort tweets into buckets by emoji')
parser.add_argument('indir', type=str, help='Input dir for tweets (one tweet per line)')
parser.add_argument('outdir', type=str, help='Output dir for emoji-tweets (one file per emoji)')

args = parser.parse_args()


emoji_tweets = process_twitter(args.indir)
print_emoji_tweets(emoji_tweets,args.outdir)
