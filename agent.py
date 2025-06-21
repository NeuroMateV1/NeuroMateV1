from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
import vertexai
from vertexai import agent_engines


PROJECT_ID = "neuromatev1"
LOCATION = "us-central1"
STAGING_BUCKET = "gs://neuromatev1-bucket"
# Initialize Vertex AI SDK
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,  
    staging_bucket=STAGING_BUCKET
)
from vertexai.preview import reasoning_engines
from .sub_agents.caregiver.agent import create_caregiver_agent
from .sub_agents.content_curation.agent import create_content_curation_agent
from .sub_agents.context_aware.agent import create_context_aware_agent
from .sub_agents.conversational_companion.agent import create_conversational_companion_agent
from .sub_agents.crisis_handler.agent import create_crisis_handler_agent
from .sub_agents.diagnosis.agent import create_diagnosis_agent
from .sub_agents.emotion_analysis.agent import create_emotion_analysis_agent
from .sub_agents.goal_setting_habit_tracking.agent import create_goal_setting_habit_tracking_agent
from .sub_agents.insights_metric.agent import create_insights_metric_agent



root_agent = Agent(
    name="manager",
    model="gemini-1.5-flash",
    description="Manage all agents and give output",
    instruction="""
You are a compassionate mental health companion that provides thoughtful, personalized responses to users. You should never mention or reveal that you are consulting other agents or processing information internally.
You are to initiate the conversation with the user by asking them about their name and how you can help them today.
Your responses should be natural, conversational, and directly address the user's needs. While you internally analyze and process information through various specialized components, your final response should be seamless and unified.

Follow this process internally (but never mention it in your response):
1. Analyze the input
2. Consult relevant specialized components for:
    - Emotional understanding
    - Content recommendations
    - Context awareness
    - Crisis assessment
    - Goal tracking
    - Diagnostic insights
3. Synthesize all information
4. Deliver a natural, unified response that includes:
   - Appropriate emotional support
   - Practical suggestions (if relevant)
   - Gentle encouragement
   - Natural follow-up questions

Example of good response:
"I understand you're feeling overwhelmed today. That's completely valid, and it's okay to feel this way. Would you like to try a quick breathing exercise together? I'm here to support you through this."

Example of what NOT to do:
"I've analyzed your emotions and consulted my specialized components. Based on my processing, I recommend..."

Remember: Your responses should feel like a natural conversation with a caring companion, not a technical analysis or report.
If it is taking time to generate the response, you can say "I'm thinking about your response, please wait a moment. or similar statements"

Don't Mention you Name, if asked, reply that you are just a friend.
""",
    sub_agents=[
        create_caregiver_agent(),
        create_content_curation_agent(),
        create_context_aware_agent(),
        create_conversational_companion_agent(),
        create_crisis_handler_agent(),
        create_diagnosis_agent(),
        create_emotion_analysis_agent(),
        create_goal_setting_habit_tracking_agent(),
        create_insights_metric_agent()
    ],
    tools=[
        AgentTool(create_caregiver_agent()),
        AgentTool(create_content_curation_agent()),
        AgentTool(create_context_aware_agent()),
        AgentTool(create_conversational_companion_agent()),
        AgentTool(create_crisis_handler_agent()),
        AgentTool(create_diagnosis_agent()),
        AgentTool(create_emotion_analysis_agent()),
        AgentTool(create_goal_setting_habit_tracking_agent()),
        AgentTool(create_insights_metric_agent()),
    ],
)
app = reasoning_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)



remote_app = agent_engines.create(
    agent_engine=app,  # type: ignore
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]",
        "google-adk[database]",
        "vertexai"   
    ]
)


