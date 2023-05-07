def solution(n, m):
    a, b = max(n, m), min(n, m)
    while b > 0: # b가 0보다 같거나 작아질 때 멈춤
        tmp = a % b # a를 b로 나눈 나머지
        a = b # a는 작은 값이 되고
        b = tmp # b는 a를 b로 나눈 나머지
    gcd = a
    # 최소공배수 구하기
    lcm = n * m // gcd
    # 유클리드 호제법은 두 수 a, b (a > b)에 대해서 a를 b로 나눈 나머지를 r이라고 할 때,
    # b와 r의 최대공약수와 a와 b의 최대공약수가 같다는 원리를 바탕으로 합니다.
    # 이를 반복하여 r이 0이 될 때의 b값이 최대공약수가 됩니다.
    return [gcd, lcm]
    