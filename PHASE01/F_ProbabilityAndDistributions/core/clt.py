import random


def demonstrate_clt(dist_fn, n_samples, n_averages):
    """
    Central Limit Theoram
    """
    averages = []

    for _ in range(n_averages):
        samples = [dist_fn() for _ in range(n_samples)]
        avg_samples = sum(samples)/len(samples)
        averages.append(avg_samples)
    return averages


if __name__ == "__main__":
    def dist_fn():
        """Simulation of a dice"""
        return random.randint(1, 6)
    
    print(f"Central Limit Theoram: {demonstrate_clt(
        dist_fn=dist_fn,
        n_samples=5,
        n_averages=100
        )}")