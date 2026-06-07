from pydantic import BaseModel, Field
from typing import Optional, Union, List, Dict, Any, Literal

## Base message
class BaseMessage(BaseModel):
    content: Optional[str] = ""

    ## default method to convert to dict, which is used by the OpenAI SDK when sending messages to the API
    def dict(self) -> Dict:
        return dict(self)

## System message model
class SystemMessage(BaseMessage):
    role: Literal["system"] = "system"


## User message model
class UserMessage(BaseMessage):
    role: Literal["user"] = "user"

## Tool message
class ToolMessage(BaseMessage):
    role: Literal["tool"] = "tool"
    tool_call_id: str
    name: str

## AI message model, which includes an optional field for tool calls that the AI may make in its response
class AIMessage(BaseMessage):
    role: Literal["assistant"] = "assistant"
    tool_calls: Optional[List[Any]] = None



AnyMessage = Union[
    SystemMessage,
    UserMessage,
    AIMessage,
    ToolMessage
]
