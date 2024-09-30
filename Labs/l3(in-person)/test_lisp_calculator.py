from lisp_calculator import evaluate_lisp_expression

def run_tests(test_file):
    """
    Runs test cases from the specified file.

    Args:
        test_file (str): Path to the test cases file.
    """
    print(test_file)
    with open(test_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        expr, expected = line.strip().split(',')
        expected = int(expected) # Convert expected result to integer
        result = evaluate_lisp_expression(expr)
    assert result == expected, f"Test failed for expression {expr}. Expected {expected}, got {result}"

    print("All tests passed!")


if __name__ == "__main__":
    run_tests('test_cases.txt')
