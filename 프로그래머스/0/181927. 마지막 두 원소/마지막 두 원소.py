# def solution(num_list):
#     if int(num_list([-1]))>int(num_list([-2])):
#         num_list.append(int(num_list[-1])-int(num_list[-2]))
#     else:
#         num_list.append(int(num_list[-1]*2))
#     return num_list
def solution(num_list):
    if int(num_list[-1]) > int(num_list[-2]):
        num_list.append(int(num_list[-1]) - int(num_list[-2]))
    else:
        num_list.append(2*num_list[-1])
    return num_list