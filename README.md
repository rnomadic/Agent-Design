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

![0_BnHljDx_9gV_MiBD](https://github.com/user-attachments/assets/8c8560c0-9ca3-46b7-9393-4fe47fbe8e58)


