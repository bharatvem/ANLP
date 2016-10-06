'''
Created on Oct 1, 2016

@author: Beast
'''
from nltk.corpus import brown
from collections import Counter,defaultdict
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import math
from _collections import OrderedDict

def main(s):
    # Adding *ST* to the start and *END* to the end of each sentence in Brown corpus
    brown_tag_words = []
    for i in brown.tagged_sents():
        brown_tag_words.append( ("ST","ST") )
        brown_tag_words.extend([ (word,tag) for (word, tag) in i ])
        brown_tag_words.append( ("END","END") )
        
    # Get tokens and tags from the edited corpus and add it Counter datatype
    tokens,tags = zip(*brown_tag_words)
    tagcounter = Counter(tags)
    tokencounter = Counter(tokens)
    tokencounter[0]
 
    # Get the list of possible tags for each tokens in a dictionary format
    tokenTags = defaultdict(Counter) 
    for token, tag in brown.tagged_words():     
        tokenTags[token][tag] +=1
    
    # Get the list of possible tag combinations and their counts in dictionary format
    tagTags = defaultdict(Counter)
    posBigrams = ngrams(tags,2)
    for tag1, tag2 in posBigrams:     
        tagTags[tag1][tag2] += 1
        
    # Get the tokenized sentence from the user
    words = word_tokenize(s)
    s_tag = OrderedDict()
    
    # Get the most probable tag for each word in the given sentence 's'
    for i in range(0,len(words)): 
#         print("word is :"+words[i]+str(list(tokenTags[words[i]])))
        minimum,actual_tag = -9999999999999,' '
        listprobs = []
        for j in tokenTags[words[i]]:
            tcj,tci = 0,0
            if tagcounter[j] == 0:
                tcj = 0.000001
            else:
                tcj = tagcounter[j]
            if tagcounter[words[i-1]]==0:
                tci = 0.000001
            else:
                tci = tagcounter[words[i-1]]
            #If     
            p_tokenTags = tokenTags[words[i]][j]/tcj
            
            # If first word, compare it with the *ST* as the starting tag
            # else consider the tag of the previous word
            # Calculating the probability of the current tag provided the previous word's tag is known 
            if i == 0:
                p_tagTags = tagTags["ST"][j]/tagcounter["ST"]
            else:
                p_tagTags = tagTags[s_tag[words[i-1]]][j]/tci
            # Calculate the probability for the current expected tag 
            prob = p_tokenTags * p_tagTags
            #Applying log 
            if prob == 0: # if probability is 0, setting it to a low value
                lprob = math.log2(0.0000000000000001)
            else:
                lprob = math.log2(prob)
            listprobs.append((j,lprob)) #add the tag & its probability for a single word
            # Get the tag which has the maximum probability among the tags for each word 
            if lprob > minimum :
                minimum = lprob
                actual_tag = j
#         print(listprobs)
        s_tag[words[i]]=actual_tag # add the most probable tag to each word onto a dictionary s_tag
        
#     print(s_tag)
    return(s_tag)
 
    
if __name__ == '__main__':
#     sente = input("Enter sentence: ")
    sente = 'time flies like an arrow'
    print("OUTPUT WITH tags FOR EACH TOKEN:")
    qq = main(sente)
    print(qq)