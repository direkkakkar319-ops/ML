import math


def expected_value(values, probas):
    return sum(v*p for v,p in zip(values, probas))


def variance(values, probas):
    mu = expected_value(values=values, probas=probas)
    return sum(p * (v-mu) ** 2 for v,p in zip(values, probas))


def standard_deviation(variance):
    return math.sqrt(variance)


if __name__ == "__main__":
    die_values = [1, 2, 3, 4, 5, 6]
    die_probas = [1/6] * 6
    
    mu = expected_value(values=die_values, probas=die_probas)
    var = variance(values=die_values, probas=die_probas)

    print(f"Die: E[X] = {mu:.4f}, Var(X) = {var:.4f}, SD = {standard_deviation(variance=var):.4f}")