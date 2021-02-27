################################################################################
# Simple Sequence Generator
################################################################################

def get_next_n(last_n, sums_dict):
    '''Returns smallest key in dictionary with value = 1'''
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

def ulam_generator(v, n_iter):
    '''Generates first n_iter+2 items of U(2,v) sequence'''
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
# Bonus: optimal sequence generator
################################################################################

def ulam_generator_optim(v, n_iter):
    '''Generates first n_iter+2 items of U(2,v) sequence'''
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
            # erase all even terms from dictionary
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