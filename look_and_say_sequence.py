'''
A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is obtained by describing the previous term. An example is easier to understand:

Each consecutive value describes the prior value.

1      #
11     # one 1's
21     # two 1's
1211   # one 2, and one 1.
111221 # #one 1, one 2, and two 1's.


Your task is, return the nth term of this sequence.
'''
import time

def sequence(nth_term):
    result_seq = '1'
    for i in range(1, nth_term):
        seq = ''
        index = 0
        length = len(result_seq)
        while index < length:
            counter = 1
            k = index + 1
            while k < length and result_seq[index] == result_seq[k]:
                counter += 1
                k += 1
            seq += (str(counter) + result_seq[index])
            index = k
        result_seq = seq
        print(seq)
    return result_seq

start = time.time()
print("End Result: ", sequence(7))
print(time.time() - start)

