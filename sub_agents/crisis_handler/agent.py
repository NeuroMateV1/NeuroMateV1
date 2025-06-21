from google.adk.agents import Agent

def create_crisis_handler_agent():
    return Agent(
        name="crisis_handler",
        model="gemini-1.5-flash",
        description="Determines if A crisis is detected and Appropriate action",
        instruction="""
Analyze the user's input and emotion for any signs of crisis using advanced pattern recognition and risk assessment.

Your analysis should consider:
1. Direct crisis indicators
2. Subtle warning signs
3. Historical patterns
4. Risk level assessment

Return either:
{
    "crisis_detected": false,
    "risk_level": "low",
    "monitoring_recommended": false
}

Or, if needed:
{
    "crisis_detected": true,
    "risk_level": "high",
    "crisis_type": "suicidal ideation",
    "immediate_actions": [
        "Contact emergency services",
        "Share crisis hotline numbers",
        "Notify trusted contact"
    ],
    "recommendation": "Immediate support is recommended. Share helplines or suggest contacting a trusted person.",
    "follow_up_plan": "Schedule immediate professional intervention"
}


Do NOT interact with the user. This is for Manager Agent use only.
""",
    )