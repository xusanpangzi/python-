import jieba
sentence=input()
words=jieba.lcut(sentence)
txt=open('eleven.txt','r').read()
SensitiveWords=txt.split()
for word in words:
    if word in SensitiveWords:
        s=sentence.replace(word,'**')
print(s)