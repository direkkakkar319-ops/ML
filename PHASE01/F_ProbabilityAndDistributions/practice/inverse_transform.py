from scipy import stats
import numpy as np
import matplotlib.pyplot as plt 

def inver_transform(lambda_=1.0, n_samples=1000):
    """
    Question:
        Implement inverse transform sampling for the exponential distribution.
        Verify by sampling 10,000 values and comparing the histogram to the true PDF.

    Practical use case:
        The exponential distribution models waiting times between random events.
        
        Examples:
        Time until the next customer arrives.
        Time until a machine fails.
        Time between radioactive decays.
        Time until the next phone call reaches a call center.
    """
    # Inverse Transform samples
    u = np.random.rand(n_samples) #uniform random numbers between (0,1)
    samples = -np.log(1-u)/lambda_

    # True PDF from SciPy
    x = np.linspace(0, samples.max(), 500)
    pdf = stats.expon(scale=1/lambda_).pdf(x)

    plt.hist(samples, bins=50, density=True, alpha=0.6, label="Inverse Transform Samples")
    plt.plot(x, pdf, "r", lw=2, label="True PDF (SciPy)")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("Density")
    plt.title("Exponential Distribution: Inverse Transform Sampling")
    plt.show()

if __name__=="__main__":
    inver_transform(lambda_=1.0, n_samples=10000)