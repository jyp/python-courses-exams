def cube_root(r, epsilon):
    x = 1.0
    x_prev = x+2*epsilon
    iteration = 0
    while abs(x_prev - x) > epsilon:
        print("Iteration", iteration, ":", x)
        x_prev = x
        x = (2 * x + r / (x ** 2)) / 3
        iteration += 1

