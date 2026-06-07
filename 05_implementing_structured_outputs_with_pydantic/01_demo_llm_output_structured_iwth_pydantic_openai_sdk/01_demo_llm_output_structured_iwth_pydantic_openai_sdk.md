from libs_4.messages import SystemMessage

# Demo: Implementing Structured Outputs with Pydantic and OpenAI SDK
### This demonstration showcases how to effectively apply the concepts of structured outputs using Pydantic and the OpenAI SDK. The focus will be on parsing outputs from a Language Model (LLM) and ensuring data integrity through type validation.
### The demonstration will cover the following topics:

- Basic string output parsing
- Utilizing tools for structured outputs
- Implementing Pydantic models for type validation
- Understanding different parser types and their applications

## Step-by-Step Instructions
1. **Setup Environment**
### Begin by setting up the environment and importing necessary libraries. Ensure that the .env file is loaded to access any required environment variables.

```python
from typing import Annotated
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from libs_4.messages import UserMessage, SystemMessage
from libs_4 import tool
from libs_4.llm import LLM
from libs_4 import (
    StrOutputParser,
    JsonOutputParser,
    PydanticOutputParser,
    ToolOutputParser,
)

load_dotenv()

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
- **Summary of Steps**
  - Set up the environment and import necessary libraries.
  - Parse basic string outputs from the LLM.
  - Use tools to create structured outputs.
  - Implement Pydantic models for validation and type safety.
  - Access and utilize the structured data from the Pydantic model.
- **Key Takeaways**
  - Understanding how to parse outputs from LLMs is crucial for effective data handling.
  - Tools can enforce specific output formats, making it easier to work with LLM responses.
  - Pydantic models provide a robust way to validate and structure data, ensuring type safety.
  - Different parsers serve unique purposes and can be selected based on the output format needed.