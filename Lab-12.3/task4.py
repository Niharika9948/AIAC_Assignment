def f(x):
    return 2 * x**3 + 4 * x + 5

def grad_f(x):
    return 6 * x**2 + 4

def gradient_descent(start_x, learning_rate, max_iter, tol=1e-6):
    x = start_x
    for i in range(max_iter):
        grad = grad_f(x)
        x_new = x - learning_rate * grad
        if abs(x_new - x) < tol:
            break
        x = x_new
    print("The value of x where f(x) is minimum:", x)
    print("The minimum value of f(x):", f(x))
    return x

if __name__ == "_main_":
    try:
        start_x = float(input("Enter start value of x (e.g., 0): "))
        learning_rate = float(input("Enter learning rate (e.g., 0.01): "))
        max_iter = int(input("Enter maximum iterations (e.g., 1000): "))
        gradient_descent(start_x, learning_rate, max_iter)
    except Exception as e:
        print(f"Error: {e}")