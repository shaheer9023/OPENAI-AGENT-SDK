from agents import Agent, Runner,AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled
set_tracing_disabled(True)
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from dotenv import load_dotenv
load_dotenv()
from tools import add, subtract, multiply, divide
from rich import print
from dynamic_instruction import instruction
from user_schema import User
import os

gemini_provider = AsyncOpenAI(
    api_key=os.getenv("gemini_api_key"),base_url=os.getenv("base_url")
)
gemini_model = OpenAIChatCompletionsModel(
    model=os.getenv("gemini_model"),openai_client=gemini_provider
    )

# # openAI Agent
math_agent = Agent(
    name="Math Agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    An agent that uses Gemini model for solving math problems.""",
    tools=[add, subtract, multiply, divide],
    handoff_description="This agent can handle math-related queries.",
    tool_use_behavior="stop_on_first_tool",
    model=gemini_model,
)

english_agent = Agent(
    name="English Agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    An agent that uses Gemini model for solving English language problems.""",
    handoff_description="This agent can handle English language queries.",
    model=gemini_model,
)




my_agent = Agent[User](
    name="Myself Agent",
    instructions=instruction,
    handoffs=[math_agent, english_agent],
    model=gemini_model
)





user1 = User(
    name="shaheer Ahmad",
    age=22,
    location="Pakistan"
)
while True:
    prompt = input("Enter your prompt: ")
    if prompt.lower() == "exit":
        break
    else:
        result = Runner.run_sync(
            my_agent,
            prompt,
            context=user1
        )
        print(f"{result.last_agent.name} is running......")
        print(result.final_output)
