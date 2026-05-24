from openai import OpenAI
import threading

user_prompt = "What are current trends shaping the future of the energy industry?"

client = OpenAI(
    base_url = "https://openai.vocareum.com/v1",
    api_key = ""
)

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

# Shared dict for thread-safe collection of agent outputs
agent_outputs = {}

# Example contract text (in a real application, this would be loaded from a file)
contract_text = """
CONSULTING AGREEMENT

This Consulting Agreement (the "Agreement") is made effective as of January 1, 2025 (the "Effective Date"), by and between ABC Corporation, a Delaware corporation ("Client"), and XYZ Consulting LLC, a California limited liability company ("Consultant").

1. SERVICES. Consultant shall provide Client with the following services: strategic business consulting, market analysis, and technology implementation advice (the "Services").

2. TERM. This Agreement shall commence on the Effective Date and shall continue for a period of 12 months, unless earlier terminated.

3. COMPENSATION. Client shall pay Consultant a fee of $10,000 per month for Services rendered. Payment shall be made within 30 days of receipt of Consultant's invoice.

4. CONFIDENTIALITY. Consultant acknowledges that during the engagement, Consultant may have access to confidential information. Consultant agrees to maintain the confidentiality of all such information.

5. INTELLECTUAL PROPERTY. All materials developed by Consultant shall be the property of Client. Consultant assigns all right, title, and interest in such materials to Client.

6. TERMINATION. Either party may terminate this Agreement with 30 days' written notice. Client shall pay Consultant for Services performed through the termination date.

7. GOVERNING LAW. This Agreement shall be governed by the laws of the State of Delaware.

8. LIMITATION OF LIABILITY. Consultant's liability shall be limited to the amount of fees paid by Client under this Agreement.

9. INDEMNIFICATION. Client shall indemnify Consultant against all claims arising from use of materials provided by Client.

10. ENTIRE AGREEMENT. This Agreement constitutes the entire understanding between the parties and supersedes all prior agreements.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first above written.
"""


class LegalTermsChecker:
    """Agent that checks for problematic legal terms and clauses in contracts."""

    def run(self, contract_text):
        system_prompt = """
        You are a legal expert specializing in contract law. Analyze the contract for potentially problematic legal terms,
        clauses, or language that could create legal issues or disputes. Focus on liability, rights, obligations,
        and ambiguous language.
        """
        user_prompt = f"Analyze this contract for problematic legal terms and clauses:\n\n{contract_text}"
        agent_outputs["legal"]  = call_openai(system_prompt, user_prompt)

class ComplianceValidator:
    """Agent that validates regulatory and industry compliance of contracts."""
    def run(self, contract_text):
        system_prompt = """
        You are a compliance expert specializing in regulatory requirements across industries. Analyze the contract for potential compliance issues related to data privacy, labor laws, industry-specific regulations, and standard business practices.
        """
        user_prompt = f"Analyze this contract for regulatory and industry compliance issues:\n\n{contract_text}"
        agent_outputs["compliance"] = call_openai(system_prompt, user_prompt)

class FinancialRiskAssessor:
    """Agent that assesses financial risks and liabilities in contracts."""
    def run(self, contract_text):
        system_prompt = """ 
        You are a financial analyst specializing in contract risk assessment. Analyze the contract for financial risks, liability exposure, payment terms issues, and potential financial implications that could negatively impact a business.
        """
        user_prompt = f"Analyze this contract for financial risks and liabilities:\n\n{contract_text}"
        agent_outputs["financial"] = call_openai(system_prompt, user_prompt)


class SummaryAgent:
    """Agent that synthesizes findings from all specialized agents."""
    def run(self, contract_text, inputs):
        system_prompt = """
        You are a senior contract analyst skilled at synthesizing expert insights into clear, actionable business recommendations.
        """
        legal_findings = inputs.get("legal", "No legal analysis provided.")
        compliance_findings = inputs.get("compliance", "No compliance analysis provided.")
        financial_findings = inputs.get("financial", "No financial analysis provided.")
        print("Summary Agent synthesizing findings...")
        combined_prompt = (
            f"Contract:\n{contract_text}\n\n"
            f"Here are the expert analyses:\n\n"
            f"LEGAL ANALYSIS:\n{inputs['legal']}\n\n"
            f"COMPLIANCE ANALYSIS:\n{inputs['compliance']}\n\n"
            f"FINANCIAL ANALYSIS:\n{inputs['financial']}\n\n"
            "Please synthesize these analyses into a comprehensive contract assessment report with the following sections:\n"
            "1. Executive Summary\n"
            "2. Key Legal Concerns\n"
            "3. Compliance Issues\n"
            "4. Financial Risks\n"
            "5. Recommended Actions\n\n"
            "The report should be concise, actionable, and highlight the most critical findings."
        )
        return call_openai(system_prompt, combined_prompt)


def analyze_contract(contract_text):
    legal_agent = LegalTermsChecker()
    compliance_agent = ComplianceValidator()
    financial_risk = FinancialRiskAssessor()

    theards = []

    theards.append(threading.Thread(target=legal_agent.run, args=(contract_text,)))
    theards.append(threading.Thread(target=compliance_agent.run, args=(contract_text,)))
    theards.append(threading.Thread(target=financial_risk.run, args=(contract_text,)))

    for thread in theards:
        thread.start()
    for thread in theards:
        thread.join()


    summary_agent = SummaryAgent()
    print(agent_outputs)
    summary = summary_agent.run(contract_text, agent_outputs)
    print(f"✅ All agents have completed their tasks and the summary is generated.\n {summary}")

if __name__ == "__main__":
    analyze_contract(contract_text)

