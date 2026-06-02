# Exercise: Execute tool-augmented Agent
### In this hands-on exercise, the focus will be on building an AI agent that can utilize various tools to enhance its functionality. This exercise will provide an opportunity to apply skills learned in previous concepts, such as understanding how to create and manage an agent that can intelligently decide when to use its available tools. By the end of this exercise, the agent will be capable of answering programming questions, executing code snippets, looking up documentation, performing calculations, and searching through codebases.

## Prerequisites
- Python programming language
- Libraries: typing, dotenv, json

## Objectives:
### By the end of this exercise, learners will be able to:
- Create an AI agent that can process user messages and utilize tools effectively
- Implement a calculator tool and a data analysis tool within the agent
- Test the agent's functionality with various scenarios to ensure it operates as expected

## Steps:
1. **Set Up the Workspace**
   - Open the classroom workspace provided for this exercise.
   - Ensure that all necessary libraries are installed and available in the environment.

2. Import Required Libraries
### At the beginning of your code, import the necessary libraries:

```python
from typing import List, Dict, Any
from dotenv import load_dotenv
from copy import deepcopy
import json
from lib.messages import UserMessage, SystemMessage, ToolMessage
from lib.tooling import tool
from lib.llm import LLM

```

1. **Define the Agent Class**
- Create a class named Agent that will handle user interactions and tool usage.
- Implement the __init__ method to initialize the agent with a role, instructions, model, temperature, and tools.
- Implement the invoke method to process user messages and return responses.

2. Implement Tool Functionality
### Create a calculator tool using the @tool decorator:
```python
@tool
def calculate(expression: str) -> float:
return eval(expression)
```
```python
- Create a data analysis tool to retrieve game statistics:
```
```python
@tool
def get_games(num_games:int=1, top:bool=True) -> str:
# Implementation details
```

1. Test the Agent
### Instantiate the agent with the role of "Coding Assistant" and test it with a simple query:
```python
agent = Agent(role="Coding Assistant")
response = agent.invoke("What is Python? Be concise")
print(response)
```
```python
- Test the calculator tool by creating an agent with the calculator tool and executing a calculation:
```

```python
math_agent = Agent(role="Math Assistant", tools=[calculate])
response = math_agent.invoke("What is 23 * 45?")
print(response)
```
```python
- Test the data analysis tool by creating an agent with the data analysis tool and querying game statistics:
```

```python
data_analyst_agent = Agent(role="Game Stats Assistant", tools=[get_games])
response = data_analyst_agent.invoke("What's the best game in the dataset?")
print(response)
```

1. Explore Multiple Tool Usage
### Test the agent's ability to handle multiple tool calls by asking complex questions that require using both tools:
```python
response = data_analyst_agent.invoke("If I multiply 3 by 5, what do I get? Then later add 7")
print(response)
```