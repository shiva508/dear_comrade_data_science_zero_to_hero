from openai import OpenAI

client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key=""
)

def call_openai(system_prompt, user_prompt, temp, model="gpt-3.5-turbo"):
    """
    Simple wrapper around the OpenAI's API
    """
    response = client.chat.completions.create(
        model=model,
        temperature=temp,
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
     )
    return response.choices[0].message.content.strip()


def research_agent(topic):
    system_prompt = """
    You are a research specialist who provides structured information. Always format your response with these exact headings: 
    # OVERVIEW 
    # KEY POINTS 
    # DETAILS"
    """
    user_prompt = f"Research this topic thoroughly : {topic}"
    print(f"Research agent working on topic: {topic}")
    return call_openai(system_prompt, user_prompt, temp=0.7)

def writer_agent(topic, research_results):
    system_prompt = """You are a content writer who creates engaging material from research.
    Create a well-structured article with a clear introduction, body, and conclusion.
    """
    user_prompt = f"""Write an engaging article about {topic} using this research:
        {research_results}
        """
    print(f"Writer agent creating content for: {topic}")
    return call_openai(system_prompt, user_prompt, temp=0.7)

def run_chain_calling   (topic):
    print(f"Starting workflow for topic: {topic}\n")
    research_results = research_agent(topic)
    print(f"\nResearch Results:\n{research_results}\n")
    article = writer_agent(topic, research_results)
    print(f"\nGenerated Article:\n{article}\n")
    return {"research_results": research_results, "article": article}


if __name__ == "__main__":
    result = run_chain_calling("The impact of AI on education")
    print(f"Final Workflow Result:\n{result}\n")