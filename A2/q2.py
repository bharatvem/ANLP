import nltk,math

t = "Bach was the most famous composer in the world, and so was Handel. Handel was half German, half Italian and half English. He was very large. Bach died from 1750 to the present. Beethoven wrote music even though he was deaf. He was so deaf he wrote loud music. He took long walks in the forest even when everyone was calling for him. Beethoven expired in 1827 and later died for this."
t = t.lower()
t1=""
for j in t:
    if j.isalpha():
        t1="".join([t1,j])
print(t1)
fd = nltk.FreqDist(t1)
tot = len(t1) #length of text
entropy = 0
for i in fd:
    p = fd[i]/tot
    print(i + "\t" + str(p)) #print probability
    entropy += p*math.log2(p)
print("entropy = " + str(-entropy))
    
    