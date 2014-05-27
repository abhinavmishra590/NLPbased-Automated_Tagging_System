'''
Created on Apr 16, 2014

@author: root
'''

import random 
import cPickle as pickle
#from sklearn.datasets import fetch_20newsgroups
#from sklearn.feature_extraction.text import TfidfVectorizer
#vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,stop_words='english')
import os

with open('/media/sf_G_DRIVE/nlp/Project/dataset/superuser/idToPost.pk', 'rb') as inp:
    idToPost = pickle.load(inp)
    
with open('/media/sf_G_DRIVE/nlp/Project/dataset/superuser/idToPostSan.pk', 'rb') as inp:
    idToPostSan = pickle.load(inp)

