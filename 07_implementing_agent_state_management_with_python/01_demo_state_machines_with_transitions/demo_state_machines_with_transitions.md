# Demo: State machines with transitions
### This demonstration focuses on applying state machine concepts to manage workflows effectively. State machines provide a structured way to handle various states and transitions, making it easier to control the flow of data and logic in applications. The following steps will illustrate how to create a state machine, define its states, and manage transitions between those states using Python code. Key concepts such as basic state machine implementation, workflow steps, state transitions, and data flow will be covered.

## Steps

1. **Setup the Environment**
### Begin by importing the necessary libraries and defining the state schema. This schema outlines the structure of the state that will be managed by the state machine.
```python
from typing import TypedDict
from libs_7_1.state_machine import (
      StateMachine,
      Step,
      EntryPoint,
      Termination,
)
```
2. **Define the State Schema**
### Create a schema that defines the attributes of the state. For example, a simple schema can include an input and an output value.
```python
class Schema(TypedDict):
      input: int
      output: int
```
3. **Create the State Machine Instance**
### Instantiate the state machine using the defined schema.
```python
workflow = StateMachine(Schema)
```
4. **Define the Logic for Steps**
### Create functions that define the logic for each step in the workflow. Each function takes the current state as input and returns an updated state.
```python
def step_input(state: Schema) -> Schema:
      return {"output": state["input"] + 1}

def step_double(state: Schema) -> Schema:
      return {"output": state["output"] * 2}
```

5. **Create and Connect Steps**
### Define the entry point, steps, and termination for the workflow. Connect these components to establish the flow of the state machine.
```python
entry = EntryPoint()
s1 = Step("input", step_input)
s2 = Step("double", step_double)
termination = Termination()

workflow.add_steps([entry, s1, s2, termination])
workflow.connect(entry, s1)
workflow.connect(s1, s2)
workflow.connect(s2, termination)
```
6. **Run the Workflow**
### Initialize the state and run the workflow. The output will show the results of the state transitions.
```python
initial_state = {"input": 4}
run_object = workflow.run(initial_state)
```
7. **Advanced State Management: Routing and Loops**
### Explore more complex patterns by introducing conditional routing and loops. Define a new schema for a counter-based workflow.
```python
class CounterSchema(TypedDict):
      count: int
      max_value: int
```
8. **Define Counter Logic**
### Create a function to increment the counter and define the entry point, increment step, and termination.
```python
def increment_counter(state: CounterSchema) -> CounterSchema:
      return {"count": state["count"] + 1}

entry = EntryPoint()
increment = Step("increment", increment_counter)
termination = Termination()
```
9. **Implement Router Logic**
### Create a function to determine the next step based on the counter value. This function will control the flow of the workflow based on conditions.
```python
def check_counter(state: CounterSchema) -> Step:
      if state["count"] >= state["max_value"]:
          return termination
      return increment
```
10. **Connect Steps with a Loop**
### Connect the entry point to the increment step and establish a loop that allows the workflow to continue until the termination condition is met.
```python
workflow.connect(entry, increment)
workflow.connect(increment, [increment, termination], check_counter)
```
11. **Run the Counter Workflow**
### Initialize the counter state and run the workflow to observe the transitions.
```python
initial_state = {"count": 0, "max_value": 3}
run_object = workflow.run(initial_state)
```
## Summary
### This demonstration illustrated how to create and manage state machines using Python. The following steps were covered:
- Setting up the environment and defining the state schema.
- Creating a state machine instance and defining the logic for steps.
- Connecting steps to establish the workflow.
- Running the workflow and observing state transitions.
- Implementing advanced state management techniques, including routing and loops.
## Takeaways
- State machines provide a structured approach to manage workflows and transitions.
- Defining clear schemas and step functions is crucial for effective state management.
- Advanced techniques like routing and loops enhance the flexibility of state machines.
- Observing state transitions helps in understanding the flow of data and logic in applications.
