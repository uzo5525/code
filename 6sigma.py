import math
import matplotlib.pyplot as plt
import numpy as np

# 문자열 추출
my_str = '2.85, 3.38, 3.7, 3.33, 3.49, 3.7, 3.5, 3.1, 3.42, 3.9, 3.5, 3.37, 3.45,' \
         ' 3.67, 2.65, 3.66, 3.45, 4, 4.2, 3.7, 3.38, 3.51, 2.92, 2.9, 2.7, 3.25, ' \
         '3.5, 3.9, 3.6, 3.85, 2.9, 2.6, 2.63, 3.59, 3.48, 2.78, 3.98, 3, 2.97, 3.1, ' \
         '3.3, 3.7, 2.72, 3.46, 3.39, 2.64, 2.78, 3.7, 3.05, 3.4'
my_list = my_str.split(',')

# 평균
sum_list = 0
for i in range(len(my_list)):
    sum_list += float(my_list[i])
ave = round(sum_list/len(my_list), 3)
print(ave)

# 분산
sum_list = 0
for i in range(len(my_list)):
    sum_list += (float(my_list[i])-ave)**2
spr = round(sum_list/len(my_list), 3)
print(spr)

# 표준 편차
st_dev = round(math.sqrt(spr), 3)
print(st_dev)

# 시그마 배수 값
sig1 = round(1 / st_dev, 2)
print(sig1)
sig2 = round(0.5 / st_dev, 2)
print(sig2)
print(f'기준 한도가 +=1일 경우, 시그마 배수는 {sig1}입니다.')
print(f'기준 한도가 +=0.5일 경우, 시그마 배수는 {sig2}입니다.')

# 그래프
x = np.linspace(ave-2, ave+2, 100)
y = (1 / np.sqrt(2 * np.pi * spr)) * np.exp(-(x-ave)**2 / (2 * spr))
plt.figure(figsize=(8, 8))
plt.plot(x, y, 'k')
plt.vlines(ave+1, 0, 1.5, colors='red')
plt.vlines(ave-1, 0, 1.5, colors='red')
plt.vlines(ave+0.5, 0, 1.5, colors='blue')
plt.vlines(ave-0.5, 0, 1.5, colors='blue')
plt.show()
