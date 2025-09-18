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
            "Parameters:"
            "Title: {Title}"
            "Current level: {current_level}"
            "Resources: {resources}"
            "Current date: {current_date}"
            "Target date: {target_date}"
            "Available days per week to study: {days_per_week}"
            "Hours per day: {hours_per_day}"
            "Instructions:"
             "Calculate the total number of study sessions based on the available time until the target date."
             "Break down the study plan into weekly goals and daily sessions."
             "Assign specific resources (books, videos, exercises, etc.) to each session."
             "Provide learning strategies and tips adapted to my current level (e.g., active recall, spaced repetition, practice exercises)."
             "Include checkpoints for review and progress tracking."
             "Present the plan in a clear and organized format, easy to follow."
            "Output:"
             "Total number of sessions"
            "Weekly breakdown (with dates)"
            "Daily session details"
            "Learning tips and best practices")

@chat_router.post('/chat', tags=["chat"], dependencies=[Depends(security)])
async def get_chat(request: Request, goal:CreateGoalSchema):
    logger.info(f"Getting chat: {goal}")
    prompt = PROMPT.replace("{title}", goal.title)
    prompt = prompt.replace("{current_level}", goal.current_level)
    prompt = prompt.replace("{resources}", str(goal.resources))
    prompt = prompt.replace("{current_date}", str(datetime.date.today()))
    prompt = prompt.replace("{target_date}", str(goal.target_date))
    prompt = prompt.replace("{days_per_week}", str(goal.days_per_week))
    prompt = prompt.replace("{hours_per_day}", str(goal.hours_per_day))

    logger.info(f"Prompt: {prompt}")
    logger.info(f"Env: {get_ai_env()}")
    logger.info(f"Model: {get_ai_model()}")
    agent = None
    env = 'remote'
    model = 'llama3.2:latest'
    if env == "local":
        agent = local_ai(model=model)
    elif env == "remote":
        agent = remote_ai()

    return agent.chat(prompt)



