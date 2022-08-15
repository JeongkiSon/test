import itertools
import math
def solution(numbers):
    answer = 0
    
    
    a = list(numbers)
    
    possible = []
    
    #print(a)
    for i in range(1, len(a)+1):
        poss = list(itertools.permutations(a, i))
        
        for k in range(len(poss)):
            res = int(''.join(map(str, poss[k])))
            possible.append(res)
    
    possible = list(set(possible))
    #print(possible)
    
    for i in possible:
        #print(i)
        if (i == 0) or (i == 1):
            continue
        if i == 2:
            answer += 1
            #print("answer up here i:", i)
            continue
            
        cnt = 0
        for x in range(2, int(math.sqrt(i))+1):
            if i % x == 0:
                cnt +=1

            
        if cnt == 0: #소수
            answer += 1
    
    
    return answer