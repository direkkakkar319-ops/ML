"""
Question:
    Write a function that takes a list of log probabilities and
    returns the most likely sequence, the total log probability,
    and the equivalent raw probability.
    Test it with a sentence of 50 words where each word has
    probability 0.01.
"""
import math 


def log_list(words, log_probs):
    """
    Use case:
    In NLP, "most likely sequence" usually means choosing the
    highest-probability word at each position.
    
    Example:
        >>> candidates = [
        ...     {"The": -0.1, "A": -2.3},
        ...     {"cat": -0.2, "dog": -1.5},
        ... ]
    """
    total_log_probs = sum(log_probs)
    raw_log_probs = math.exp(total_log_probs)
    
    return words, total_log_probs, raw_log_probs

words = [
    "The", "quick", "brown", "fox", "jumps",
    "over", "the", "lazy", "dog", "while",
    "birds", "sing", "softly", "near", "the",
    "river", "on", "a", "bright", "morning",
    "with", "gentle", "winds", "blowing", "through",
    "green", "trees", "and", "colorful", "flowers",
    "creating", "a", "peaceful", "scene", "for",
    "everyone", "to", "enjoy", "during", "their",
    "pleasant", "walk", "in", "the", "beautiful",
    "park", "today", "together", "happily", "always"
]
log_probs = [math.log(0.01)] * 50

sequence, total_log_probs, raw_log_probs = log_list(
    words=words,
    log_probs=log_probs
    )

print(sequence)
print(total_log_probs)
print(raw_log_probs)
