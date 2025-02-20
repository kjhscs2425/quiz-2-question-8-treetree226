"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t,, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""

# YOUR CODE HERE

one= "ctb"
midd = "ao"
last1 = "ptn"

for first in one:
    for mid in midd:
        for last in last1:
            word = first + mid + last
            print(word) 


