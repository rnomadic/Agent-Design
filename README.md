# Agent Workflow with Object Oriented Design
Try to go though the codebase as per the sequence. This design is based out of Python Object Orient Design, SOLID Principle.

Below is the snapshot of SOLID is all about.

<img width="1225" height="760" alt="image" src="https://github.com/user-attachments/assets/14435d64-c776-45a5-b750-129bec0f4610" />



# Agentic AI Patterns 
The intention of agentic AI patterns are essentially design techniques that give LLMs a bit more clarity on what is expectected outcome. They let the model plan, reflect, use tools, even work with other agents.


## 1. Reflection: Teach Your Agent to Check Its Own Work
Ever asked ChatGPT a question, read the answer, and thought, “This sounds good… but something’s off”? <br>
<br>
That’s where Reflection comes in. It’s a simple trick: have the model take a second look at its own output before finalizing it. <br>

The basic flow: <br>
<br>
Ask the question.<br>
Have the model answer.<br>
Then prompt it again: “Was that complete? Anything missing? How could it be better?”<br>
Let it revise itself.<br>

You’re not stacking models or adding complexity. You’re just making it double-check its work. And honestly, that alone cuts down on a ton of sloppy mistakes; especially for code, summaries, or anything detail-heavy. <br>
<br>
Think of it like giving your model a pause button and a mirror. <br> <br>

![0_BnHljDx_9gV_MiBD](https://github.com/user-attachments/assets/8c8560c0-9ca3-46b7-9393-4fe47fbe8e58)

<br>

## 2. Tool Use: You can't Expect the Model to Know Everything
LLM doesn’t know what’s in the database. Or in your files. Or today’s headlines. And that’s okay — because you can let it fetch that stuff.

The Tool Use pattern connects the model to real-world tools. Instead of hallucinating, it can query a vector DB, run code in a REPL, or call external APIs like Stripe, WolframAlpha, or your internal endpoints.

This setup does require a bit of plumbing: function-calling, routing, maybe something like LangChain or Semantic Kernel, but it pays off. Your agent stops guessing and starts pulling real data.

People assume LLMs should be smart out of the box. They’re not. But they get a lot smarter when they’re allowed to reach for the right tools.

![0_nHCaGi1FCWarqB7T](https://github.com/user-attachments/assets/b688ec11-ff14-489c-9022-1fe0a41f3794)

## 3. ReAct: Model Can Think While It Is Doing Some Acts

Reflection’s good. Tools are good. But when you let your agent think and act in loops, it gets even better.

That’s what the ReAct pattern is all about: Reasoning + Acting.

Instead of answering everything in one go, the model reasons step-by-step and adjusts its actions as it learns more.

Example:

Goal: “Find the user’s recent invoices.”
Step 1: “Query payments database.”
Step 2: “Hmm, results are outdated. Better ask the user to confirm.”
Step 3: Adjust query, repeat.
It’s not just responding — it’s navigating.

To make ReAct work, you’ll need three things:

Tools (for taking action)
Memory (for keeping context)
A reasoning loop (to track progress)
ReAct makes your agents flexible. Instead of sticking to a rigid script, they think through each step, adapt in real-time, and course-correct as new information comes in.

If you want to build anything beyond a quick one-off answer, this is the pattern you need.

![0_o0dRsUIiUr8RPLIa](https://github.com/user-attachments/assets/46486fed-c833-434f-970e-7398dde576b8)

## 4. Planning: Can You Teach Your Agent to Think Ahead

LLMs are pretty good at quick answers. But for anything involving multiple steps? They fall flat.

Planning helps with that.

Instead of answering everything in one shot, the model breaks the goal into smaller, more manageable tasks.

Let’s say someone asks, “Help me launch a product.” The agent might respond with:

Define the audience
Design a landing page
Set up email campaigns
Draft announcement copy
Then it tackles each part, one step at a time.

You can bake this into your prompt or have the model come up with the plan itself. Bonus points if you store the plan somewhere so the agent can pick up where it left off later.

Planning turns your agent from a reactive helper into a proactive one.

This is the pattern to use for workflows and any task that needs multiple steps.

![0_RGsbSVLCPhWmdpSK](https://github.com/user-attachments/assets/bdc834d2-c0c4-463e-9aa6-971e735a7430)




