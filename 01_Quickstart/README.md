# **Quickstart**

### **Create a project and virtual environment**

Ye sirf aik martaba karna hota hai (jab naya project shuru kar rahe hon):

```bash
mkdir my_project      # naya project folder bnao
cd my_project         # us folder me chalay jao
python -m venv .venv  # virtual environment bnao
```

---

### **Activate the virtual environment**

Har dafa jab terminal dubara kholain to virtual environment ko activate karna zaroori hota hai:

```bash
source .venv/bin/activate  # virtual environment activate karo
```

---

### **Install the Agents SDK**

```bash
pip install openai-agents  # ya `uv add openai-agents` use kar saktay ho
```

---

### **Set an OpenAI API key**

Agar key nahi hai to OpenAI ki website se API key bana lo.

```bash
export OPENAI_API_KEY=sk-...  # apni OpenAI API key yahan paste karo
```

---

### **Create your first agent**

Agents instructions, name aur optional config ke sath banaye jatay hain:

```python
from agents import Agent

agent = Agent(
    name="Math Tutor",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)
```

---

### **Add a few more agents**

Aik se zyada agents isi tarah define kiye jatay hain. `handoff_descriptions` agent ko identify karne me madad detay hain:

```python
from agents import Agent

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",  # ye bata raha hai k ye agent history ka expert hai
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",  # ye bata raha hai k ye agent math ka expert hai
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)
```

---

### **Define your handoffs**

Har agent k paas aik handoff list hoti hai jahan se wo decide karta hai ke next kisko route karna hai:

```python
triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",  # user ka sawal kis subject ka hai ye decide karta hai
    handoffs=[history_tutor_agent, math_tutor_agent]
)
```

---

### **Run the agent orchestration**

Yahan check karte hain ke workflow theek se kaam kar raha hai ya nahi, aur triage agent sahi specialist agent choose karta hai ya nahi:

```python
from agents import Runner

async def main():
    result = await Runner.run(triage_agent, "What is the capital of France?")  # test question
    print(result.final_output)
```

---

### **Add a guardrail**

Guardrail ka matlab hota hai ek extra check lagana jo input ya output pe kaam karta hai.

```python
from agents import GuardrailFunctionOutput, Agent, Runner
from pydantic import BaseModel

class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str  # yahan bataya gaya hai ke input homework hai ya nahi aur reasoning bhi di gayi hai

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
)

async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,  # agar input homework nahi hai to tripwire activate hoga
    )
```

---

### **Put it all together**

Ab sab kuch aik sath combine karte hain — agents, guardrails aur handoffs:

```python
from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner
from pydantic import BaseModel
import asyncio

# Ye class batayegi ke input homework related hai ya nahi
class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

# Guardrail agent jo homework check karega
guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
)

# Math tutor agent
math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

# History tutor agent
history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

# Guardrail function
async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )

# Triage agent jo handoff aur guardrail dono handle karta hai
triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),
    ],
)

# Main function jo test questions bhejta hai aur output print karta hai
async def main():
    result = await Runner.run(triage_agent, "who was the first president of the united states?")
    print(result.final_output)

    result = await Runner.run(triage_agent, "what is life")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())  # program start hota hai yahan se
```

---
