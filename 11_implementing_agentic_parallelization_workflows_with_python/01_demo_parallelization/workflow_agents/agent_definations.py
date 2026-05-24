from openai import OpenAI
from dotenv import load_dotenv
import threading

user_prompt = "What are current trends shaping the future of the energy industry?"

client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key = ""
)

agent_outputs = {}
# --- Helper Function for API Calls ---
def call_openai(system_prompt, input_user_prompt, model="gpt-3.5-turbo"):
    """Simple wrapper for OpenAI API calls."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content


class Agent:
    def __init__(self, name):
        self.name = name
        print(f"Agent {name} created")

    def execute(self, prompt):
        print(f"Agent {self.name} is executing task: {prompt}")
        # Simulate task execution
        print(f"Agent {self.name} completed task: {prompt}")

class PolicyAgent(Agent):
    def execute(self, prompt):
        print(f"Policy Agent resolving prompt: {prompt}")
        system_prompt = """You are a policy expert in global energy policy and climate regulations."""
        agent_outputs["policy"] = call_openai(system_prompt, prompt)

class TechnologyAgent(Agent):
    def execute(self, prompt):
        print(f"Technology Agent resolving prompt: {prompt}")
        system_prompt = """You are an expert in renewable energy, smart grids, and energy storage technologies."""
        agent_outputs["tech"] = call_openai(system_prompt, prompt)

class MarketAgent(Agent):
    def execute(self, prompt):
        print(f"Market Agent resolving prompt: {prompt}")
        system_prompt = """You are an energy market analyst focused on global investment, pricing, and demand trends."""
        agent_outputs["market"] = call_openai(system_prompt, prompt)


class SummaryAgent():
    def __init__(self, name):
        self.name = name
        print(f"Agent {name} created")
    def run(self, prompt, inputs):
        combined_prompt = (
            f"The user asked: '{prompt}'\n\n"
            f"Here are the expert responses:\n"
            f"- Policy Expert: {inputs['policy']}\n\n"
            f"- Technology Expert: {inputs['tech']}\n\n"
            f"- Market Expert: {inputs['market']}\n\n"
            "Please summarize the combined insights into a single clear and concise response."
        )
        print(f"Summary Agent resolving prompt: {combined_prompt}")
        system_prompt = """You are an energy strategist skilled at synthesizing expert insights."""
        user_prompt = combined_prompt
        return call_openai(system_prompt, user_prompt)


def main():
    policy_agent = PolicyAgent("PolicyAgent")
    technology_agent = TechnologyAgent("TechnologyAgent")
    market_agent = MarketAgent("MarketAgent")
    summary_agent = SummaryAgent("SummaryAgent")

    # Define tasks for each agent
    policy_task = "Analyze the impact of new regulations on the renewable energy sector."
    technology_task = "Evaluate the latest advancements in solar panel technology."
    market_task = "Assess the current market trends for electric vehicles."

    # Create threads for parallel execution
    threads = []
    threads.append(threading.Thread(target=policy_agent.execute, args=(user_prompt,)))
    threads.append(threading.Thread(target=technology_agent.execute, args=(user_prompt,)))
    threads.append(threading.Thread(target=market_agent.execute, args=(user_prompt,)))

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # After all agents have completed their tasks, we can summarize the results
    summary_task = f"Summarize the insights from the following outputs: {agent_outputs}"
    result = summary_agent.run(summary_task, agent_outputs)
    print(f"✅ All agents have completed their tasks and the summary is generated.\n {result}")

if __name__ == "__main__":
    main()