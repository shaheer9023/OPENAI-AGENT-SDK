### 🔹 **OpenAI Agents SDK**

* **OpenAI Agents SDK** aik asaan aur lightweight tool hai jo AI agents bananay ke liye use hota hai.
* Yeh pehle experimental tool "Swarm" ka production-ready upgrade hai.

#### 🔧 **Basic Cheezen jo SDK provide karta hai:**

* **Agents** → LLMs (jaise GPT) jinhein aap instructions aur tools ke sath use kar saktay ho.
* **Handoffs** → Ek agent doosray agent ko specific task assign kar sakta hai.
* **Guardrails** → Agents ke input ko validate karne ke liye checks lagaye ja saktay hain.

---

### 🎯 **Faiday (Why use it?):**

* **Asaan aur chhoti API** → Use karna easy hai aur jaldi seekh jaata hai.
* **Customizable** → Default setup achi tarah kaam karta hai, lekin aap use customize bhi kar saktay ho.

---

## ⭐ **Important Features**

---

#### ✅ **1. Agent Loop**

**Explanation:** Agent apne aap tool ko call karta hai, result LLM ko deta hai, aur jab tak kaam mukammal nahi hota, tab tak repeat hota rehta hai.

**🧠 Real Life Example:**

Socho aap ek agent bana rahay ho jo **flight book karne** ka kaam karta hai.

* Pehle yeh check karega k user ka destination kya hai.
* Phir date poochayga.
* Phir sasti flights search karega.
* Jab tak sari info nahi milti, agent bar bar poochta rahayga aur tool se data leta rahega.

---

#### ✅ **2. Python-first**

**Explanation:** SDK Python ko priority deta hai, yani aapko sirf Python aani chahiye — koi extra syntax ya new language seekhne ki zarurat nahi.

**🧠 Real Life Example:**

Socho aapko ek AI app banana hai jo pehle **weather check** kare aur phir **recommendation de** ke kya pehnna chahiye.

* Aap `get_weather()` aur `suggest_clothes()` jaise Python functions bana lo.
* Bas un dono ko ek dusray se chain kar do — SDK automatically isay agentic flow bana dega.

---

#### ✅ **3. Handoffs**

**Explanation:** Ek agent doosray agent ko specific kaam assign kar deta hai.

**🧠 Real Life Example:**

Aapka ek "Main Assistant" agent hai jo har kaam nahi karta.

* Jab user kahe "Translate this text", to main agent ye kaam **Translate Agent** ko de deta hai.
* Jab user kahe "Summarize this article", to yeh kaam **Summarizer Agent** ko de deta hai.

Yani agents apas mein team ki tarah kaam kartay hain.

---

#### ✅ **4. Guardrails**

**Explanation:** Inputs validate hotay hain — agar kuch galat hua to kaam start hone se pehle hi ruk jata hai.

**🧠 Real Life Example:**

Aapka agent bank info process karta hai.

* Guardrail check karta hai ke **account number sirf digits hain** aur length 10 hai.
* Agar user `abc123` type kare, to agent kaam start hi nahi karega — error day dega.

Yeh system ko **secure aur reliable** banata hai.

---

#### ✅ **5. Function Tools**

**Explanation:** Aap kisi bhi Python function ko tool mein badal saktay ho, SDK khud uska input/output schema banata hai.

**🧠 Real Life Example:**

Aapka function `def calculate_bmi(weight, height)` hai.

* **BMI** = Body Mass Index
* SDK isay tool bana dega jo validate karega ke `weight` aur `height` sahi type ke hain.
* Agent ise use karke health advice de sakta hai.

---

#### ✅ **6. Tracing**

**Explanation:** Aap dekh saktay ho ke agent ne kya steps liye, konsa tool kab call hua, aur kaha pe koi error aya.

**🧠 Real Life Example:**

Socho user ne kaha: “Book a hotel in Paris.”

* Tracing dikhayega ke agent ne pehle city samjhi, phir hotel tool call kiya, phir available hotels return kiye.
* Agar kuch wrong hua, to trace log se foran pata chal jata hai ke kis step pe issue aya.

---

### ⚙️ **Installation:**

```
pip install openai-agents
```

---

### 👋 **Hello World Example:**

```python
from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)
```

✳️ Output:

```
# Code within the code,  
# Functions calling themselves,  
# Infinite loop's dance.
```

🗝️ **Note:** Run karne se pehle `OPENAI_API_KEY` set karna zaroori hai:

```bash
export OPENAI_API_KEY=sk-...
```

---
