def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    for i in range(len(A)):
        if A[0] * B[-1] > A[-1] * B[0]:
            answer+= B.pop() * A.pop(0)
        else:
            answer+= A.pop() * B.pop(0)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer