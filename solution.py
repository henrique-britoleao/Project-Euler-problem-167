from sequence_generators import ulam_generator
import sys

class Ulam:
    '''
    Class that solves Problem 167 from Project Euler

    Attributes
    ----------
    n: int
        Number with wich to build the Ulam sequnce U(2, 2*n + 1)
    __periods: list
        Periodicity of the sequence depending on n
    __fun_diff: list
        Fundamental difference of items in sequence depending on n
    __largest_even: int
        Largest even number in the sequence
    __largest_even_i: int
        Index of the largest even number

    Parameters
    ----------
    n: int
        Number with wich to build the Ulam sequnce U(2, 2*n + 1)
    '''
    def __init__(self, n):
        self.n = n 
        self.__periods = [32, 26, 444, 1628, 5906, 80, 126960, 380882, 2097152]
        self.__fund_diff = [126, 126, 1778, 6510, 23622, 510, 507842, 1523526,
                            8388606]
        self.__largest_even = 4*n + 4
        self.__largest_even_i = int((2*n + 8)/2)
    
    def get_item(self, k):
        '''Returns the k-th item from the Ulam sequence.'''
        self._build_first_elements()
        
        if k < self.__largest_even: # no need to build period
            print(f"""The {k}th element of the sequence U(2,{2*self.n + 1}) is:\
                      {self.first_elements[int(k-1)]}""")
            
            return self.first_elements[int(k-1)]
        
        else:
            self._build_first_period() 
            n_periods, last_k = divmod(
                int(k) - self.__largest_even_i, self.__periods[self.n - 2]
            ) # subtract largest_even_i to get number of periods needed
            last_period = list(self._n_period_generator(n_periods)) 

            print(f"""The {k}th element of the sequence U(2,{2*self.n + 1}) is: 
                      {last_period[last_k - 1]}""")
            
            return last_period[last_k - 1]

    def _build_first_elements(self):
        '''Builds first elements auxiliary sequence'''
        self.first_elements = ulam_generator(2*self.n+1, self.__largest_even_i-2)
    
    def _build_first_period(self):
        '''Builds period auxiliary sequence'''
        n_hat = int(self.__largest_even/2) # int avoids float outputs
        self.period = set(self.first_elements) # improve search time
        
        while len(self.period) < self.__periods[self.n - 2] + self.__largest_even_i: # minimum n = 2
            
            test_1 = 2*(n_hat-1) + 1 in self.period
            test_2 = 2*(n_hat-2*self.n-2) + 1 in self.period
            
            if test_1 ^ test_2:
                self.period.add(2*n_hat + 1)
            else:
                pass

            n_hat += 1

        self.period = self.period - set(self.first_elements)
        self.period = sorted(list(self.period))

    def _n_period_generator(self, n_period):
        '''Generates numbers in the n-th occurence of the period'''
        for number in self.period:
            yield number + n_period*self.__fund_diff[self.n-2]
    

def main():
    total_sum = sum([Ulam(n).get_item(1e11) for n in range(2, 10+1)])
    print(f'The result of the sum is: {total_sum}')

if __name__ == '__main__':
    sys.exit(main())