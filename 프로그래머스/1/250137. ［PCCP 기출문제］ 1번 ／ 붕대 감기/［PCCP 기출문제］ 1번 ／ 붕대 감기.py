def solution(bandage, health, attacks):
    all_turn = attacks[-1][0]
    초당_회복량 = bandage[1]
    user_health = health
    attacked = False
    time = 0
    attack_turn = False
    
    for turn in range(all_turn+1):
        # 추가 회복
        if time == bandage[0]:
            user_health += bandage[-1]
            time = 0
        
        if user_health >= health:
            user_health = health
        
        # 시전
        if attacked == True:
            time = 0
            attacked = False
        time += 1
        
        # 공격
        for attack in attacks:
            if attack[0] == turn:
                attacked = True
                user_health -= attack[1]
                time = 0
                attack_turn = True
        # 초당 회복
        if attack_turn == False:
            user_health += 초당_회복량
        else:
            attack_turn = False
        if user_health <= 0:
            return -1
        # print('user_health: ',user_health, 'turn: ', turn, 'time: ', time)
    return user_health