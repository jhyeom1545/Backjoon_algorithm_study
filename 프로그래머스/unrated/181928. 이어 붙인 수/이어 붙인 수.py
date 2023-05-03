def solution(num_list):
    hol = ''
    jjack = ''
    for i in range(len(num_list)):
        if(num_list[i]%2==0):
            jjack+=str(num_list[i])
        else:
            hol+=str(num_list[i])
    
    return int(hol) + int(jjack)