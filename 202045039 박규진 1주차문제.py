import pandas as pd
import matplotlib.pyplot as plt

#1번
str = '20201231Thursday'
year = '2020'
print(year)
mmdd = '1231'
print(mmdd)
day = 'Thursday'
print(day)

#2번
a = ['쓰','레','기','통']
a.reverse()
print(a)

#3번
dic = {'year':2020,'mm':12,'dd':31,'day':'Thursday','weather':'snow'}
print(dic.keys())
print(dic.values())

#4번
for i in range(1,6):
    for k in range(i):
        print('*', end = "")
    print()

#5번
def avg(*args):
    sum = 0
    for num in args:
        sum += num
    
    return print(sum / len(args))

avg(5, 3, 12, 9)
avg(2.4, 3.2, 7.3)
avg(10, 5)

#6번

amountdic = [[500,450,520,610],[690,700,820,900],[1100,1030,1200,1380],[1500,1650,1700,1850],
                   [1900,2020,2300,2420],[1020,1600,2200,2500]]
yeardic = [2015,2016,2017,2018,2019,2020]
quarterdic = ['1분기','2분기','3분기','4분기']
df1 = pd.DataFrame(amountdic, index = yeardic, columns = quarterdic)

#쓰기권한 에러남 df1.to_csv('C:\작업')

#7번
x = range(len(quarterdic))
for i in range (0,6):
    plt.plot(x,amountdic[i])


plt.title('2015~2020 Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
xLabel = ['first','second','third','fourth']
plt.xticks(x,xLabel,fontsize=10)
plt.show()