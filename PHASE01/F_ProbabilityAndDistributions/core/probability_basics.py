import math
import random

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

def combinations(n ,k):
    return factorial(n)//(factorial(k)*factorial(n-k))

def conditional_probability(p_a_and_b, p_b):
    return p_a_and_b/p_b

if __name__ == "__main__":
    p_king_given_face = conditional_probability(4/52, 12/52)
    print(f"P(King | Face card) = {p_king_given_face:.4f}")