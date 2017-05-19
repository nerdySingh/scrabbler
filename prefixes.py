import time
import re 
wordlist=[]
mybool=[]
def check(f,pref,pref_len):
    flag = True
    for i in range(len(f)):
        if f[i][0] == pref[0]: #checks only those words that match with the 1'st letter of the prefix string.
            word=f[i][:pref_len] #for every string thats is read we concatenate the string into a word based on the lenght of the prefix string.
            my_match = re.findall(pref,word) #used regular expression to match the prefix string and the word.
            if len(my_match) >0: #my_match result is created which is a list of the sub_string of the word that is being matched.
                mybool.append(flag) #if the condition is true, append the flag value to a list called my_bool
                wordlist.append(f[i]) #it is also appended to the word_list.
            else:
                flag = False
                mybool.append(flag)
                if len(mybool)>1:
                    if mybool[i-1] == True:
                        return True  # we know that the dictionary list is sorted, so after the last value is true, if we get a false we can return the word list and end the code. 
        else:
            flag = False
            mybool.append(flag)


if __name__ == "__main__":
    f = open("words.txt", "r") #read the file words.txt for the dictionary to be input in the code represented by "f".
    f = f.readlines() #converted the file values into a list.
    f = [x.strip() for x in f] #the list values have \n appended to them so we remove them.
    pref = input("Enter the prefix string:") #we give the user the previleges of adding the prefix string.
    match = re.findall(r'[a-z]',pref)
    if len(match)>0:
        pref_len = len(pref) #counts the length of the prefix string.
        flag = check(f,pref,pref_len) #calls the function check that returns the boolean value.
        thefile = open('prefixes.txt', 'w')#opens a file named prefixes.txt.
        for item in wordlist:
            thefile.write("%s\n" % item) #writes the word into every new line of the file.
        print("Check the prefixes.txt file for the output values to be generated. ") #the code is printed to be done.
    else:
        print("The input prefix string should be of lower charachters only, eg[abcdefg]")