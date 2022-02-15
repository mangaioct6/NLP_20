#!/usr/bin/env python
import sys
import pandas as pd
# in order to count the same and different words I am  initiating some variables
current_word = None
word_count = 0
word = None

# creating a list to create df. Because from df, I can easily sort word count.
word_list=[]

# take the words from mapper and count it.
for line in sys.stdin: # took this from mapper
    line = line.strip()

    # separating word and count 
    word, count = line.split("\t",1)
   
    # make sure oyr count is integer
    count = int(count)
  #  l_word = [i.lower() for i in word]
    
    # sorting words and if we have multiple same word, we increment the count for that word instead of printing them again and again
    if current_word == word:
        word_count +=1

    else:
    #    if current_word:
    #        print(current_word + "\t" + str(word_count))

        current_word = word
        word_count = count 
    word_list.append({'word':current_word,"count":word_count})
# the last word is iterating in the else condition. But it wasn't printing. To print the last word using below condition
if current_word == word:
  print(current_word + "\t" + str(word_count))

# creating word dataframe 
word_df=pd.DataFrame(word_list,columns = ['word','count'])

# printing words and counts based on its frequency in descending order
print(word_df[['word','count']].groupby(['word']).max().sort_values(ascending = False, by = 'count'))


# My git bash command
# cat ../cats_txt.txt|./mapper.py|sort|./reducer.py
