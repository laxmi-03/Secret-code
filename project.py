import random
import string


while True:
  opt=int(input("Enter 0 for encode or 1 for decode the message: "))

  if opt==0:
    text= input("Enter text to encode: ")
    words=text.split()
    nWord=[]
    for word in words:
      if len(word)<3:
        nWord=word[::-1]
      else:
        word=word[1:]+word[0]
        for i in range(0,3):
          word=random.choice(string.ascii_letters)+ word +random.choice(string.ascii_letters)
      nWord.append(word)
    print(" ".join(nWord))

  else:
    text= input("Enter text to decode: ")
    words=text.split()
    nWord=[]
    for word in words:
      if len(word)<3:
        nWord=word[::-1]
      else:
        stnew=word[3:-3]
        stnew=stnew[-1]+stnew[:-1]
        nWord.append(stnew)
    print(" ".join(nWord))

  ans=input("Do you want to continue? (y/n): ")
  if ans=='n':
    break
