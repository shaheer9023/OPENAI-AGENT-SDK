from agents import Agent, Runner
from rich import print
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
class AgentOutput(BaseModel):
    final_output: str

# openAI Agent
openai_agent = Agent(
    name="OpenAI Agent",
    instructions="An agent that uses OpenAI model for various tasks.",
    output_type=AgentOutput,
)


prompt = input("Enter your prompt: ")

result = Runner.run_sync(
    starting_agent=openai_agent,
    input=prompt,
    

    )



print(f"[yellow]Agent Response: [/yellow]")
print(f"[cyan]{result.final_output}[/cyan]")
