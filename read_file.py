#reading writing files
#search a pattern and extract the floating point number at the end of it.
#calculate the average of those values and print the amount of lines it occurs on. 

import statistics
fname = input('Enter file name: ')

try:
    fhand = open(fname)
except:
    print ("File cannot be opened" , fname)
    if fname == 'na na boo boo':
        print ("NA NA BOO BOO TO YOU TOO! \n")
        print ("You have been punked mate!")
        exit()
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        values = float(line[-7:])
        print (values)
        a = [values]
        mean = statistics.mean(a)
        
print ("Average confidence value: " , mean)        
print ("The no of times the line occurs is " , count)

        



