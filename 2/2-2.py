t = list(input())

print(t)

sub =[]
sum = 0
for i in range(len(t)):
    if '1'<=t[i]<='9':
        sum += int(t[i])
    else:
        sub.append(t[i])
        
sub = sorted(sub)
ans = "".join(sub)
print(ans + str(sum))