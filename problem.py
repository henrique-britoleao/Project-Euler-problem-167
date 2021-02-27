################################################################################
# Project Euler: Problem 167
################################################################################
import time
def get_next_n(last_n, sums_dict):
    delta = 1
    while True:
        try:
            if sums_dict[last_n + delta] == 1:
                del sums_dict[last_n + delta] # reduce size of dict stored in memory
                return (last_n + delta, sums_dict)
            else:
                del sums_dict[last_n + delta] 
                delta += 1
        except:
            delta += 1 

def problem_167(v, n_iter):
    sequence = [2, v]
    sums = {}
    count = 0 
    while count < n_iter:
        count += 1
        for item in sequence[:-1]:
            temp = sequence[-1] + item
            sums[temp] = sums.get(temp, 0) + 1 # counts the number of ways a number 
                                            # can be represented as a sum of 
                                            # previous items
        next_n, sums = get_next_n(sequence[-1], sums)
        sequence.append(next_n)
    return sequence

################################################################################
# Introduce knowledge of even numbers
################################################################################

def problem_167_v2(v, n_iter):
    sequence = [2, v]
    sums = {}
    count = 0 
    while count < n_iter:
        count += 1
        if count < (v+7)/2:
            for item in sequence[:-1]:
                temp = sequence[-1] + item
                sums[temp] = sums.get(temp, 0) + 1 # counts the number of ways a number 
                                                # can be represented as a sum of 
                                                # previous items
        elif count == (v+7)/2:
            sums = {key:value for key, value in sums.items() if key%2 != 0}
            temp_1 = sequence[-1] + 2
            temp_2 = sequence[-1] + 2*v+2
            sums[temp_1] = sums.get(temp_1, 0) + 1
            sums[temp_2] = sums.get(temp_2, 0) + 1
            
        else: 
            temp_1 = sequence[-1] + 2
            temp_2 = sequence[-1] + 2*v+2
            sums[temp_1] = sums.get(temp_1, 0) + 1
            sums[temp_2] = sums.get(temp_2, 0) + 1
        next_n, sums = get_next_n(sequence[-1], sums)
        sequence.append(next_n)
    return sequence

# start_time = time.time()
# problem_167_v2(5, 1e7)
# print(f'Run time: {time.time() - start_time}')

################################################################################
# Optimized version
################################################################################

# def get_next_n_opt(n_hat, sequence, v):
#     test_1 = 2*(n_hat-1) + 1 in sequence
#     test_2 = 2*(n_hat-v-1) + 1 in sequence
#     if test_1 ^ test_2:
#         return 2*n_hat + 1
#     else:
#         pass
             
         
# def problem_167_opt(v, n_items):
#     sequence = [2, v]
#     sums = {}
#     largest_even = 2*v + 2
#     largest_even_i = (v+7)/2
#     while len(sequence) < largest_even_i:
#         for item in sequence[:-1]:
#             temp = sequence[-1] + item
#             sums[temp] = sums.get(temp, 0) + 1 
#         next_n, sums = get_next_n(sequence[-1], sums)
#         sequence.append(next_n)

#     del sums
#     sequence = set(sequence) # optimize search times
#     n_hat = int(largest_even/2) # int avoids float outputs
    
#     while len(sequence) < 32 + 1 + largest_even_i:
#         sequence.add(get_next_n_opt(n_hat, sequence, v))
#         n_hat += 1

#     return sequence

