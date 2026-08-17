"""
Question:
    Multiple tests. A patient tests positive twice on independent
    tests (both 99% accurate, disease prevalence 1 in 10,000).

    What is P(sick) after both tests? Use the posterior
    from the first test as the prior for the second ?
"""

import sys

sys.path.append(r"E:\ML\PHASE01\G_BayesTheoramAndStatisticalThinking\core")
from bayes_function import bayes

prior = 1 / 10000
likelihood = 99 / 100
false_positive = 0.01

posterori_01 = bayes(
    prior=prior, likelihood=likelihood, false_positive_rate=false_positive
)
print(f"Posterior for first case: {posterori_01}")

prior = posterori_01
posterori_02 = bayes(
    prior=prior, likelihood=likelihood, false_positive_rate=false_positive
)
print(f"Posterior for second case; {posterori_02}")
