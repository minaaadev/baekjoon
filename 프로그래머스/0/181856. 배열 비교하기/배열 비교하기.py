def solution(arr1, arr2):
    answer = 0
    if len(arr1)<len(arr2):
        return -1
    elif len(arr1)>len(arr2):
        return 1
    
    #두 배열의 길이가 같다면
    sum1=sum(arr1)
    sum2=sum(arr2)
    
    if sum1>sum2:
        return 1
    elif sum1<sum2:
        return -1
    else:
        return 0
    return answer