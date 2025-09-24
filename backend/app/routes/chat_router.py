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
            "### Week 1 Session 1: [Topic] - "
            "Content: - [List of topics] - Bibliographic Material & Links: - "
            "[Resource 1, with link] - [Resource 2, with link] Session 2: [Topic] - Content: - [List of topics] - "
            "Bibliographic Material & Links: - [Resource 1, with link] - [Resource 2, with link] --- "
            "### Week 2 Session 3: [Topic] ... and so on.")

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

    agent = None
    env = 'local'
    model = 'llama3.2:latest'
    if env == "local":
        agent = local_ai(model=model)
    elif env == "remote":
        #agent = remote_ai()
        pass

    example = (
        "Study Plan for Machine Learning\n"
        "\n"
        "Week 1\n"
        "Session 1: Introduction to Machine Learning\n"
        "- Content:\n"
        "  Overview of machine learning\n"
        "  Types of machine learning (supervised, unsupervised, reinforcement)\n"
        "  Basic concepts and terminology\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  Chapter 1: \"Introduction to Machine Learning\" from Python Crash Course book by Eric Matthes:\n"
        "    https://www.youtube.com/watch?v=0W4rjwqVgGk\n"
        "  Coursera's Machine Learning Specialization - Week 1: Introduction to Machine Learning:\n"
        "    https://www.coursera.org/learn/machine-learning/specialization/week/1\n"
        "\n"
        "Session 2: Supervised and Unsupervised Learning\n"
        "- Content:\n"
        "  Supervised learning (regression, classification)\n"
        "  Unsupervised learning (clustering, dimensionality reduction)\n"
        "  Basic algorithms for supervised and unsupervised learning\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  Chapter 2: \"Supervised Learning\" from Python Crash Course book by Eric Matthes:\n"
        "    https://www.realpython.com/python-supervised-learning/\n"
        "  Coursera's Machine Learning Specialization - Week 2: Supervised Learning:\n"
        "    https://www.coursera.org/learn/machine-learning/specialization/week/2\n"
        "\n"
        "Week 2\n"
        "Session 3: Reinforcement Learning and Neural Networks\n"
        "- Content:\n"
        "  Introduction to reinforcement learning\n"
        "  Basic concepts of neural networks (perceptrons, multilayer perceptrons)\n"
        "  Introduction to deep learning\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  Chapter 3: \"Reinforcement Learning\" from Python Crash Course book by Eric Matthes:\n"
        "    https://scikit-learn.org/stable/modules/neural_networkssupervised.html\n"
        "  Coursera's Machine Learning Specialization - Week 3: Reinforcement Learning and Neural Networks:\n"
        "    https://www.coursera.org/learn/machine-learning/specialization/week/3\n"
        "\n"
        "Session 4: Model Evaluation, Overfitting, and Regularization\n"
        "- Content:\n"
        "  Evaluation metrics for machine learning models (accuracy, precision, recall)\n"
        "  Techniques to prevent overfitting\n"
        "  Introduction to regularization techniques\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  Chapter 4: \"Model Evaluation\" from Python Crash Course book by Eric Matthes:\n"
        "    https://www.realpython.com/python-regularization/\n"
        "  Coursera's Machine Learning Specialization - Week 4: Model Evaluation, Overfitting, and Regularization:\n"
        "    https://www.coursera.org/learn/machine-learning/specialization/week/4\n"
        "\n"
        "Week 3\n"
        "Session 5: Advanced Topics in Machine Learning\n"
        "- Content:\n"
        "  Introduction to transfer learning and domain adaptation\n"
        "  Basic concepts of ensemble methods (bagging, boosting)\n"
        "  Techniques for handling missing data\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  Chapter 5: \"Advanced Topics in Machine Learning\" from Python Crash Course book by Eric Matthes:\n"
        "    https://www.realpython.com/python-advanced-machine-learning/\n"
        "  Coursera's Machine Learning Specialization - Week 5: Advanced Topics in Machine Learning:\n"
        "    https://www.coursera.org/learn/machine-learning/specialization/week/5\n"
        "\n"
        "Session 6: Final Project\n"
        "- Content:\n"
        "  Final project idea and preparation\n"
        "  Review of key concepts learned throughout the course\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  [Your own notes and materials for this session]\n"
        "  [Additional resources as needed]\n"
        "\n"
        "Session 7: Practicing and Refining Your Skills\n"
        "- Content:\n"
        "  Practice applying machine learning concepts to real-world problems\n"
        "  Refine your skills through projects and exercises\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  [Your own notes and materials for this session]\n"
        "  [Additional resources as needed]\n"
        "\n"
        "Session 8: Review and Assessment\n"
        "- Content:\n"
        "  Review of key concepts learned throughout the course\n"
        "  Assessment of your understanding through quizzes or exams\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  [Your own notes and materials for this session]\n"
        "  [Additional resources as needed]\n"
        "\n"
        "Session 9: Real-World Applications\n"
        "- Content:\n"
        "  Overview of real-world applications of machine learning (e.g., medical imaging, natural language processing)\n"
        "  Case studies and examples\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  [Real-world applications and case studies]\n"
        "  [Additional resources as needed]\n"
        "\n"
        "Session 10: Final Project Presentation\n"
        "- Content:\n"
        "  Present your final project to the class or online community\n"
        "  Review of key concepts learned throughout the course\n"
        "\n"
        "Bibliographic Material & Links:\n"
        "  [Your own notes and materials for this session]\n"
        "  [Additional resources as needed]\n"
    )
    #response = agent.chat(prompt)
    #logger.info(f"Response: {response}")
    return {"reply":  example}



