def solution(num_list):
    answer = 0
    odd=""
    even=""
    for num in num_list:
        if num%2!=0:
            odd+=str(num)
        if num%2==0:
            even+=str(num)
    answer=int(odd)+int(even)
    return answer