import sys
import re
import collections
import time
word_list=[]

def checkLetterInList(u_l,content,remaining_list):
    remaining_list = remaining_list.replace(u_l,"")
    for i in range(len(content)):
        if u_l == content[i][0]:
            freq = collections.Counter(content[i])
            temp = u_l
            if freq[temp] <=1:
                for v in remaining_list:
                        if freq[v] >1:
                            flag = False
                             #print(flag)
                            break
                        else:
                            flag = True
                if flag == True:
                    remaining_list = sys.argv[1]
                    flag = True
                    #freq = collections.Counter(content[i])
                    for k in content[i]:
                        if k not in remaining_list:
                            flag=False
                            break
                    if flag == True:
                        word_list.append(content[i])

    thefile = open('my_scrabbler.txt', 'w')
    for item in word_list:
        thefile.write("%s\n" % item)

if __name__ == "__main__":
    start_time= time.time()
    file = open("words.txt", "r") #reading the dictionary file words.txt
    content = file.readlines()
    content = [x.strip() for x in content]  #striping trailing new lines from content.
    user_input = sys.argv[1] #reading values from the commandline
    regexp = re.compile(r"(.)\1.*[a-z]")
    freq = collections.Counter(user_input)
    flag = True
    for i in user_input:
        if freq[i]>1:
            flag = False
            break
        else:
            flag = True


#separating every charachter and forming words with those
    if flag == True:
        for i in user_input:
            checkLetterInList(i, content, user_input)
        print("Check output in my_scrabbler.txt as file has been generated.")
    else:
        print("You cannnot have double charachters in input.")
