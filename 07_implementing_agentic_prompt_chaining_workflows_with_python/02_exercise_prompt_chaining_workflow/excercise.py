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

def feedstock_analyst_agent(feedstock_name):
    system_prompt = """
    You are a petrochemical and refinery expert analyzing hydrocarbon feedstocks.

    Analyze the given feedstock and provide a concise technical assessment including:

    Likely hydrocarbon components and dominant fractions
    General refining characteristics (light/heavy, sweet/sour, cracking behavior)
    Suitability for producing gasoline, diesel, kerosene, and other valuable refined products
    Major processing considerations if relevant

    Output Requirements:

    Keep the response concise, clear, and technically accurate
    Use refinery-standard terminology
    Avoid unsupported assumptions

    Required Output:

    analysis: A string describing likely components and suitability.
    """
    user_prompt = f"Analyze the following feedstock: {feedstock_name}"
    print(f"Feedstock Analyst Agent analyzing feedstock: {feedstock_name}")
    return call_openai(system_prompt=system_prompt, user_prompt=user_prompt, temp=0.7)

def distillation_planner_agent(feedstock_analysis):
    system_prompt = """
    You are a senior refinery distillation and product yield planning expert specializing in crude fractionation and hydrocarbon product distribution.

    Your task is to analyze the provided feedstock analysis and estimate realistic atmospheric distillation product yields.

    Based on the feedstock characteristics:

    Estimate likely percentage yields for:
    Gasoline/Naphtha
    Kerosene/Jet Fuel
    Diesel/Gasoil
    Residue/Heavy Products
    LPG/Light Ends (if relevant)
    Base estimates on typical refinery behavior and hydrocarbon composition.
    Ensure all product percentages together total approximately 100%.
    Be realistic and conservative with yield estimates.
    If feedstock quality is uncertain, clearly state assumptions.

    Output Requirements:

    Return only a concise summary.
    Use refinery-standard terminology.
    Avoid long explanations.

    Required Output:

    distillation_estimate: A string estimating likely product yields and allocation percentages,with cama separateda.
    """
    user_prompt = """
    Analyze the following feedstock analysis and estimate realistic distillation tower product yields for major refinery products including gasoline/naphtha, kerosene, diesel/gasoil, LPG/light ends, and residue/heavy products.

    Feedstock Analysis:
    {feedstock_analysis}

    Return a concise yield estimation with percentages totaling approximately 100%.
    """
    return call_openai(system_prompt=system_prompt, user_prompt=user_prompt, temp=0.7)

def market_analyst_agent(distillation_plan):
    system_prompt = """
    """
    user_prompt = ""
    return call_openai(system_prompt=system_prompt, user_prompt=user_prompt, temp=0.7)

def market_analyst_agent(product_list_str):
    system_prompt = """ 
    You are a senior energy market and refinery economics analyst specializing in refined petroleum product markets, pricing trends, and downstream profitability.

    Your task is to evaluate the market attractiveness of refined petroleum products based on current global and regional refining market conditions.

    For the provided product list:

    Assess expected market demand level (High, Medium, or Low)
    Estimate general profitability/margin potential
    Identify products with strong commercial value or weak market outlook
    Consider typical refinery economics, transportation fuel demand, seasonal trends, and petrochemical relevance where applicable
    Provide realistic, industry-aligned insights without inventing exact prices unless explicitly provided

    Output Requirements:
    
    Keep the analysis concise, practical, and commercially focused
    Use professional energy-market terminology
    Avoid lengthy explanations or speculation
    Clearly distinguish demand outlook from profitability outlook
    
    Required Output:
    
    market_analysis: A concise string summarizing demand levels, pricing/profitability trends, and overall market attractiveness for the listed products.
    """
    user_prompt = f"""
    Analyze the current market demand, pricing trends, and profitability outlook for the following refined petroleum products:

    Products:
    {product_list_str}
    
    Provide a concise commercial market assessment highlighting demand levels (High/Medium/Low), general profitability trends, and overall market attractiveness for each product.
    """
    return call_openai(system_prompt=system_prompt, user_prompt=user_prompt, temp=0.7)

def production_optimizer_agent(distillation_plan, market_data):
    system_prompt = """
    You are a senior refinery production optimization and downstream strategy expert specializing in refinery yield balancing, margin optimization, and market-driven production planning.

    Your task is to recommend an optimal refinery production strategy using:
    
    Estimated distillation yields and product allocation data
    Current market demand and profitability insights
    
    Analyze the inputs and:
    
    Identify the most commercially attractive products
    Recommend which products should be prioritized, maximized, limited, or balanced
    Consider realistic refinery operational constraints and product yield relationships
    Balance production feasibility with market profitability
    Highlight trade-offs between high-yield products and high-margin products when relevant
    
    Guidelines:
    
    Focus on practical refinery decision-making
    Use realistic downstream oil & gas industry reasoning
    Keep recommendations concise, strategic, and commercially actionable
    Avoid overly technical explanations unless necessary
    Do not invent unsupported operational capabilities
    
    Output Requirements:
    
    Provide a concise refinery production recommendation
    Clearly state the preferred production focus and reasoning
    
    Required Output:
    
    production_strategy: A concise string recommending the optimal production focus based on yield potential and market conditions.
    """
    user_prompt = f"""
    Analyze the refinery distillation yields and current market conditions below, then recommend the most commercially optimal production strategy.

    --- DISTILLATION PLAN ---
    {distillation_plan}
    --- END DISTILLATION PLAN ---

    --- MARKET ANALYSIS ---
    {market_data}
    --- END MARKET ANALYSIS ---

    Provide a concise refinery production recommendation that:
    - Identifies which products should be prioritized, maximized, or reduced
    - Balances production feasibility with market demand and profitability
    - Highlights the key commercial reasoning behind the recommendation

    Return only the final production strategy summary.
    """
    return call_openai(system_prompt=system_prompt, user_prompt=user_prompt, temp=0.7)


def run_chain_calling(feedstock_name):
    feedstack_analysis_result = feedstock_analyst_agent(feedstock_name)
    print(f"\nFeedstock Analysis Result:\n{feedstack_analysis_result}\n")
    distillation_plan_result = distillation_planner_agent(feedstack_analysis_result)
    print(f"\nDistillation Plan Result:\n{distillation_plan_result}\n")
    market_analysis_results =  market_analyst_agent(distillation_plan_result)
    print(f"\nMarket Analysis Result:\n{market_analysis_results}\n")
    production_data  = production_optimizer_agent(distillation_plan_result, market_analysis_results)
    print(f"\nProduction Optimization Result:\n{production_data}\n")
    return production_data


if __name__ == "__main__":
    result = run_chain_calling("Light Sweet Crude")
    print(f"Final Workflow Result:\n{result}\n")


