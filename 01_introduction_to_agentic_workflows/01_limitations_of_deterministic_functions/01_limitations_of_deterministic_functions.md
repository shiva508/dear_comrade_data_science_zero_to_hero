# Demo: The Limitations of Deterministic Functions
## The Limitations of Deterministic Functions
###  In traditional programming, a deterministic function is one that, given a particular input, will always produce the same output. These functions operate on a predefined set of rules, often implemented through conditional logic such as if-else statements.
### Because it is deterministic, its output is defined by this logic.
- The function takes in the query, reads the prompt, and generates the output.
- It's very deterministic; you have to define each one of the cases for that input.
- If the function receives a query it hasn't been programmed for, it can only reply back with, "I cannot respond to that query; I don't have any information."

## The Rise of LLM-Powered Agents
### The functions that have LLMs are what we now call agents. An agent, in the context of modern AI, is a system that can perceive its environment, make decisions, and take actions to achieve specific goals. The key difference from a simple deterministic function is that an agent possesses a degree of autonomy and adaptability.
### The OpenAI LLM-powered function, on the other hand, is very different. Here, it takes in a query just as before, but instead of having to define each one of the cases, it returns the output from the OpenAI LLM. So it's very open what it's using to generate the output; it's actually the knowledge contained in the LLM itself. This approach introduces a new level of flexibility. An LLM-powered agent can respond to a wide range of queries, including those it has never seen before, replying back with a joke or providing other new and generative content.
### This function can handle the joke request because it leverages the vast, generative knowledge of the LLM. However, if we wanted an LLM function to provide real-time weather updates, we would have to make this an actual agent that has a tool or a means to access real-time data information. That's when we're going to start using them in agentic workflows.
Introduction to Agentic Workflows