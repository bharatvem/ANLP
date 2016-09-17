import nltk,math,numpy

#Get the data
t = "Bach was the most famous composer in the world, and so was Handel. Handel was half German, half Italian and half English. He was very large. Bach died from 1750 to the present. Beethoven wrote music even though he was deaf. He was so deaf he wrote loud music. He took long walks in the forest even when everyone was calling for him. Beethoven expired in 1827 and later died for this."
t = t.lower() #convert to lower
t1=""
#Remove everything that is not an alphabet
for j in t:
    if j.isalpha():
        t1="".join([t1,j])
# print(t1)
fd = nltk.FreqDist(t1) #get the freq distribution
tot = len(t1) #length of text
entropy,ent = 0,0
ent_list = []
probabs = {}
print("Probabilities of each character in the text are: ")
for i in fd:
    p = fd[i]/tot
    probabs[i]=p #create a dictionary with probabilities of alphabets
    ent = -1*p*math.log2(p)
    ent_list.append(ent)
    entropy += p*math.log2(p)

probabs = sorted(zip(probabs.values(), probabs.keys()), reverse=True)
print(probabs) #prints probabilities of the alphabets in descending order

print("\nentropy is = " + str(-entropy))
# print(list(fd.values()))
# print(ent_list)
print("\nThe variances are: ")
#Get the variance of the characters from the freq distribution
print("variance of the characters:"+str(numpy.var(list(fd.values()))))
#Get the variance of the entropies from the freq distribution
print("variance of the entropies of characters:"+str(numpy.var(ent_list)))

    
    