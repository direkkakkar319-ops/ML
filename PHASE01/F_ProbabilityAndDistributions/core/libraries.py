import numpy as np 
from scipy import stats
from scipy.special import softmax, log_softmax


"""
normal distribution
    loc--> mean=0
    scale-->standardDeviation=1
Random samples
    size-->number of random numbers=1000
"""
normal = stats.norm(loc=0, scale=1)
samples = normal.rvs(size=10000)

print(f"Mean: {np.mean(samples):.4f}, Std: {np.std(samples):.4f}")
print(f"P(X < 1.96) = {normal.cdf(1.96):.4f}") #Cumulative Distribution Function{CDF}

"""
Creating logits-->Raw scores
softmax-->Logits to actual Probabilities
log_softmax-->returns the log of probabilities
    `log_softmax` combines softmax and log for numerical stability.
    PyTorch uses this internally for cross-entropy loss.
"""
logits = np.array([2.0,1.0,0.1])
probs = softmax(logits)
log_probs = log_softmax(logits)

print(f"Softmax: {probs}")
print(f"Log_Softmax: {log_probs}")
