K, N = map(int,input().split())

lan_list = []

for i in range(K):
    lan_list.append(int(input()))

def solution():
    low = 1 
    high = max(lan_list)
    while True:
        result = 0
        mid = int((low+high)//2)
        for i in lan_list:
            result += i // mid
        # K 총 구해야 하는 개수
        if result >= N:
            low = mid + 1
        else:
            high = mid - 1
        if low > high:
            return high
result = solution()
print(result)