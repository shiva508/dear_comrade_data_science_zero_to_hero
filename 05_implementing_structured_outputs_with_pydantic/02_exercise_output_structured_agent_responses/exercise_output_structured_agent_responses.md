# Exercise: Output structured Agent responses
### In this hands-on exercise, learners will enhance an AI agent to provide structured outputs using Pydantic models. This exercise focuses on ensuring that the agent's responses are consistent, validated, and easily usable in downstream applications. By applying the skills and concepts learned in previous sections, learners will create structured output formats, parse and validate responses, and return data in a consistent JSON format. The task involves defining a Pydantic model for structured tasks, such as summarizing a meeting with action items, and building a bridge from language to logic.
## Prerequisites:
- Python programming language
- Pydantic library


## Objectives:
### By the end of this exercise, learners will be able to:
- Define structured output formats using Pydantic models
- Enhance an existing agent class to support structured outputs
- Validate and parse responses to ensure they meet defined formats

## Steps:
1. **Set Up the Workspace**
   - Open the classroom workspace provided for this exercise.
   - Ensure all necessary libraries are installed, including Pydantic.

2. **Import Required Libraries**
   - At the beginning of your code, import the necessary libraries:
```python
from typing import List, Any
from pydantic import BaseModel, Field
import json
```
3. **Define Pydantic Models**
   - Create a Pydantic model for action items. Include fields for task, assignee, and due date.
```python
class ActionItem(BaseModel):
task: str = Field(..., description="Task description")
assignee: str = Field(..., description="Person responsible for the task")
due_date: str = Field(..., description="Due date for the task")
``` 
   - Create a Pydantic model for meeting summaries. Include fields for title, date, participants, key points, and action items.
```python
class MeetingSummary(BaseModel):
title: str
date: str
participants: List[str]
key_points: List[str]
action_items: List[ActionItem]
```
4. **Enhance the Agent Class**
 - Create a new class called StructuredAgent that inherits from the existing Agent class.
 - Initialize the agent with role, instructions, model, temperature, tools, and output model.
 - Implement the invoke method to process user messages and return structured responses.

5. **Test the Enhanced Agent**
 - Create an instance of the StructuredAgent using the MeetingSummary model.
 - Prepare a sample meeting transcript and invoke the agent to generate a summary.
```python
meeting_agent = StructuredAgent(
role="Meeting Assistant",
instructions="Summarize meetings and track action items in a structured format",
output_model=MeetingSummary
)
meeting_transcript = "..."
summary = meeting_agent.invoke(meeting_transcript)
print(json.dumps(summary, indent=2))
```
6. **Validate the Output**
   - Create an instance of MeetingSummary using the output from the agent.
   - Access and print structured data to verify that it matches the expected format.
```python
validated_summary = MeetingSummary(**summary)
print("Meeting Title:", validated_summary.title)
```