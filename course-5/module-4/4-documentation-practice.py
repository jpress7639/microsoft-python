def build_prompt(function_name, description, params, returns):
    """Build a structured prompt string for a generative AI documentation tool.

    Args:
        function_name (str): Name of the Python function.
        description (str): Short description of the function behavior.
        params (dict): Mapping of parameter names to their descriptions.
        returns (str): Description of the return value.

    Returns:
        str: A multi-line prompt string.
    """
    # TODO: Implement according to the specification in the instructions.
    return f"{function_name} is a function \nthat {description}\nwith {params} \nand returns {returns}"

def evaluate_docstring(docstring, required_keywords):
    """Evaluate an AI-generated docstring for keyword coverage.

    Args:
        docstring (str): The generated docstring text.
        required_keywords (list): Keywords that should appear in the docstring.

    Returns:
        dict: A dictionary with keys 'missing' (list of keywords not found)
              and 'coverage' (float between 0.0 and 1.0).
    """
    # TODO: Implement according to the specification in the instructions.
    raise NotImplementedError("evaluate_docstring is not implemented yet")
