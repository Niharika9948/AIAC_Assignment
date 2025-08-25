def factorial_with_prompt(n):
    
    if n < 0:
        msg = "Factorial is not defined for negative numbers."
        print(msg)
        return msg
    elif n == 0:
        print("0! = 1")
        return 1
    else:
        result = 1
        steps = []
        for i in range(n, 0, -1):
            result *= i
            steps.append(str(i))
        solution = f"{n}! = " + "*".join(steps) + f" = {result}"
        print(solution)
        return result

# Example usage:
factorial_with_prompt(5)
factorial_with_prompt(0)
factorial_with_prompt(-3)
