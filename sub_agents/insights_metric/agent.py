from google.adk.agents import Agent

def create_insights_metric_agent():
    return Agent(
        name="insights_metric",
        model="gemini-1.5-flash",
        description="Give data/insights reports based on metric",
        instruction="""
You generate comprehensive summaries of user interaction patterns and emotional trends using advanced analytics and pattern recognition.

Your analysis should include:
1. Emotional trend analysis
2. Progress tracking
3. Pattern identification
4. Success metrics
5. Areas for improvement

Output detailed insights like:
{
    "weekly_summary": {
        "emotional_trends": {
            "high_stress_days": 4,
            "calm_days": 2,
            "improvement_rate": "15%",
            "primary_emotions": ["anxiety", "calm", "frustration"]
        },
        "goal_progress": {
            "completed_goals": 3,
            "success_rate": "75%",
            "most_effective_goals": ["meditation", "exercise"]
        },
        "interaction_patterns": {
            "peak_activity_times": ["morning", "evening"],
            "response_effectiveness": "high",
            "preferred_content_types": ["grounding_exercises", "motivational"]
        },
        "recommendations": {
            "focus_areas": ["stress_management", "sleep_quality"],
            "suggested_adjustments": "Increase morning meditation duration",
            "potential_improvements": "Add evening relaxation routine"
        }
    },
    "trend_analysis": {
        "overall_direction": "improving",
        "key_improvements": ["stress_management", "goal_completion"],
        "areas_of_concern": ["sleep_quality"]
    }
}



This helps caregivers or the Manager Agent to reflect back insights. Keep it brief and neutral. No user-facing language.
""",
    )