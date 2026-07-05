import math 
import matplotlib.pyplot as plt


def uniform_pdf(x, a, b):
    """
    Compute the Probability Density Function (PDF)
    of a Uniform distribution.

    Formula:
                  1
        f(x) = --------   for a <= x <= b
                (b - a)
             = 0          otherwise

    Args:
        x (float): Value at which to evaluate the PDF.
        a (float): Lower bound of the distribution.
        b (float): Upper bound of the distribution.

    Returns:
        float: Probability density at x.
    """
    if a<=x<=b:
        return 1.0/(b-a)
    return 0.0


def normal_pdf(x, mu, sigma): #Computes bellcurve -> CLT
    """
    Compute the Probability Density Function (PDF)
    of a Normal (Gaussian) distribution.

    Formula:
                           1
        f(x) = -------------------------- * exp(-0.5 * ((x - μ) / σ)^2)
                σ * sqrt(2π)

    Equivalent mathematical form:
                        1
        f(x) = ----------------- * e^(-(x-μ)^2 / (2σ^2))
                σ * √(2π)

    Args:
        x (float): Value at which to evaluate the PDF.
        mu (float): Mean (μ) of the distribution.
        sigma (float): Standard deviation (σ) of the distribution.

    Returns:
        float: Probability density at x.
    """
    coeff = 1.0 / (sigma * math.sqrt(2 * math.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coeff * math.exp(exponent)


if __name__ == "__main__":
    print(f"Uniform PDF: {uniform_pdf(x = 4, a = 0, b = 10):.4f}")
    print(f"Normal PDF: {normal_pdf(x=14, mu=10, sigma=2):.4f}")

    x_u = [i/10 for i in range(-20, 121)]   # -2 to 12
    y_u = [uniform_pdf(i, 0, 10) for i in x_u]

    plt.plot(x_u, y_u)
    plt.title("Uniform Distribution PDF")
    plt.xlabel("x")
    plt.ylabel("Density")
    plt.grid(True)
    plt.show()

    x_n = [i/10 for i in range(-50, 51)]   # -5 to 5
    y_n = [normal_pdf(i, 0, 1) for i in x_n]

    plt.plot(x_n, y_n)
    plt.title("Normal Distribution PDF")
    plt.xlabel("x")
    plt.ylabel("Density")
    plt.grid(True)
    plt.show()
