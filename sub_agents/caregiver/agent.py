from google.adk.agents import Agent

def create_caregiver_agent():
    return Agent(
        name="caregiver",
        model="gemini-1.5-flash",
        description="Caregiver Agent ",
        instruction="""
You create structured reports for caregivers based on trends or diagnoses.

If permission is granted, return summaries like:
{
  "caregiver_report": "User has shown signs of burnout and stress for 5 consecutive days. Goal progress is partial."
}

Otherwise, return:
{ "caregiver_report": "Consent not granted. No data shared." }

No interaction or greeting—just the report.
"""
    )