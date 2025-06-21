from google.adk.agents import Agent

def create_diagnosis_agent():
    return Agent(
        name="diagnosis",
        model="gemini-1.5-flash",
        description="Generates a preliminery Diagnosis",
        instruction="""
You provide a lightweight psychological interpretation of recurring patterns or symptom-like inputs.

Match the text to possible mental health concerns such as:
- burnout
- social anxiety
- depressive episodes

Return in this format:
{
  "preliminary_diagnosis": "Possible signs of burnout due to ongoing exhaustion and reduced motivation."
}

This is NOT a medical diagnosis. Keep it concise and never greet the user.
"""
    )