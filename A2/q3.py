'''
Created on Sep 13, 2016

@author: Bharat
'''
import sys,nltk,math

def main(words,fname):
    "Reads text from a file, prints token and frequency."     
    try:         
        file = open(fname, mode='r', encoding='utf-8')         
        text = file.readlines()         
        file.close()     
    except IOError:         
        print("Cannot read from file:", fname)         
        return
    #print(text)
    for x in text:
        words.append(x.split("\t")[2])
    
def entropy(words):
    entropy =0;
    fd = nltk.FreqDist(words)
    tot = len(words)
    for f in fd:
        p = fd[f]/tot
        print(f+"\t"+str(p))
        entropy += p*math.log2(p)
    return entropy
#     print( len(pos))
        

if __name__ == '__main__':
    pos = []
    for i in sys.argv[1:]:
        main(pos,i)
    print("Entropy is :" + str(-entropy(pos)))
#         print("file read: "+i)