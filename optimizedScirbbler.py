import time
import re 
wordlist=[]
mybool=[]
def check(f,pref,pref_len):
    flag = True
    for i in range(len(f)):
        if f[i][0] == pref[0]:
            word=f[i][:pref_len]
            my_match = re.findall(pref,word)
            if len(my_match) >0:
                mybool.append(flag)
                wordlist.append(f[i])
            else:
                flag = False
                mybool.append(flag)
                if len(mybool)>1:
                    if mybool[i-1] == True:
                        return True 
        else:
            flag = False
            mybool.append(flag)


if __name__ == "__main__":
    start_time= time.time()
    f = open("words.txt", "r")
    f = f.readlines()
    f = [x.strip() for x in f]
    pref = input("Enter the prefix string:")
    pref_len = len(pref)
    flag = check(f,pref,pref_len)
    print(wordlist)

    print("--- %s seconds ---" % (time.time() - start_time))
    