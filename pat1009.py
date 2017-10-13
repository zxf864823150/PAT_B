def S(a):
    return len(a)
def SU(l):
    count = 0
    for i in range(len(l)):
        count+=l[i]
    return count
word_list = input().split(' ')
length_list = list(map(S,word_list))
length = SU(length_list)
if length > 80:
    print(None)
reword_list = word_list[::-1]
for i in range(len(reword_list)):
    if i == len(reword_list)-1:
        print(reword_list[i],end='')
    else:
        print('%s '%reword_list[i],end='')