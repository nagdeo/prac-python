'''str="Aparna"
cnt=0
for char in str:
    cnt=cnt+1
print(cnt)
print(len(str))'''
'''
Str1="google.com"

for char in Str1:
     cnt=0
     for ch in Str1:
         if(char==ch):
             cnt=cnt+1
     print(char,":",cnt)'''
'''
Str2="google.com"
dict={}
for char in Str2:
    keys=dict.keys()
    if char in keys:
        dict[char]+=1
    else:
        dict[char]=1
print(dict)'''
'''
print("Enter the string")
str=input()

if len(str)<2:
    print("Empty String")
else:
    print(str[0:2] + str[-2:])'''
'''
str1="restart"
char=str1[0]
str1=str1.replace(char,'$')
print(char+str1[1:])'''
'''
str="abc,xyz"
print(str.split(','))
print (str[4]+str[5]+str[2]+" "+str[0]+str[1]+str[6])
words = str.split(',')
print(words[1])
str1=words[0]
str2=words[1]
newa=str2[0:2]+str1[2:]
newb=str1[0:2]+str2[2:]
print(newa, " ",newb)
o/p:
['abc', 'xyz']
xyc abz
xyz
xyc   abz
'''

'''
str1=input()
if(str1[-3:]!='ing'):
    print(str1+'ing')
else:
    print(str1+'ly')
#o/p bowling
#bowlingly
#simmi
#simmiing'''


'''
words=str1.split()
print(words)
for id, word in enumerate(words):
   if word=='not':
        print(id,word)
   if word=='poor':
       print(id,word)'''
'''
str1='The lyrics is not that poor'
snot = str1.find('not')
spoor = str1.find('poor')
print(snot,spoor)
if spoor>snot and snot>0 and spoor>0:
    print(str1.replace(str1[snot:],'good'))'''
'''
def longerWord(a):
    for word in a:
        for words in a:

           if len(word)>len(words):
               longer = word
        return word


print(longerWord(['a','avs','jjjjj']))'''

Word='defr'


if Word=='defer' or Word=='if' or Word=='for':
        print(Word," is a keyword")
else:
        print(Word,"is not a keyword")







