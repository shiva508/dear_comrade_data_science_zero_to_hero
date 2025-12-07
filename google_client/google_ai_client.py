from google import genai

def prompt(message: str) -> str:
    client = genai.Client(api_key="")

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=message
    )
    return response.text

if __name__ == "__main__":
    user_input = "Explain the theory of relativity in simple terms."
    output = prompt(user_input)
    print("AI Response:", output)