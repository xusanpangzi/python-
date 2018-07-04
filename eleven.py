
word=input()
txt=open('eleven.txt','r').read()
words=txt.split()
if word in words:
    print("Freedom")
else:
    print("Human right")