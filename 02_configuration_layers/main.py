from agents import Agent, Runner, RunConfig
from gemini_config import *
from rich import print 
# Gemini Agent
gemini_agent = Agent(
    name="Gemini Agent",
    instructions="An agent that uses Gemini model for various tasks.",
    model=gemini_model,
)
# openAI Agent
openai_agent = Agent(
    name="OpenAI Agent",
    instructions="An agent that uses OpenAI model for various tasks.",
    model=os.getenv("openai_model"),
)


prompt = input("Enter your prompt: ")

result = Runner.run_sync(
    starting_agent=gemini_agent,
    input=prompt,
    # run_config=RunConfig(
    #     model=os.getenv("openai_model"),

    )


print(f"[yellow]Agent Response: [/yellow]")
print(f"[cyan]{result.final_output}[/cyan]")
