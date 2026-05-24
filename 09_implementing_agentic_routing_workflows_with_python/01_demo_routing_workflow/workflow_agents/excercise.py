from openai import OpenAI

client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key = ""
)

def call_openai(system_prompt, user_prompt, temperature, model="gpt-3.5-turbo"):
    try:
        response = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Exception occurred due to {e}"

class CodeGenerationAgent:
    """
    Agent that generates code from OpenAI's codegen API based on description
    """
    def __init__(self):
        self.description = "Code Generation Agent: Use this agent to generate code in various programming languages based on a textual description of the desired functionality."
        self.name = "Code Generation Agent"

    def get_description(self):
        """
        Return description of the agent
        """
        return self.description

    def run(self, task_prompt):
        """
        Run the agent with the given task description and return the generated code
        """
        system_prompt = """
        You are a specialist Code Generation Agent. Your task is to write clean, efficient, and well-documented code based on the user's request.
        Provide only the code block for the requested language, followed by a brief explanation of how it works.
        """
        user_prompt = f"Generate code for the following task: {task_prompt}"
        print(f"{self.name} is generating code for task: {task_prompt}")
        return call_openai(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.7)


class EuropeanHistoryQAAgent:
    """Agent that answers questions about European history."""
    def __init__(self):
        self.description = "European History Q&A Agent: Use this agent to get answers to specific questions about European history, from ancient times to the modern era."
        self.name = "European History Q&A Agent"

    def get_description(self):
        """Returns the agent's description."""
        return self.description

    def run(self, task_prompt):
        system_prompt = """You are a specialist European History Agent. Your task is to provide accurate and detailed answers to questions about European history.
        Cite key dates, figures, and events in your response."""
        user_prompt = f"Answer the following question about European history: {task_prompt}"
        print(f"{self.name} is answering a question: {task_prompt}")
        return call_openai(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.7)

class MathematicalProblemSolvingAgent:
    """Agent that solves mathematical problems."""
    def __init__(self):
        self.description = "Mathematical Problem Solving Agent: Use this agent to solve mathematical problems, including algebra, calculus, and other quantitative tasks."
        self.name = "Mathematical Problem Solving Agent"

    def get_description(self):
        """Returns the agent's description."""
        return self.description

    def run(self, task_prompt):
        system_prompt = """You are a specialist Mathematical Problem Solving Agent. Your task is to solve the given mathematical problem, showing the steps involved for clarity.
    Provide the final answer clearly."""
        user_prompt = f"Solve the following mathematical problem: {task_prompt}"
        print(f"{self.name} is solving a problem: {task_prompt}")
        return call_openai(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.7)

def routing_agent(task_prompt, agents):
    """
        Routing agent that uses an LLM to determine which agent to use based on the task prompt.
        Args:
            task_prompt (str): The user's request.
            agents (list): A list of agent objects to choose from.
        """
    # Dynamically create the list of available agents from their descriptions
    agent_descriptions = "\n".join([f"- {agent.get_description()}" for agent in agents])
    system_prompt = f"""You are an expert AI routing assistant. Your job is to analyze a user's task prompt and route it to the most appropriate agent.
        You have the following agents available:
        {agent_descriptions}

        Analyze the user's task prompt below and determine which agent is the best fit.
        Respond only with the exact name of the agent (e.g., 'Code Generation Agent'), and nothing else.

        Task: {task_prompt}"""
    user_prompt = f"Given the task: '{task_prompt}', which agent should handle this task?"
    # Use an LLM to choose the agent
    agent_choice_name = call_openai(system_prompt=system_prompt, user_prompt=user_prompt, temperature=0.7).strip()

    # Find the chosen agent object and run it
    for agent in agents:
        if agent.name == agent_choice_name:
            print(f"--- Routing task to {agent.name}... ---")
            return agent.run(task_prompt)

    return f"Error: Could not find an agent named '{agent_choice_name}'. Please check the routing prompt."


if __name__ == "__main__":
    print("--- Initializing Agents ---")
    code_generation_agent = CodeGenerationAgent()
    history_agent = EuropeanHistoryQAAgent()
    math_agent = MathematicalProblemSolvingAgent()
    all_agents = [code_generation_agent, history_agent, math_agent]

    # --- Example 1: Code Generation Task ---
    math_task_prompt = "Write a Python function that implements a recursive binary search algorithm."
    print(f"User Task: \"{math_task_prompt}\"")
    math_task_result = routing_agent(math_task_prompt, all_agents)
    print("\nAgent Output:\n", math_task_result)
    print("\n" + "=" * 50 + "\n")

    # --- Example 2: European History Task ---
    history_task_prompt = "What were the main causes of the French Revolution?"
    print(f"User Task: \"{history_task_prompt}\"")
    result2 = routing_agent(history_task_prompt, all_agents)
    print("\nAgent Output:\n", result2)
    print("\n" + "=" * 50 + "\n")

    # --- Example 3: Mathematical Task ---
    math_task_prompt = "Calculate the derivative of f(x) = 5x^4 + 3x^2 - 2x + 7."
    print(f"User Task: \"{math_task_prompt}\"")
    result3 = routing_agent(math_task_prompt, all_agents)
    print("\nAgent Output:\n", result3)