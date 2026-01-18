# Agent Workflow with Object Oriented Design
You should design your agentic workflow based on the Object Oriented Design Principle of Python. This will give you flexibility to design the software in more modular, flexible and scalable for future expansion. Basic idea is not to modify existing code base while adding new features, different techstack under the application callflow.

Fundamental guidelines is provided by the SOLID principle.

You can refer the code inside OOD. Try to go though the codebase as per the sequence. 


<img width="1225" height="760" alt="image" src="https://github.com/user-attachments/assets/14435d64-c776-45a5-b750-129bec0f4610" />



# Let's Build A Simple Agent Using Langgraph
LangGraph is one of the more popular low-level orchestration frameworks for building agentic workflows among the developer community. It was built by the LangChain team, who hoped it would give builders better control by making the flow explicit.

It might feel overwhelming at first, but it gets easier once you understand the fundamentals—which is exactly what we’ll go through here by building a single-agent workflow that we can visualize and test in LangGraph Studio.

Essentially, with LangGraph, you’re writing code that can be visualized as a graph with nodes. You won’t be working in a visual programming system; instead, you code it manually and then visualize and debug it via LangGraph Studio (though that part is optional).

<img width="1456" height="668" alt="image" src="https://github.com/user-attachments/assets/d875d178-cdac-473b-b759-95e87a181006" />


### Some Important Aspect Of Agentic Design
#### Node, Graph
The graph is the overall framework for setting up your agent’s workflow. See it as the environment we need to execute our workflow. We always set up the graph first.

After defining the graph, we set up our nodes—these are the core functionalities or operations. Nodes are where everything happens. In an agent workflow, a node could do anything from calling an LLM to invoking a tool (like a search function or an API), or performing some computation.

The edges are the connections between nodes. They tell the graph which node to go to next. Edges can be static (always go from A to B) or conditional (branch based on something in the state). So essentially, nodes do the work, edges decide what happens next.

<img width="1456" height="442" alt="image" src="https://github.com/user-attachments/assets/29969363-f48e-4156-9cec-6780a01c001d" />


#### State

State is the current memory or context of the workflow, where we hold all the data that flows between nodes.

You can think of state as short-term memory—it sticks around during the current run or conversation. It often holds things like conversation history between LLM calls or variables we need in multiple places.

<img width="1456" height="511" alt="image" src="https://github.com/user-attachments/assets/bd1e3287-0923-4c0f-b591-9e9409ed499a" />


#### Tool
LLM doesn’t know what’s in the database. Or in your files. Or today’s headlines. And that’s okay — because you can let it fetch that stuff.

<img width="1438" height="568" alt="image" src="https://github.com/user-attachments/assets/d9e3c814-e079-40bf-8088-28691e3ab227" />

#### Adding Edges
Now we can start connecting the nodes, and need to set the first entry point for the workflow:

<img width="1456" height="596" alt="image" src="https://github.com/user-attachments/assets/4d18ad2d-a366-4a1a-966a-7f8ed0bb684a" />

#### Compiling the Workflow

The last thing we need to do is compile the workflow.

Please refer the Langchain-Callflow.py for implementation detail.

#### Testing the workflow

To test this workflow, open up LangGraph Studio, connect to LangSmith (free to create an account), turn on Docker Desktop (make sure it's the latest version), and then open the langgraph_example project.

<img width="1456" height="919" alt="image" src="https://github.com/user-attachments/assets/3b0865a2-1ab4-4041-8cbf-96b9290821ce" />

Once it’s loaded, you’ll be able to add a human message and submit it to see what happens.

<img width="1456" height="914" alt="image" src="https://github.com/user-attachments/assets/f73304b7-b01b-40ad-8a4d-d0b53c72af1f" />

It only has those two mock tools available, so it won’t be very useful in practical scenario, however it will be useful for understanding the call sequence.

<img width="1456" height="871" alt="image" src="https://github.com/user-attachments/assets/56e4aed9-2f9c-4771-949f-2d6ce08697f2" />


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

## 5. Multi-Agent: Get a Team of Agent Working Together To Accomplish a Complex Task

Why rely on one agent when you can have a whole team working together?

Multi-Agent setups assign different roles to different agents, each handling a piece of the puzzle. They collaborate — sometimes even argue — to come up with better solutions.

Typical setup:

Researcher gathers info
Planner outline steps
Coder writes the code
Reviewer double-check everything
PM: keeps it all moving
It doesn’t have to be fancy. Even basic coordination works:

Give each agent a name and job.
Let them message each other through a controller.
Watch as they iterate, critique, and refine.

The magic happens when they disagree. That’s when you get sharper insights and deeper thinking.

![0_yWrvDIxeOiYMWNgj](https://github.com/user-attachments/assets/9f40cdc4-7afb-40cf-bd4c-f46da9f41661)

### Simple Starting Point
Let’s say you’re building a research assistant. Here’s a no-nonsense setup that puts these patterns into play:

#### 1. Start with Planning
Prompt: “Break this research task into clear steps before answering.”
Example: “1. Define keywords, 2. Search recent papers, 3. Summarize findings.”

#### 2. Use Tool Use
Hook it up to a search API or a vector DB so it’s pulling real facts — not making stuff up.

#### 3. Add Reflection
After each answer, prompt: “What’s missing? What could be clearer?” Then regenerate.

#### 4. Wrap it in ReAct
Let the agent think between steps. “Results look shallow — retrying with new terms.” Then act again.

#### 5. Expand to Multi-Agent (optional)
One agent writes. Another critiques.
They talk. They argue. The output gets better.




