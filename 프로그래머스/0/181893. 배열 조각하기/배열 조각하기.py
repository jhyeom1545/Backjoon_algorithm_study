def solution(arr, query):
    for k, v in enumerate(query):
        if k == 0 or k % 2 == 0:
            # 뒷부분 자르기
            arr = arr[:v+1]
        else:
            # 앞부분 자르기
            arr = arr[v:]
    return arr