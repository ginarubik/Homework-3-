#QUESTION 2: Number In Sequence

# Non-recursive (mathematical) Solution: 


def num_in_seq(n): return 8*n-(n-1)

# Recursive Solution:

def num_in_seq(n):
    if n == 0:
        return 1
    else:
        return 7 + num_in_seq(n-1)

print(num_in_seq(10))

# Improved Recursive:

def num_in_seq(n):
    return 1 if n == 0 else 7 + num_in_seq(n-1)


#Note: The recursive solution exhausts the memory if a very big number is used. The non-recursive mathematical solution gives a fast result on the computer.