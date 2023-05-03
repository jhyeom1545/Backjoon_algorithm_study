def solution(num_list):
    sum = 0;
    rhq = 1;
    for i in range(len(num_list)):
        sum+=num_list[i]
        rhq*=num_list[i]
    print(sum**2)
    print(rhq)
    return 1 if sum**2 > rhq else 0