import math

def taylor_approx(f, f_gradient, f_hessian, x0, h, order=2):
    """
    Formula:
        f(x + h) = f(x) + f'(x)*h + (1/2)*f''(x)*h^2 + (1/6)*f'''(x)*h^3 + ...
    """
    result = f(x0)

    if order>=1:
        result += f_gradient(x0) * h
        """
        For first order
            f(x + h) = f(x) + f'(x)*h
        """
    
    if order>=2:
        """
        For second order
            f(x + h) = f(x) + f'(x)*h + (1/2)*f''(x)*h^2 
        """
        result += 0.5 * f_hessian(x0) * h ** 2
    
    return result

x0 = 0.0
for h in [0.1, 0.5, 1.0, 2.0]:
    true_val = math.sin(h)
    t1 = taylor_approx(math.sin, math.cos, lambda x: -math.sin(x), x0, h, order=1)
    t2 = taylor_approx(math.sin, math.cos, lambda x: -math.sin(x), x0, h, order=2)
    print(f"h={h:.1f}  sin(h)={true_val:.4f}  order1={t1:.4f}  order2={t2:.4f}")

