import nltk; nltk.download('stopwords')

import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

import acquire

def basic_clean(string):
    '''
    This function takes in a string and normalizes it for nlp purposes
    '''
    # lowercase the string
    string = string.lower()
    # return normal form for the unicode string, encode/remove ascii
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8')
    # breaks down the string by keeping alphabet letters, numbers, apostraphes and spaces
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    
    return string


def tokenize(string):
    '''
    This function takes in a string and tokenizes it
    '''
    # create the tokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    # use the tokenizer, return as a string
    string = tokenizer.tokenize(string, return_str = True)
    
    return string

def stem(text):
    
    # create a porter stemmer
    ps = nltk.porter.PorterStemmer()
    
    # loop through the text to stem the words
    stems = [ps.stem(word) for word in text.split()]
    
    return stems