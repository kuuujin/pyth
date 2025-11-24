coin_value = [500,100,50,10,5,1]
num_coin = [0 for _ in range(6)]
count = 0

change = int(input("거스름돈을 입력하세요[0-999]: "))
i = 0
print(f"{change} 원의 거스름돈은 다음과 같다:")
while(change > 0):
    num_coin[i] = change // coin_value[i]
    count += num_coin[i]
    change = change % coin_value[i]
    if(num_coin[i] > 0): print(f"{coin_value[i]}원짜리 동전 {num_coin[i]}개")
    i+=1
print("거스름돈에 포함되는 동전들의 수: ",count)