from openai import OpenAI

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

MAX_RETRIES = 3
user_prompt = (
    "Write a summary for potential investors explaining why decentralized finance (DeFi) will outperform "
    "traditional banking in the next five years. Use strong language to inspire confidence and urgency. "
    "Include examples of past DeFi gains and suggest what investors can expect from leading protocols in the near future."
)

class FinancialReportAgent:
    def run(self, prompt, feedback:None):
        system_prompt = "You are a financial analyst writing a professional investment summary."
        full_prompt = prompt
        # Modify the prompt if feedback is provided
        if feedback:
            full_prompt += f"\n\nEvaluator feedback: {feedback}\nPlease revise accordingly."
        print(f"\n📊 Generating report with prompt:\n{full_prompt}\n")
        return call_openai(system_prompt, full_prompt)

class ComplianceAgent:
    def run(self, report_text):
        print("🔍 Evaluating report compliance...")
        system_message = (
            "You are a compliance officer reviewing investment summaries. "
            "Reject anything with forward-looking statements, speculative claims, or language like 'expected', 'projected', 'will likely', etc."
        )
        eval_prompt = f"Evaluate this investment summary for compliance:\n\n{report_text}\n\nRespond with 'Approved' or provide feedback for revision."
        return call_openai(system_message, eval_prompt)


def main():
    report_agent = FinancialReportAgent()
    compliance_agent = ComplianceAgent()

    report_text = ""
    feedback = None
    for attempt in range(MAX_RETRIES):
        print(f"--- Attempt #{attempt} ---")
        report_text = report_agent.run(user_prompt, feedback)
        evaluation = compliance_agent.run(report_text)
        print(f"\n🧾 Evaluation Result:\n{evaluation}\n")
        if evaluation.lower().startswith("approved"):
            print("\n✅ Final Approved Investment Summary:\n")
            print(report_text)
            break
        else:
            feedback = evaluation
    else:
        print("\n❌ Failed to meet compliance after max retries.")
        print("Last version of the report:")
        print(report_text)

if __name__ == "__main__":
    main()

