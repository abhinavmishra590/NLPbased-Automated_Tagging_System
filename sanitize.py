'''
Created on Apr 11, 2014

@author: root
'''

import cPickle as pickle
import nltk
from nltk.corpus import stopwords



   
with open('/media/sf_G_DRIVE/nlp/Project/dataset/superuser/idToPostSan.pk', 'rb') as inp:
    idToPost = pickle.load(inp)


#Should've used set not list for stop words. Runtime ~1hr
def remStopWords (str):
    filtered_words = [w for w in nltk.word_tokenize(str) if not w in nltk.corpus.stopwords.words('english')] 
    return filtered_words

#Sanitized posts and saved to file
def sanitizePosts():
    for key,post in idToPost.iteritems():
        post[0] = remStopWords(post[0].lower()) #Remove StopWords and convert to lower
        post[1] = remStopWords(post[1].lower()) #Remove StopWords and convert to lower
        idToPost[key] = post
        
    with open('/media/sf_G_DRIVE/nlp/Project/dataset/superuser/idToPostSan.pk', 'wb') as output:
        pickle.dump(idToPost, output, protocol=0)
        
#Remove punctuation
def remPunct():
    puncSet = set()
    puncSet.add('.')
    puncSet.add('!')
    puncSet.add('?')
    puncSet.add(',')
    puncSet.add(';')
    puncSet.add(':')
    puncSet.add(',')
    
    for key in idToPost.keys():
        post = idToPost[key]
        for word in post[1]:
            if word in puncSet:
                post[1].remove(word)
        idToPost[key] = post
        
    with open('/media/sf_G_DRIVE/nlp/Project/dataset/superuser/idToPostSanPunct.pk', 'wb') as output:
        pickle.dump(idToPost, output, protocol=0)
    

remPunct()