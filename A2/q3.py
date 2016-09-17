'''
Created on Sep 13, 2016

@author: Bharat Vemulapalli
'''
import sys,nltk,math

def main(words,fname):
    #Reads text from a file    
    try:         
        file = open(fname, mode='r', encoding='utf-8')         
        text = file.readlines()         
        file.close()     
    except IOError:         
        print("Cannot read from file:", fname)         
        return
    #pulls the POS tagger for in every line of the text and adds it to a list
    for x in text:
        words.append(x.split("\t")[2])
    
def entropy(words):
    #find the entropy of a list of words in a list
    entropy =0;
    fd = nltk.FreqDist(words) #get frequency distribution
    tot = len(words)
    for f in fd:
        p = fd[f]/tot
        print(f+"\t"+str(p))
        entropy += p*math.log2(p)
    return entropy
        

if __name__ == '__main__':
    pos = [] #empty list for the list of POS taggers from all files
    #Pass all the files in the arguments while running the program
    #Reads all files i.e G01/G02.....G22
    for i in sys.argv[1:]:
        main(pos,i)
    print("\nEntropy is :" + str(-entropy(pos))) #prints the entropy
