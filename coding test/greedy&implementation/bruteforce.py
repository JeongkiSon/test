a = int(input())

totaltime = a * 60 * 60 + 59 * 60 + 59 #초임

h = 0
m = 0
s = 0

cnt = 0
for i in range(totaltime):
    s += 1
    
    if s == 60:
        s = 0
        m +=1
        
        if m == 60:
            m = 0
            h += 1
    
    
    if ('3' in str(s)) or ('3' in str(m)) or ('3' in str(h)):
        cnt += 1
        #print(h, m, s, cnt)
        
print(cnt)   
