def tokenize(expression):
    """
        Tokenizes a LISP-like expression.

        Args:
        expression (str): The LISP expression to tokenize.
        Returns:
        list: A list of tokens.
    """
    tokens = []
    # TODO: Implement the tokenizer function
    braces_Stack = []
    for c in expression:
        if c !=" ":

            tokens.append(c)
    return tokens