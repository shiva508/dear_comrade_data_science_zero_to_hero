# Course Overview
### This course is designed to equip you with the knowledge and skills to develop intelligent AI agents that can interact with the real world, manage their internal processes, access and utilize diverse data sources, and continuously improve their performance.
## Course Topics
- **Extending Agents with Tools**
  - Understanding how LLM-based agents utilize external tools to broaden their capabilities and interact with real-world systems.
  - Learning how tools empower agents to perform actions (e.g., check weather, query databases, perform calculations) beyond generating text.
  - Exploring Function Calling as a dependable method for models to determine when and how to employ tools, ensuring structured outputs for external actions.

- **Structured Outputs**
  - Producing structured, machine-readable outputs (e.g., JSON) for subsequent processing.
  - Recognizing the importance of structured outputs for initiating code, APIs, and other agents, moving beyond free-form text.
  - Utilizing Pydantic models in Python to define data schemas and enforce type validation for reliable outputs.

- **Agent State Management**
  - Introducing the concept of state as internal context that exists solely during a single agent execution.
  - Understanding that while LLMs are inherently stateless, agents require temporary state to handle complexity and monitor progress during a task.
  - Employing state machines as a clear, modular approach to managing this internal state, ensuring predictable and testable execution.

- **Short-Term Memory**
  - Enabling agents to recall interactions across multiple turns within the same session (thread).
  - Learning that memory is an abstraction achieved by feeding previous interactions back into the agent's prompt to maintain context.
  - Exploring strategies such as conversation history, sliding windows, and simple summarization, balancing context with token costs and performance.

- **External APIs**
  - Applying external API integrations to extend agent functionality and incorporate live data into agent workflows.
  - Understanding that APIs act as the link between an agent's reasoning and the external environment, facilitating real-world actions.
  - Addressing challenges associated with external APIs, including authentication, non-determinism, and the necessity for robust error handling and observability.

- **Web Search Agents**
  - Developing an agent capable of performing web searches via an API and integrating the results into LLM responses.
  - Recognizing that web search grants agents access to real-time, unstructured data, counteracting hallucinations by grounding responses in verifiable evidence.
  - Focusing on effectively interpreting raw search results, filtering relevant information, and citing sources.

- **Interacting with Databases**
  - Developing an agent that interacts with databases to retrieve and update structured information.
  - Understanding how agents can engage with relational (SQL), NoSQL, and vector databases.
  - Learning about Text2SQL agents that convert natural language into database queries, and the role of vector databases in semantic search for "similar meaning" queries.

- **Agentic RAG**
  - Building a basic RAG agent that operates autonomously, retrieving relevant documents and generating an answer.
  - Exploring how Agentic RAG goes beyond static retrieval by allowing agents to reason about retrieved content, reflect, and attempt again if necessary.
  - Understanding that this approach involves planning, evaluating retrieved information, reformulating queries, and adapting strategies for dynamic retrieval.

- **Long-Term Memory**
  - Constructing an agent that retains information across different sessions.
  - Learning how long-term memory enables agents to personalize interactions, avoid repetition, and improve through experience over time.
  - Considering semantic (facts), episodic (experiences), and procedural (behavior) memory, along with aspects of storage, retrieval, privacy, and relevance.

- **Evaluating Agents**
  - Evaluating the performance of AI agents across various dimensions, from final outputs to internal reasoning steps.