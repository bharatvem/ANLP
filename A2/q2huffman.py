'''
Created on Sep 15, 2016

@author: Bharat Vemulapalli
'''
# from huffman import *
import nltk
def getencode(ls):
    ls1 = {}
    for i in ls:
        print(bin(i))
        ls1[ls[i]]=bin(i)
    return ls1

def main():
    t = "Bach was the most famous composer in the world, and so was Handel. Handel was half German, half Italian and half English. He was very large. Bach died from 1750 to the present. Beethoven wrote music even though he was deaf. He was so deaf he wrote loud music. He took long walks in the forest even when everyone was calling for him. Beethoven expired in 1827 and later died for this."
    t = t.lower() #convert to lower
    t1=""
    d={}
    #Remove everything that is not an alphabet
    for j in t:
        if j.isalpha():
            t1="".join([t1,j])
    fd=nltk.FreqDist(t1)
    for x in fd:
        print(x+":"+str(fd[x]))
        d[x]=fd[x]
    listdes = sorted(d,key=d.__getitem__,reverse=True)
    print(listdes)
    print(getencode(listdes))
    

        
    

if __name__ == '__main__':
    main()