from stack import Stack
from tokenizer import tokenize

def apply_operator(op, operands):
    """
        Applies the operator to the list of operands. 

        Args:
        op (str): The operator (e.g., "+", "-", "*", "/").
        operands (list): The list of operands (integers).

        Returns:
        int: The result of applying the operator.

        Raises:
        ValueError: If the operator is unknown.
    """
    # TODO: Implement the apply_operator function
    ops = {'+':lambda x, y: x+y, '-':lambda x,y:x-y,'*':lambda x, y: x*y, '/':lambda x,y:x/y}
    # using python dictionaries and lambda function to map operators
    if op not in ops:
        raise ValueError("Wrong operator")
    return int(ops[op](operands[0], operands[1]))


def evaluate_lisp_expression(expression):
    """
        Evaluates a LISP-like arithmetic expression.

        Args:
        expression (str): The LISP expression to evaluate.

        Returns:
        int: The result of the evaluation.

        Raises:
        ValueError: If  the expression is invalid or contains unknown operators.
    """
    stack = Stack()
    tokens = tokenize(expression)
    # TODO: Implement the evaluate_lisp_expression(expression) function with proper error handling
    braces_stack = Stack()
    # to check the brases if the are proper or not
    ops = ( "+", "-", "*", "/")
    # just to see if the operations are fine
    for token in tokens:
        # looping through the tokens and checking each of them
        if token == '(':
            # adding the opening paranthesis
            braces_stack.push(token)
            stack.push(token)
            continue
        elif token==')':
            if not braces_stack.is_empty():
                braces_stack.pop()
                # checking the closing bracket
                stack.push(token)
                continue
            else:
                raise ValueError("Invalid expression with invalid paranthesis")
        else:
            if stack.peek() in ops and token in ops:
                # checking for multiple operations
                raise ValueError("Invalid expressions with improper operators")
            else:
                stack.push(token)
    if not braces_stack.is_empty():
        raise ValueError("Invalid paranthesis")
    # check for multile open braces
    store_stack = Stack()
    # stack to store the resultant values in case of a nested expression
    while not stack.is_empty():
        if stack.peek() == ')':
            stack.pop()
            continue
        else:
            operands = [None]*2
            v1 = stack.pop()
            v2 = stack.pop()
            # TO CHECK IF IT is an operator or a nested expression
            if v2 in ops:
                operands[1] = store_stack.pop()
                operands[0] = int(v1)
                op = v2
            else:
                operands[1] = int(v1) 
                operands[0] = int(v2)
                op = stack.pop()
            # applying the opration
            res = apply_operator(op, operands)
            if stack.peek()=='(':
                stack.pop()
                store_stack.push(res)
                if stack.is_empty():
                    break
            else:
                raise ValueError("Wrong paranthesis")
            # after the operation is done we again check what's after the op
            # a liitle unorthodox, but a crude way of doing it
            if stack.peek() == ')':
                stack.pop()
                if stack.is_empty():
                    break
            elif stack.peek() in ops:
                if not store_stack.is_empty():
                    operands[1] = int(store_stack.pop())
                    operands[0] = res
                    op = stack.pop()
                    res = apply_operator(op, operands)
                else:
                    raise ValueError("Invalid expression")
                if stack.peek()=='(':
                    stack.pop()
                    if stack.is_empty():
                        break
                else:
                    raise ValueError("Invalid expression")
            
    return res

