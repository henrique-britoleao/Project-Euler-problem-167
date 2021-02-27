import problem
import sys

class Ulam:
    '''
    # TODO
    '''
    def __init__(self, n):
        self.n = n 
        self.__periods = [32, 26, 444, 1628, 5906, 80, 126960, 380882, 2097152]
        self.__fund_diff = [126, 126, 1778, 6510, 23622, 510, 507842, 1523526,
                            8388606]
        self.largest_even = 4*n + 4
        self.largest_even_i = int((2*n + 8)/2)
    
    def get_item(self, k):
        '''
        # TODO
        '''
        self.get_first_elements()
        if k < self.largest_even:
            print(f'The {k}th element of the sequence U(2,{2*self.n + 1}) is: {self.first_elements[int(k-1)]}')
            return self.first_elements[int(k-1)]
        else:
            self.get_first_period()
            n_periods, last_k = divmod(int(k) - self.largest_even_i, self.__periods[self.n - 2])
            last_period = list(self.n_period_generator(n_periods))

            print(f'The {k}th element of the sequence U(2,{2*self.n + 1}) is: {last_period[last_k - 1]}')
        return last_period[last_k - 1]

    def get_first_elements(self):
        
        self.first_elements = problem.problem_167(2*self.n + 1, self.largest_even_i - 2)
    
    def get_first_period(self):
        
        n_hat = int(self.largest_even/2) # int avoids float outputs
        self.period = set(self.first_elements)
        
        while len(self.period) < self.__periods[self.n - 2] + self.largest_even_i: # minimum n = 2
            
            test_1 = 2*(n_hat-1) + 1 in self.period
            test_2 = 2*(n_hat-2*self.n-2) + 1 in self.period
            
            if test_1 ^ test_2:
                self.period.add(2*n_hat + 1)
            else:
                pass

            n_hat += 1
        self.period = self.period - set(self.first_elements)
        self.period = sorted(list(self.period))

    def n_period_generator(self, n_period):
        for number in self.period:
            yield number + n_period*self.__fund_diff[self.n-2]
    

def main():
    total_sum = sum([Ulam(n).get_item(5) for n in range(2, 10+1)])
    print(f'The result of the sum is: {total_sum}')

if __name__ == '__main__':
    sys.exit(main())