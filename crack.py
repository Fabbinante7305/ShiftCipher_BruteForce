#This will take Ciphertext and brute force every combination to get a sensical Plaintext value

cipherText = input("Enter CIPHERTEXT value:\t")

letterList = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
valueList = list(letterList.values())
keyList = list(letterList.keys())
position = 0
place = 0
tempLetter = 0
valueToFind = 0
#Cycles through every possible key value
for j in range(0,25):
    print("\nKey Value: " + str(j))
    #Cycles through each letter in the Ciphertext value
    for i in cipherText:
        tempLetter = letterList.get(i) #Gets the value attatched to the current letter in the dictionary
        place = tempLetter-j #Gets the new value by shifting according to the current key (j) value
        
        #This accounts for negative indexes and will make sure we start reading from the end of the alphabet
        if(place <0):
            place = place+26
        
        position = valueList.index(place) #Gets the position of where the value is found in the dictionary
        newLetter = keyList[position] #Using the location of the value, we now get the appropriate dictionary key value which ends up being the new letter
        print(newLetter,end = "")

            
    
