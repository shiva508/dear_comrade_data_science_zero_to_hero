# Constructing Agentic Systems with Python
### How can you structure Python code to build agentic components? A design that mirrors a logical separation of concerns can promote modularity and clarity, using standard Python features.
1. **Agent Library/Module**: One common practice is to create a dedicated Python module (e.g., a file named agent_definitions.py). This file would house the class definitions for various types of agents. These classes serve as the blueprints defining the agents' attributes and methods, assuming familiarity with Python's object-oriented programming concepts.
2. **Agent Instantiation Logic**: Separately, in a script that drives the workflow, one would import these agent classes. Here, specific instances (objects) of these agent classes would be created and configured. This is where each agent could be customized to its specific role or task.
3. **Workflow Implementation Logic**: Finally, the logic for the actual workflow would be implemented. This involves defining the sequence of tasks, how data is passed between the instantiated agents, and how these agents collaborate to achieve the overall goal of the system.
### This structured design—separating agent definitions (typically as classes), instantiation logic (creating objects), and workflow implementation—provides a scalable foundation for developing agentic systems in Python.
### Let's look at a simple scenario: an agentic workflow that first fetches some data (like a user profile) and then processes that data (perhaps to extract key information).
### *Agent Library/Module (e.g., agent_definitions.py****)*
### This file will house the class definitions for our various types of agents. These classes act as blueprints.
```python
# workflow_agents/agent_definitions.py

class Agent:
    """
    A base class for our agents.
    While not strictly necessary for simple cases,
    it can be useful for defining common interfaces or utilities.
    """
    def __init__(self, name):
        self.name = name
        print(f"Agent '{self.name}' initialized.")

    def execute(self, data=None):
        """
        A generic method to execute the agent's task.
        Specific agents will override this.
        """
        raise NotImplementedError("Each agent must implement the 'execute' method.")

class DataFetchingAgent(Agent):
    """
    An agent specialized in fetching data.
    For this example, it will simulate fetching user data.
    """
    def __init__(self, name, data_source):
        super().__init__(name)
        self.data_source = data_source
        print(f"DataFetchingAgent will fetch from: {self.data_source}")

    def execute(self, user_id):
        """
        Simulates fetching data for a given user_id.
        In a real scenario, this might involve an API call or database query.
        """
        print(f"'{self.name}' is fetching data for user_id: {user_id} from {self.data_source}...")
        # Simulate data fetching
        if user_id == "123":
            return {"user_id": "123", "name": "Alice Wonderland", "occupation": "Dreamer"}
        else:
            return {"user_id": user_id, "error": "User not found"}

class DataProcessingAgent(Agent):
    """
    An agent specialized in processing data.
    For this example, it will extract key information from the fetched data.
    """
    def __init__(self, name, fields_to_extract=None):
        super().__init__(name)
        self.fields_to_extract = fields_to_extract if fields_to_extract else ["name", "occupation"]
        print(f"DataProcessingAgent will extract fields: {self.fields_to_extract}")

    def execute(self, fetched_data):
        """
        Processes the fetched data to extract specified fields.
        """
        print(f"'{self.name}' is processing data: {fetched_data}")
        if "error" in fetched_data:
            return {"processed_info": None, "error": fetched_data["error"]}

        processed_info = {}
        for field in self.fields_to_extract:
            processed_info[field] = fetched_data.get(field, "N/A")

        return {"processed_info": processed_info, "original_data_keys": list(fetched_data.keys())}
```
### agent_definitions.py:

- We have a base Agent class with an __init__ method to give each agent a name and an execute method that specific agents must implement.
- DataFetchingAgent inherits from Agent. Its execute method simulates fetching data for a user.
- DataProcessingAgent also inherits from Agent. Its execute method takes the data fetched by the previous agent and extracts specific fields.
- These classes serve as the blueprints defining the agents' attributes and methods.
## Agent Instantiation and Workflow Implementation Logic (e.g., main_workflow.py)
### This script will import the agent classes, create specific instances (objects) of them, and then define the actual workflow by coordinating these instances.
```python
# main_workflow.py

# Import agent classes from our library
from workflow_agents.agent_definitions import DataFetchingAgent, DataProcessingAgent

def run_user_data_workflow(user_id_to_process):
    """
    This function implements the agentic workflow.
    """
    print(f"\n--- Starting User Data Workflow for User ID: {user_id_to_process} ---")

    # === 2. Agent Instantiation Logic ===
    # Create specific instances (objects) of agent classes and configure them.
    # Each agent can be customized for its specific role or task.
    fetcher = DataFetchingAgent(name="UserProfileFetcher", data_source="MainUserDatabase")
    processor = DataProcessingAgent(name="UserInfoExtractor", fields_to_extract=["name", "occupation", "user_id"])

    print("--- Agents Instantiated ---")

    # === 3. Workflow Implementation Logic ===
    # Define the sequence of tasks and how data is passed between agents.

    # Step 1: Fetch user data
    print("\nStep 1: Fetching Data...")
    fetched_user_data = fetcher.execute(user_id=user_id_to_process)
    print(f"Fetcher Output: {fetched_user_data}")

    if "error" in fetched_user_data and fetched_user_data["error"]:
        print(f"Workflow stopped due to error in fetching: {fetched_user_data['error']}")
        return {"status": "Error", "details": fetched_user_data['error']}

    # Step 2: Process fetched data
    print("\nStep 2: Processing Data...")
    processed_data_report = processor.execute(fetched_data=fetched_user_data)
    print(f"Processor Output: {processed_data_report}")

    print("--- Workflow Completed ---")
    return {"status": "Success", "data": processed_data_report}

if __name__ == "__main__":
    # Example 1: Successful run
    result1 = run_user_data_workflow("123")
    print(f"\nFinal Result for User 123: {result1}\n")

    # Example 2: User not found
    result2 = run_user_data_workflow("456")
    print(f"Final Result for User 456: {result2}")
```