def solution(number, limit, power):
    m_power = {}
    result = 0
    for i in range(1,number+1):
        num=0
        sqrt_i = int(i ** 0.5) # 제곱근 구하기
        for j in range(1, sqrt_i+1): # 제곱근까지만 반복문 돌기
            if i % j ==0:
                num += 1
                if j != i // j: # 중복 방지
                    num += 1
        m_power[i] = num
    for i in range(1, number+1):
        if m_power[i] > limit:
            m_power[i] = power
        result += m_power[i]
    return result
