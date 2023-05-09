import time
import sys
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = time.perf_counter()
        self.string = s
        self.length = k
        self.global_length = len(self.string)
        sys.setrecursionlimit(10000)
        self.coincidence = 0
        self.the_most_high_value = 0
        self.time = 0
        print('string: ', self.string)
        print('longitude : ', self.length)
        print('Amount of letters: ', self.global_length)
        Solution.change_symbols(self)
        print('The most high value:', self.the_most_high_value)
        end = time.perf_counter()
        print(end - start)
        return self.the_most_high_value

    def change_symbols(self):
        for i in self.string:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                self.string = self.string.replace(i, '1')
        Solution.divide_letters(self)

    def detect_fragment(self):
        return self.string[(self.length + self.time) - self.length:self.length + self.time]

    def divide_letters(self):
        for i in Solution.detect_fragment(self):
            if i == '1':
                self.coincidence += 1
        print('coincidence: ', self.coincidence)
        Solution.update_numbers(self)

    def update_numbers(self):
        if self.coincidence >= self.the_most_high_value:
            self.the_most_high_value = self.coincidence
        self.coincidence = 0
        if self.global_length > self.length + self.time:
            self.time += 1
            Solution.divide_letters(self)
