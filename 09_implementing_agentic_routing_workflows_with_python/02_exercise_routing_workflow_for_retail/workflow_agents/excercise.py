from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key = ""
)


# --- Helper Function for API Calls ---
def call_openai(system_prompt, user_prompt, model="gpt-3.5-turbo"):
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


# --- Agents for Different Retail Tasks ---

def product_researcher_agent(query):
    """Product researcher agent gathers product information."""
    system_prompt = """You are a product research agent for a retail company. Your task is to provide 
    structured information about products, market trends, and competitor pricing."""

    user_prompt = f"Research this product thoroughly: {query}"
    return call_openai(system_prompt, user_prompt)


def customer_analyzer_agent(query):
    """Customer analyzer agent processes customer data and feedback."""
    system_prompt = """You are a customer analysis agent. Your task is to analyze customer feedback, 
    preferences, and purchasing patterns."""

    user_prompt = f"Analyze customer behavior for: {query}"
    return call_openai(system_prompt, user_prompt)


def pricing_strategist_agent(query, product_data=None, customer_data=None):
    """Pricing strategist agent recommends optimal pricing."""
    system_prompt = """You are a pricing strategist agent. Your task is to recommend optimal pricing 
    strategies based on product research and customer analysis."""

    # TODO: Implement this function
    # It should use product_data and customer_data to inform the pricing strategy
    user_prompt = f"""
    Original Pricing Query: {query}
    Product Research Data:
    {product_data}
    Customer Analysis Data:
    {customer_data}
    Based on all the above information, please provide a recommended pricing strategy, suggest an optimal price or price range, and explain your reasoning.
    """
    return call_openai(system_prompt, user_prompt)


# --- Routing Agent with LLM-Based Task Determination ---
def routing_agent(query, context=None):
    """Routing agent that determines which agent to use based on the query."""

    # TODO: Implement the routing agent
    # 1. Use an LLM to analyze the query and determine the correct task type
    system_prompt_classifier = """You are an AI assistant that can route retail queries to 
    product_researcher_agent, customer_analyzer_agent, or pricing_strategist_agent based on the content of the query.
    Respond only with the agent's name, nothing else."""
    user_prompt_classifier = f"Given the query: '{query}', which agent should handle this task?"
    agent_choice = call_openai(system_prompt_classifier, user_prompt_classifier).strip()
    print(f"LLM Classified Task For: {agent_choice}")

    # 2. Route the query to the appropriate agent
    if "product_researcher_agent" in agent_choice:
        print("Routing to Product Researcher Agent...")
        return product_researcher_agent(query)
    elif "customer_analyzer_agent" in agent_choice:
        print("Routing to Customer Analyzer Agent...")
        return customer_analyzer_agent(query)
    elif "pricing_strategist_agent" in agent_choice:
        print("Routing to Pricing Strategist Agent...")
        # For the pricing strategist, we need to gather additional data from the other agents
        product_data = None
        customer_data = None
        if context and "product_data" in context:
            product_data = context["product_data"]
        else:
            product_data = product_researcher_agent(query)
        if context and "customer_data" in context:
            customer_data = context["customer_data"]
        else:
            customer_data = customer_analyzer_agent(query)

        product_data = product_researcher_agent(query)
        customer_data = customer_analyzer_agent(query)
        return pricing_strategist_agent(query, product_data=product_data, customer_data=customer_data)
    else:
        print("LLM could not classify the task. Please check the query and try again.")
        return None
    # 3. Return the results from the chosen agent
    pass  # Replace this with your implementation


# --- Example Usage ---
if __name__ == "__main__":
    # Example queries
    queries = [
        "What are the specifications and current market trends for wireless earbuds?",
        "What do customers think about our premium coffee brand?",
        "What should be the optimal price for our new organic skincare line?"
    ]

    # Process each query
    for query in queries:
        print(f"\nQuery: {query}")
        print("\nProcessing...")
        result = routing_agent(query)
        # TODO: Use the routing agent to process the query
        # Print the results
        print("\nResult:\n", result)