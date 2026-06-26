from value import Value


def gradient_check(build_expr, x_val, h=1e-7):
    """
    Compare automatic differentiation against numerical differentiation.

    Computes the derivative of a function in two ways:
    1. Automatic differentiation using backpropagation.
    2. Numerical differentiation using the central difference
       approximation.

    A small difference between the two gradients indicates that the
    automatic differentiation implementation is likely correct.

    Args:
        build_expr: A function that accepts a Value object and returns
            a Value representing the computation graph.
        x_val: The input value at which the derivative is evaluated.
        h: Small perturbation used for the finite-difference
            approximation.

    Returns:
        A tuple containing:
            - autodiff_grad: Gradient computed by backpropagation.
            - numerical_grad: Gradient computed using finite
              differences.
            - diff: Absolute difference between the two gradients.
    """
    x = Value(x_val)
    y = build_expr(x)

    y.backward()
    autodiff_grad = x.grad

    y_plus = build_expr(
        Value(data=x_val + h)
        ).data
    y_minus = build_expr(
        Value(data=x_val - h)
        ).data

    numerical_grad = (y_plus - y_minus) / (2 * h)

    diff = autodiff_grad - numerical_grad
    per_diff = diff*100 # returns the changes in autodiff comapred to numerical gradient

    return autodiff_grad, numerical_grad, diff, per_diff


def complex_expr(x):
    """
    Example differentiable function used for gradient checking.

    Computes:
        tanh(x³ + 2x + 1)

    This expression combines polynomial arithmetic and a nonlinear
    activation, making it a useful test case for validating automatic
    differentiation.

    Args:
        x: A Value object.

    Returns:
        A Value representing the computed expression.
    """
    return (x ** 3 + x * 2 + 1).tanh()


ad, num, diff, per_diff = gradient_check(build_expr=complex_expr,x_val=0.5)

print(f"Autodiff: {ad}")
print(f"Numerical: {num}")
print(f"Difference: {diff}")
print(f"Percentage Difference: {per_diff:.4f}")
