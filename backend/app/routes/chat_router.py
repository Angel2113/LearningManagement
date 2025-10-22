from fastapi import APIRouter, Depends, Request
from fastapi.params import Depends
from app.schemas.goals_schema import CreateGoalSchema
from app.utils.local_ai import AIClient as local_ai
from app.utils.remote_ai import AIClient as remote_ai
from app.routes.auth_router import get_current_user, security
from fastapi import APIRouter
from typing import Annotated
import datetime
import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

chat_router = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]

load_dotenv()

def get_ai_env():
    return os.getenv("AI_ENV")

def get_ai_model():
    return os.getenv("AI_MODEL")


PROMPT = ("You are an expert learning coach. I will provide you with some parameters about my study goal, "
            "and I want you to create a detailed study plan."
            "Title:{title} "
            "Current Level: {current_level} "
            "Target Date: {target_date} "
            "Current Date: {current_date} "
            "Days per Week: {days_per_week} "
            "Hours per Day: {hours_per_day} "
            "Resources: {resources} "
            "--- Output Structure: "
            "Generate a study plan based on the provided parameters. "
            "The output must be explicitly divided into sessions and content to be covered in each one. "
            "For each study session, include the following: "
            "- Session: A clear heading for the session (e.g., 'Session 1: Introduction to Machine Learning'). "
            "- Content: A detailed list of topics to be covered in that session. "
            "- Bibliographic Material & Links: A list of specific chapters, articles, or videos from the provided "
            "resources, along with direct links to them. Also, feel free to suggest other high-quality, free resources "
            "if they are relevant. The output should be explicitly structured as follows: ## Study Plan for [title] "
            "### Session 1: [Topic] - "
            "Content: - [List of topics] - Bibliographic Material & Links: - "
            "[Resource 1, with link] - [Resource 2, with link] Session 2: [Topic] - Content: - [List of topics] - "
            "Bibliographic Material & Links: - [Resource 1, with link] - [Resource 2, with link] --- "
            "### Session 2: [Topic] ... and so on."
          "The final output should be a single string that can be easily split into individual sessions.")

@chat_router.post('/chat', tags=["chat"], dependencies=[Depends(security)])
async def get_chat(request: Request, goal:CreateGoalSchema):
    logger.info(f"Getting chat: {goal}")
    prompt = PROMPT.replace("{title}", goal.title)
    prompt = prompt.replace("{current_level}", str(goal.current_level))
    prompt = prompt.replace("{resources}", str(goal.resources))
    prompt = prompt.replace("{current_date}", str(datetime.date.today()))
    prompt = prompt.replace("{target_date}", str(goal.target_date))
    prompt = prompt.replace("{days_per_week}", str(goal.days_per_week))
    prompt = prompt.replace("{hours_per_day}", str(goal.hours_per_day))

    agent = None
    env = 'local'
    model = 'llama3.2:latest'
    if env == "local":
        agent = local_ai(model=model)
    elif env == "remote":
        #agent = remote_ai()
        pass
    response = agent.chat(prompt)
    logger.info(f"Response: {response}")
    return {"reply":  response}



