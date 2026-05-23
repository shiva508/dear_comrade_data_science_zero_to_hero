import os
import time
from typing import Any, List, Dict

class Agent:
    """
    A base class for our agents.
    While not strictly necessary for simple cases,
    it can be useful for defining common interfaces or utilities.
    """
    def __init__(self, name):
        self.name = name
        print(f"Agent '{self.name}' initialized.")
    def run(self, input_data:None):
        """
        A generic method to execute the agent's task.
        Specific agents will override this.
        """
        print(f"Agent '{self.name}' processing data {str(input_data)}.")
        raise NotImplementedError("Each agent must implement the 'execute' method.")


class ResearchAgent(Agent):

    """
    A base class for our research agents.
    """
    def run(self, query):
        print(f"Agent '{self.name}' processing data {str(query)}.")
        time.sleep(0.5)
        return f"Research for query: {query} found 3 points"

class SummarizerAgent(Agent):
    """Agent that summarizes information"""
    def run(self, text: str) -> str:
        print(f"📝 {self.name} summarizing text...")
        time.sleep(0.5)  # Simulate processing
        return f"Summary: {text.split(':', 1)[1][:30]}..."

class FactCheckerAgent(Agent):
    """Agent that verifies information"""
    suspicious_keywords = ["error", "uncertain", "debated"]
    def run(self, text: str) -> Dict:
        print(f"✓ {self.name} fact checking... {text}")
        flags = [kw for kw in self.suspicious_keywords if kw in text.lower()]

        time.sleep(0.5)  # Simulate verification
        return {
            "text": text,
            "accuracy": "high",
            "verified_claims": 3,
            "flags": flags,
        }
