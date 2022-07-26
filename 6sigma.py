import math
my_str = '2.85, 3.38, 3.7, 3.33, 3.49, 3.7, 3.5, 3.1, 3.42, 3.9, 3.5, 3.37, 3.45,' \
         ' 3.67, 2.65, 3.66, 3.45, 4, 4.2, 3.7, 3.38, 3.51, 2.92, 2.9, 2.7, 3.25, ' \
         '3.5, 3.9, 3.6, 3.85, 2.9, 2.6, 2.63, 3.59, 3.48, 2.78, 3.98, 3, 2.97, 3.1, ' \
         '3.3, 3.7, 2.72, 3.46, 3.39, 2.64, 2.78, 3.7, 3.05, 3.4'
my_list = my_str.split(',')

sum = 0
for i in range(len(my_list)):
    sum += float(my_list[i])
ave = round(sum/50, 3)
print(ave)

sum = 0
for i in range(len(my_list)):
    sum += (float(my_list[i])-ave)**2
spr = round(sum/50, 3)
print(spr)

st_dev = round(math.sqrt(spr), 3)
print(st_dev)