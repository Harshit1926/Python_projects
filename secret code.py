choice=int(input("type 1 for creating a secret code type 2 for decode:"))
if choice==1:
    code=input("type your sentence/word here to create a secret code:")
    words=code.split(" ")
    nword=[]
    for word in words:
        if len(word)>=3:
                r1="ghf"
                r2="hhv"
                ncode=r1+word[1:]+word[0]+r2
                nword.append(ncode)
                
        else:
                nword.append(word[::-1])
    print(" ".join(nword))
else:
    code=input("enter a code to decode:")
    words=code.split(" ")
    nword=[]
    for word in words:
        if len(word)>=3: 
            ncode=word[3:-3]
            ncode=ncode[-1]+ncode[:-1]
            nword.append(ncode)
          
        else:
            nword.append(word[::-1])
    print(" ".join(nword))
      
          

