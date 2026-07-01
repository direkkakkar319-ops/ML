import math

from probability_basics import factorial


def bernoulli_pmf(k, p):
    """
    Return the probability of outcome k (0 or 1) in a Bernoulli distribution.

    Formula:
        P(X = k) = p          if k = 1
                 = 1 - p      if k = 0
    
    Args:
        k (int): Outcome (0 = failure, 1 = success).
        p (float): Probability of success.

    Returns:
        float: Probability of the given outcome.
    """
    return p if k==1 else (1-p)


def categorical_pmf(k, probs):
    """
    Return the probability of category k from a categorical distribution.
    
    Formula:
        P(X = k) = probs[k]
    
    Args:
        k (int): Category index.
        probs (list[float]): Probabilities for each category.

    Returns:
        float: Probability of category k.
    """
    return probs[k]


def possion_pmf(k, lam):
    """
    Return the probability of observing exactly k events in a Poisson distribution.
        
    Formula:
        P(k) = [(λ ** k) * (e ** (-λ))] / k!
    
    Args:
        k (int): Number of events.
        lam (float): Average number of events (λ).

    Returns:
        float: Probability of observing exactly k events.
    """
    return (lam ** k) * math.exp(-lam) / factorial(k)
    #      [(λ ** k)  * (e ** (-λ))]   / k! 

print(f"Bernaulli PMF: {bernoulli_pmf(1, 0.8)}")

probs = [
    0.10,
    0.20,
    0.05,
    0.25,
    0.30,
    0.10
]
print(f"Categorical PMF: {categorical_pmf(4, probs=probs)}")

print(f"Possion PMF: {possion_pmf(2, 4)}")
