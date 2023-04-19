#QN1
#longest common substring

'''def longest_common_substring(str1, str2):
    word1 = len(str1)
    word2 = len(str2)
    t= [[0]*(word2+1) for i in range(word1+1)]
    l_length = 0
    l_end_pos = 0
    for i in range(1, word1+1):
        for j in range(1, word2+1):
            if str1[i-1] == str2[j-1]:
                t[i][j] = t[i-1][j-1] + 1
                if t[i][j] > l_length:
                    l_length = t[i][j]
                    l_end_pos = i
            else:
                t[i][j] = 0
    longest_substring = str1[l_end_pos-l_length:l_end_pos]
    return longest_substring

str1 = "fis h"
str2 = "wldwis hde"
print(longest_common_substring(str1, str2))'''      # output: 'is h'  

#QN2
#accept a dictionary and return a list
'''def find_correct(word_dict):
    correct= 0
    almost= 0
    wrong= 0
    
    for word, contestant_spelling in word_dict.items():
        if word == contestant_spelling:
            correct += 1
        elif abs(len(word) - len(contestant_spelling)) > 2:
            wrong += 1
        else:
            wrong_letters= sum([1 for i in range(len(word)) if word[i] != contestant_spelling[i]])
            if wrong_letters <= 2:
                almost += 1
            else:
                wrong += 1
    
    return [correct, almost, wrong]

word_dict = {"THEIR":"THEIR","BUSINESS":"BISINESS","WINDOWS": "WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}

result = find_correct(word_dict)
print(result)'''                                      #O/P-[2,2,1]


#QN3
#DENOMINATION LIST

'''def count_change(amount, denominations):
    if amount == 0:
        return 1
    if amount < 0 or not denominations:
        return 0
    return count_change(amount - denominations[-1], denominations) + count_change(amount, denominations[:-1])
                                                                                                                       #o/p-
amount=int(input("amount:"))                                                                #10
denominations=list(map(int,input("denominations list:").split()))    #10 5 1
print(count_change(amount, denominations)) '''                                     #4


#QN4
#ten_substring
'''def substring(num_str):
    ten_subs = []
    for i in range(len(num_str)):
        for j in range(i + 1, len(num_str) + 1):
            if sum(map(int, num_str[i:j])) == 10:
                ten_subs.append(num_str[i:j])
    return ten_subs

num_str = input("Enter a string of digits: ")           #3523014
ten_subs =substring(num_str)
print("10-substrings:", ten_subs)'''                             #['352', '523', '5230', '23014']

#QN5
#ROTATION OF STRING
s=input().split(",")                                                        #rhdt:246,djdb:2563
stt=[]
numm=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    numm.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2]+ss[:2]
for i in range(len(numm)):
    print(rotate(stt[i],numm[i]))                           #trhd,bdjd

