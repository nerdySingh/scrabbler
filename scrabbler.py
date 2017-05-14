import sys
import collections
word_list=[]

def checkLetterInList(u_l,content,remaining_list):
    
    remaining_list = remaining_list.replace(u_l,"")
    for i in range(len(content)):
        if u_l == content[i][0]:
            freq = collections.Counter(content[i])
            temp = u_l
            #for j in range(len(u_l)):# i guess i dont need the loop i was right 
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
                    freq = collections.Counter(content[i])
                    for k in content[i]:
                        if k not in remaining_list:
                            flag=False
                            break
                    if flag == True:
                        word_list.append(content[i])
    
    thefile = open('test_without_j_loop.txt', 'w')
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