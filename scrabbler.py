import sys
import collections
word_list=[]

def checkLetterInList(u_l,content,remaining_list):
    
    remaining_list = remaining_list.replace(u_l,"")
    for i in range(len(content)):
        if u_l == content[i][0]:
            freq = collections.Counter(content[i])
            temp = u_l
            for j in range(len(u_l)):
                if freq[temp] <=1:
                    for v in remaining_list:
                         #flag = checkRemaininLetters(v,content[i])
                         #print(flag
                         #print(freq[v])
                         if freq[v] >1:
                             flag = False
                             #print(flag)
                             break
                         else:
                            flag = True
                    if flag == True:
                        word_list.append(content[i])
    
    thefile = open('test.txt', 'w')
    for item in word_list:
        thefile.write("%s\n" % item)
                             

    
                

            


file = open("words.txt", "r") #reading the dictionary file words.txt
content = file.readlines()
content = [x.strip() for x in content]  #striping trailing new lines from content.
user_input  = sys.argv[1] #reading values from the commandline
#writing code for ebery letter in the user input'''

#separating every charachter and forming words with those
for i in user_input:
    checkLetterInList(i,content,user_input)

    


'''
#concatenates the list
 word_list = []
    remaining_list = remaining_list.replace(u_l,"")
    print(remaining_list)
["abbess","abbesses","abbey","abbeys","abbot","abbots"]

    '''