

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 23:39:43 2016

@author: hagit

input : directory with fre text files  , filenames are *.txt 

Text example :  Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the
book her sister was reading, but it had no pictures or conversations in it, ‘and what is the use of a book,’ thought Alice ‘without pictures or
conversations?’

output : *.csv file per each input file , in the following format 

| input file Directory ,|input file name ,|stemmed word ,| POS ,|original word |
--------------------------------------------------------------------------------

For example 

C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,king,NN,king
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,queen,NN,queen
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,hearts,NN,heart
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,seated,NN,seat
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,throne,NN,throne
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,arrived,NN,arriv
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,great,JJ,great
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,crowd,NN,crowd
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,assembled,NN,assembl
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,sorts,NN,sort
C:/Users/user/Documents/Python Scripts/thesis/books/alice,11.txt,little,NN,littl


You must Download  NLTK libraries as following : 
 
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('punkt')
>>> nltk.download('wordnet')
>>> nltk.download('averaged_perceptron_tagger') 
"""
# encoding=utf-8
import os
import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize 
import re 
 #from porter2stemmer import Porter2Stemmer
from nltk.stem import WordNetLemmatizer
wnl= WordNetLemmatizer()
#stemmer = Porter2Stemmer()
stemmer = SnowballStemmer('english')
import fnmatch
import string

matches = []

 
stopset = set(stopwords.words('english'))
ps = nltk.PorterStemmer()
snow = SnowballStemmer('english')
book_dir='C:/Users/user/Documents/Python Scripts/thesis/books/alice'
"""
Token
remove stop words
lemm
pos

"""
for root, dirnames, filenames in os.walk(book_dir, topdown = True):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))
        #print (filename)

for book_filename in matches:
    print("Reading '{0}'...".format(book_filename))
     
    str2=book_filename.split('\\')
    n=len(str2)
    book_chapter=str2[n-1]
    book_dir   = str2[n - 2]
     
    file=open(book_filename,'r')      # /datagen3/hagit/university/stem/all'+id+'.json','r')
    out_filename = book_filename + '.csv'  #''/datagen3/hagit/university/stem/all_words_stem_nltk.csv'
    try:
        os.remove(out_filename)
    except OSError:
        pass


    out     = open(out_filename,'w' )

    for line in file:
        line=unicode(line, errors='ignore')
        
        #toker = RegexpTokenizer(r'((?<=[^\w\s])\w(?=[^\w\s])|(\W))+', gaps=True)
        #regwords = toker.tokenize(line)
        
        my_clean_text=''

        """ phase1 tokenize,lower,remove stopwords """
        stop_words = set(stopwords.words('english'))
        stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','’','‘','--','“','”','!','*','-'])
        # tokenize
        #word_tokens = word_tokenize(line)
        word_tokens = wordpunct_tokenize(line)
        # lowercase
        lower_word_tokens = [w.lower() for w in word_tokens]
        # remove stop words
        filtered_sentence = [w for w in lower_word_tokens if not w in stop_words and w not in string.punctuation and w not in ("’","‘","--","“","”","!",'(',')',';','?','.','\n','') ]
        #filtered_sentence = [w for w in lower_word_tokens if not w in stop_words] # and w not in string.punctuation and w not in ("’","‘","--","“","”","!") ]

        """ phase2 stemmer , lemmetizer  """

        for w in filtered_sentence:
            # First lemmetizer
            #lw = wnl.lemmatize(w)
            #myword = stemmer.stem(lw)
            
            #Stemmer
            # replace special characters 
            w = re.sub('[^a-zA-Z0-9\n\.]', ' ', w)
            myword = stemmer.stem(w)

            my_clean_text = my_clean_text+' '+myword

            """ phase3 tag POS """

            tagged_word = nltk.pos_tag(nltk.word_tokenize(myword))

            for (theme,tag) in tagged_word:
                try:
                    if tag.encode('utf-8').strip()!='.':
                        out.write(book_dir+','+book_chapter+','+w+','+tag.encode('utf-8').strip()+','+theme.encode('utf-8').strip()+'\n')
                        #print (dir_name+','+book_chapter+','+w+','+tag.encode('utf-8').strip()+','+theme.encode('utf-8').strip()+'\n')
                except:
                    pass
    out.close()
    file.close()
