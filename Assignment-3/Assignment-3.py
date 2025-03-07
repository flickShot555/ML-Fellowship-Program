# Mean squared Error:
def mean_squared_error(actual, predicted):
    total_points = 0  # Counter for elements
    sum_of_squares = 0  # Sum of squared differences

    # Counting elements in both lists
    for _ in actual:
        total_points += 1

    # Ensure lists have the same length
    length_predicted = 0
    for _ in predicted:
        length_predicted += 1
    if total_points != length_predicted:
        raise ValueError("Both lists must have the same number of elements.")

    # Calculate sum of squared differences
    index = 0
    while index < total_points:
        difference = actual[index] - predicted[index]
        sum_of_squares += difference * difference
        index += 1

    return sum_of_squares / total_points  # Return MSE

# Root mean Squared error:
def root_mean_squared_error(actual, predicted):
    mse = mean_squared_error(actual, predicted)  # Compute MSE
    return mse ** 0.5  # Take square root

# Cosine Similarity
def cosine_similarity(a, b):
    length_a = 0  # Count elements in a
    length_b = 0  # Count elements in b

    for _ in a:
        length_a += 1
    for _ in b:
        length_b += 1

    if length_a != length_b:
        raise ValueError("Both lists must have the same number of elements.")

    dot_product = 0
    sum_a_squared = 0
    sum_b_squared = 0
    index = 0

    while index < length_a:
        dot_product += a[index] * b[index]  # Compute dot product
        sum_a_squared += a[index] * a[index]  # Sum of squares of a
        sum_b_squared += b[index] * b[index]  # Sum of squares of b
        index += 1

    magnitude_a = sum_a_squared ** 0.5  # sqrt(sum of squares of a)
    magnitude_b = sum_b_squared ** 0.5  # sqrt(sum of squares of b)

    if magnitude_a == 0 or magnitude_b == 0:
        return 0  # Avoid division by zero

    return dot_product / (magnitude_a * magnitude_b)  # Return cosine similarity

# Linear regression
def linear_regression(x, y):
    n = 0  # Number of data points
    sum_x = 0  # Sum of x values
    sum_y = 0  # Sum of y values
    sum_xy = 0  # Sum of (x * y)
    sum_x_squared = 0  # Sum of x^2

    # Count data points manually
    for _ in x:
        n += 1

    length_y = 0
    for _ in y:
        length_y += 1

    if n != length_y:
        raise ValueError("Both lists must have the same number of elements.")

    index = 0
    while index < n:
        sum_x += x[index]
        sum_y += y[index]
        sum_xy += x[index] * y[index]
        sum_x_squared += x[index] * x[index]
        index += 1

    # Compute slope (m)
    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = (n * sum_x_squared) - (sum_x * sum_x)
    if denominator == 0:
        raise ValueError("Cannot compute slope; possible division by zero.")
    m = numerator / denominator

    # Compute intercept (b)
    b = (sum_y - (m * sum_x)) / n

    return m, b  # Return slope and intercept

# Softmax function
def softmax(values):
    exponentials = []  # List for storing exponentials
    sum_of_exponentials = 0  # Sum of exponentials

    # Compute exponentials and their sum
    for val in values:
        exp_val = 2.718281828459045 ** val  # Using approximation for e^x
        exponentials.append(exp_val)
        sum_of_exponentials += exp_val

    # Compute probabilities
    softmax_result = []
    for exp_val in exponentials:
        softmax_result.append(exp_val / sum_of_exponentials)

    return softmax_result  # Return softmax probabilities
