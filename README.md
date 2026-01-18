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

