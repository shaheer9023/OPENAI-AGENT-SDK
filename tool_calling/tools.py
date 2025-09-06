from agents import function_tool,RunContextWrapper

def _format_result(operation: str, a: int, b: int, result) -> str:
    border = "═" * 40
    return (
        f"\n╔{border}╗\n"
        f"║   🎯 {operation} Result   🎯\n"
        f"╠{border}╣\n"
        f"║   {a} {operation} {b} = {result}\n"
        f"╚{border}╝\n"
    )

@function_tool
def add(a: int, b: int) -> str:
    """Adds two integers.
    Args:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        str: Beautifully formatted sum of a and b.
    """
    print("✨ Addition tool called ✨")
    result = a + b
    return _format_result("+", a, b, result)

@function_tool
def subtract(a: int, b: int) -> str:
    """Subtracts the second integer from the first.
    Args:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        str: Beautifully formatted difference of a and b.
    """
    print("✨ Subtraction tool called ✨")
    result = a - b
    return _format_result("-", a, b, result)

@function_tool
def multiply(a: int, b: int) -> str:
    """Multiplies two integers.
    Args:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        str: Beautifully formatted product of a and b.
    """
    print("✨ Multiplication tool called ✨")
    result = a * b
    return _format_result("×", a, b, result)

@function_tool
def divide(a: int, b: int) -> str:
    """Divides the first integer by the second. Raises an error if the second integer is zero.
    Args:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        str: Beautifully formatted quotient of a and b.
    """
    print("✨ Division tool called ✨")
    if b == 0:
        raise ValueError("🚫 Cannot divide by zero.")
    result = round(a / b, 4)
    return _format_result("÷", a, b, result)




import requests
@function_tool
def userdata()->list:
    """Fetches user data from a public API and return list"""
    print("✨ User data tool called ✨")
    result = requests.get("https://jsonplaceholder.typicode.com/users")
    return (result.json())