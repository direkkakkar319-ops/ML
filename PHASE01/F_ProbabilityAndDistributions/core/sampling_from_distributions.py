import random
import math


def sample_bernaulli(p, n=1):
    """
    Bernaulli Sampling
    """
    return [1 if random.random()<p else 0 for _ in range(n)]

def sample_categorical(probs, n=1):
    """
    Categorical Sampling
    """
    cumulative = []
    total = 0
    samples = []

    for p in probs:
        total += p
        cumulative.append(total)

    for _ in range(n):
        r = random.random()
        for i, c in enumerate(cumulative):
            if  r<= c:
                samples.append(i)
                break
    return samples

def samples_normal_box_muller(mu, sigma, n=1):
    """
    Normal Sampling (Box-Muller)
    Formula:
        z=math.sqrt(-2*log(u1)*cos(2*π*u2))    
    """
    samples = []
    
    for _ in range(n):
        u1 = random.random()
        u2 = random.random()
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2) # box-muller transform
        samples.append(mu+sigma*z)
    return samples

if __name__ == "__main__":
    print(f"Bernaulli Sampling: {sample_bernaulli(p=0.5, n=5)}")

    print(f"Categorical Sampling: {sample_categorical(probs=[0.2,0.5,0.3], n=10)}")

    print(f"Normal Sampling: {samples_normal_box_muller(mu=100, sigma=15, n=5)}")
