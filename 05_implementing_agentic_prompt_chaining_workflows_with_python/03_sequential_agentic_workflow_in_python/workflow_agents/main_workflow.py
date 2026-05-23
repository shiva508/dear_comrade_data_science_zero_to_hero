from agent_definitions import ResearchAgent, SummarizerAgent, FactCheckerAgent
def run_user_query_workflow(user_query):
    """
    Initialize agents and run the workflow for a user query.
    """
    research_agent = ResearchAgent("Researcher")
    summarizer_agent = SummarizerAgent("Summarizer")
    fact_checker_agent = FactCheckerAgent("FactChecker")

    # Run the workflow
    research_results = research_agent.run(user_query)
    print(f"  → Output: {str(research_results)[:50]}...\n")
    fact_check_results = fact_checker_agent.run(research_results)
    print(f"  → Output: {str(fact_check_results)[:50]}...\n")
    summarization_result = summarizer_agent.run(fact_check_results["text"])
    print(f"  → Output: {str(summarization_result)[:50]}...\n")

    print("✅ Workflow 'Information Processing' completed\n")

    print("Final result:")
    print(summarization_result)

    print("\nKey concepts demonstrated:")
    print("1. Agents as components that perform specific tasks")
    print("2. Workflow connecting agents in sequence")
    print("3. Information flowing through the system")


if __name__ == "__main__":
    run_user_query_workflow("What are the latest advancements in renewable energy?")