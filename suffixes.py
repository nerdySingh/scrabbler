import re 
import time
wordlist=[]
mybool=[]
def check(f,suff):
    flag = True
    for i in range(len(f)):
        end_len = len(f[i]) #checks for the length of the string.
        start_len = end_len- len(suff) #checks for the length of the suffix to be found in the string.
        word = f[i][start_len:end_len] #the concatenation of the start and the end length.
        my_match=re.findall(suff,word) #regex to use to to find any matches in the string
        if len(my_match)>0:
            flag = True
            wordlist.append(f[i])
        else:
            flag=False
    return len(wordlist)


if __name__ == "__main__":
    start_time= time.time()
    f = open("words.txt", "r")
    f = f.readlines()
    f = [x.strip() for x in f]
   
    suff = input("Enter the suffix string:")
    flag=check(f,suff)
    if flag > 0:
        #print(wordlist)
        thefile = open('suffixes.txt', 'w')#opens a file named suffixes.txt to be written.
        for item in wordlist:
            thefile.write("%s\n" % item) #writes the word into every new line of the file.
        print("Check the suffixes.txt file for the output values to be generated. ") #the code is printed to be done.
    else:
        print("No such suffixes were found.")