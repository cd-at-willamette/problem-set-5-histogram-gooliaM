##################################################
# Name: Julia Martin
# Collaborators: chatgpt for 2 lines
# Estimate of time spent (hr): 30 mins
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    ar_len = (len(array))
    for i in range(ar_len):
        if not(all(len(lst) == len(array[0]) for lst in array)): #chatgpt wrote this
            return False
    
    total_sum = []
    
    for i in range(len(array)):
        sum = 0
        for j in range(len(array[i])):
            sum = sum + array[i][j]
        total_sum.append(sum)
    
    if all(element == total_sum[0] for element in total_sum): #chatgpt wrote this
        return True
            

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))

