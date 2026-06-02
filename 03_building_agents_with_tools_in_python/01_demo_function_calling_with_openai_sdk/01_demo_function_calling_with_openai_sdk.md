# Demo: Function Calling with OpenAI SDK
### The demonstration will cover the following topics:
- Basic string output parsing
- Utilizing tools for structured outputs
- Implementing Pydantic models for type validation
- Understanding different parser types and their applications

## Step-by-Step Instructions

1. **Setup Environment**
### Begin by setting up the environment and importing necessary libraries. Ensure that the .env file is loaded to access any required environment variables. Add the following to your workspace .env (or config.env) when using the Vocareum-hosted OpenAI endpoint:
### OPENAI_API_KEY="voc-key" OPENAI_BASE_URL="https://openai.vocareum.com/v1(opens in a new tab)" TAVILY_API_KEY="tvly-**********"
### We recommend storing Vocareum's base URL in OPENAI_BASE_URL and reading it from code (via os.getenv) so the same code works both locally and in the Vocareum workspace without editing endpoints.
```python
from typing import Annotated
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from lib.messages import UserMessage, SystemMessage
from lib.tooling import tool
from lib.llm import LLM
from lib.parsers import (
    StrOutputParser,
    JsonOutputParser, 
    PydanticOutputParser, 
    ToolOutputParser,
)

load_dotenv()
# Ensure your .env (or config.env) includes OPENAI_BASE_URL set to https://openai.vocareum.com/v1 when using the Vocareum-hosted OpenAI endpoint.
assert os.getenv("OPENAI_API_KEY") is not None
assert os.getenv("OPENAI_BASE_URL") is not None
assert os.getenv("TAVILY_API_KEY") is not None

chat_model = LLM()
```

2. **Basic String Output Parsing**
### Start with a simple example to understand how to parse string outputs from the LLM. This step demonstrates the most basic form of output handling.
```python
messages = [
    SystemMessage(content="Extract the event information."),
    UserMessage(content="Alice and Bob are going to a science fair on Friday.")
]

ai_message = chat_model.invoke(messages)
parser = StrOutputParser()
parsed_output = parser.parse(ai_message)
print(parsed_output)
```
3. **Working with Tools for Structured Outputs**
### Next, utilize tools to enforce a specific output format. This approach simplifies programmatic processing of the LLM's responses.
```python
@tool
def calendar_event(name: str, date: str, participants: list[str]):
    """Identify name of the event, date when it will happen and all the participants"""
    return {
        "name": name,
        "date": date,
        "participants": participants
    }

chat_model_with_tools = LLM(tools=[calendar_event])
ai_message = chat_model_with_tools.invoke(messages)
parser = ToolOutputParser()
structured_output = parser.parse(ai_message)[0]["args"]
```

4. **Using Pydantic Models for Validation**
### Implement Pydantic models to validate and structure the outputs from the LLM. This step ensures type safety and data integrity.
```python
class CalendarEvent(BaseModel):
    """A Pydantic model representing a calendar event."""
    name: Annotated[str, Field(description="Name/Title of the event. Defaults to ''", default=None)]
    date: Annotated[str, Field(description="Date of the event. Defaults to ''", default=None)]
    participants: Annotated[list[str], Field(description="Who will participate. Defaults to ''", default=None)]

ai_message = chat_model.invoke(input=messages, response_format=CalendarEvent)
parser = JsonOutputParser()
json_output = parser.parse(ai_message)

parser = PydanticOutputParser(model_class=CalendarEvent)
event: CalendarEvent = parser.parse(ai_message)
```

5. **Accessing Parsed Data**
### Finally, access the structured data from the validated Pydantic model.
```python
participants = event.participants
print(participants)
```

## Summary of Steps
- Set up the environment and import necessary libraries.
- Parse basic string outputs from the LLM.
- Use tools to create structured outputs.
- Implement Pydantic models for validation and type safety.
- Access and utilize the structured data from the Pydantic model.

## Key Takeaways
- Understanding how to parse outputs from LLMs is crucial for effective data handling.
- Tools can enforce specific output formats, making it easier to work with LLM responses.
- Pydantic models provide a robust way to validate and structure data, ensuring type safety.
- Different parsers serve unique purposes and can be selected based on the output format needed.

## Step-by-Step Instructions
1. **Basic Interaction with Language Models**
- **Single-Turn Query**:
  - Use the invoke method to send a simple question to the AI.
  - Example: response = chat_model.invoke("What is an AI Agent?")
- **Multi-Turn Conversation**:
  - Structure a conversation by defining roles for the AI and the user.
### Example:
```python
messages = [
  SystemMessage(content="You're an OpenAI API specialist"),
  UserMessage(content="What is Function Calling?")
]
response = chat_model.invoke(messages)
```
2. **Building an AI Tool**
- **Define the Tool**:
  - Use the @tool decorator to create a function that retrieves weather data.
  - Ensure the function has clear documentation and typed parameters.
  - Example:

```python
@tool
def get_weather(city: str):
  """Get the current temperature for a city."""
  ...
```
- **Mock Weather Data**:
  - For demonstration purposes, create a dictionary with mock weather data.
  - Example:

```python
mock_weather = {
  "São Paulo": "28°C",
  "Oslo": "-3°C",
  "New York": "15°C",
  "Tokyo": "22°C"
}
```
- **Bind the Tool to the LLM**:
  - Create an instance of the LLM that includes the weather tool.
  - Example: chat_model_with_tools = LLM(tools=[get_weather])

3. **Using the Tool in Conversations**
- **Set Up the Conversation**:
  - Define the system message to instruct the AI on how to use the weather tool.
  - Example:
```python
messages = [
  SystemMessage(content="You are a helpful assistant that can access a tool to get current temperature for cities."),
  UserMessage(content="How cold is it in Oslo?")
]
```
- **Invoke the AI with Tool Usage**:
  - The AI recognizes the need to use the weather tool and makes a tool call.
  - Example:
```python
ai_message = chat_model_with_tools.invoke(messages)
```
- **Extract Tool Call Information**:
  - Retrieve the tool call ID and arguments from the AI's response.
  - Example:
```python
tool_call_id = messages[-1].tool_calls[0].id
args = json.loads(messages[-1].tool_calls[0].function.arguments)
```
- **Execute the Tool**:
  - Call the weather function with the extracted arguments.
  - Example: tool_result = get_weather(**args)
- **Create a Tool Response Message**:
  - Formulate a response message from the tool's result.
  - Example:
```python
tool_message = ToolMessage(content=tool_result["temperature"], tool_call_id=tool_call_id, name="get_weather")
```

- **Final AI Response**:
  - Allow the AI to generate a final response based on the tool's output.
  - Example
```python
ai_message = chat_model_with_tools.invoke(messages)
```
## Takeaways
- Understanding how to interact with Language Models is crucial for effective AI communication.
- Building tools enhances the capabilities of AI, allowing it to perform specific tasks.
- The flow of messages and tool usage is essential for creating a seamless user experience with AI.