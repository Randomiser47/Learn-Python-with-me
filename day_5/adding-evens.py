# even_sum = 0
# for i in range(1,101):
#     if i%2==0:
#         even_sum+=i
# even_sum+=1
# print(even_sum)

even_sum = 0
for i in range(2,101,2):
    even_sum+=i
    print(i)
print(even_sum)