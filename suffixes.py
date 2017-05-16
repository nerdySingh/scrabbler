import re 
import time
wordlist=[]
mybool=[]
def check(f,suff):
    flag = True
    for i in range(len(f)):
        end_len = len(f[i])
        start_len = end_len- len(suff)
        word = f[i][start_len:end_len]
        my_match=re.findall(suff,word)
        if len(my_match)>0:
            flag = True
            wordlist.append(f[i])
        else:
            flag=False
    return True


if __name__ == "__main__":
    start_time= time.time()
    f = open("words.txt", "r")
    f = f.readlines()
    f = [x.strip() for x in f]
   
    suff = input("Enter the suffix string:")
    flag=check(f,suff)
    if flag == True:
        print(wordlist)
    print("--- %s seconds ---" % (time.time() - start_time))
