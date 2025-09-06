from agents import RunContextWrapper,Agent
from user_schema import User


def instruction(ctx:RunContextWrapper,agent:Agent[User])->str:
    return f"user information is {ctx.context} you are a helpful assistant and use other tools and agents  if needed."
