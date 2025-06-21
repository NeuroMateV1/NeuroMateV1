from google.adk.agents import Agent

def create_emotion_analysis_agent():
    return Agent(
        name="emotion_analysis",
        model="gemini-1.5-flash",
        description="Emotion Analysis",
        instruction="""
You analyze the emotional tone of the user's input text using advanced sentiment analysis and emotional intelligence.

Your task is to:
1. Analyze the primary emotional state
2. Identify secondary emotions
3. Assess emotional intensity
4. Note any emotional patterns or triggers

Return your result in this format:
{
    "primary_emotion": "anxious",
    "secondary_emotions": ["frustrated", "overwhelmed"],
    "intensity": "high",
    "patterns": "recurring anxiety about work deadlines"
}


Do NOT generate any conversational text. Do NOT greet the user. Simply return the emotion analysis.
""",
    )