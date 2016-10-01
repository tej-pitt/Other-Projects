""" Script: Word memoriser
    Function: Makes an application for guessing a word and what it means,
    in another language with a quiz like structure. Every word will have
    multiple choices for answers. 
"""
    


import random

count=0 
score=0 

file1 = open('C:/Users/tejas/Documents/eng.txt','r')
file2 = open('C:/Users/tejas/Documents/ger.txt','r')

f1content= file1.readlines()
f2content= file2.readlines()

while count<15:
    
    wordnum= int(random.randint(0,len(f1content)-1))
    print ('Word:',f1content[wordnum],'')
    options= [random.randint(0,len(f2content)-1),
    random.randint(0,len(f2content)-1),
    random.randint(0,len(f2content)-1)]
        
    options[random.randint(0,2)]= wordnum

    print ('1.',f2content[options[0]]),
    print ('2.',f2content[options[1]]),
    print ('3.',f2content[options[2]]),
    
    answer= int(input('\nYour choice:'))
    
    if options[answer-1] == wordnum:
        input('\n Correcto! Hit enter....')
        score= score + 1
    else:
        input('Wrong! Hit enter....')
    count= count + 1
    
print ('\n Your score is:',score)


