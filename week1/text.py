'''
Created on Aug 26, 2016

@author: Beast
'''
import nltk

def main():
    print("you are in main")
    a = "I'm bharat. starting to study python and nltk. I will use it in Natural Language Processing"
#     tokens = nltk.word_tokenize(a)
    fd = nltk.FreqDist(a)
    for x in fd:
        print(x + "\t" + str(fd[x]))
    
if __name__ == '__main__':
    print("You are in text.py")
    main()