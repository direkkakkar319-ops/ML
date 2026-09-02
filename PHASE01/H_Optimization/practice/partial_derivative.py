def partial_derivative_x(f, x, y, h=1e-4):
    return (f([x + h, y]) - f([x - h, y])) / (2 * h)


def partial_derivative_y(f, x, y, h=1e-4):
    return (f([x, y + h]) - f([x, y - h])) / (2 * h)


def partial_derivative(f, point: list, h=1e-4):
    x, y = point
    df_dx = partial_derivative_x(f=f, x=x, y=y)
    df_dy = partial_derivative_y(f=f, x=x, y=y)
    return [df_dx, df_dy]


def make_grad_func(f, h=1e-4):
    """Binds f into partial_derivative, returning a grad_func(point) -> [df_dx, df_dy]."""

    def grad_func(point):
        return partial_derivative(f, point, h=h)

    return grad_func
