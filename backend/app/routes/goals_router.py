from fastapi import APIRouter, Depends, Request
from typing import Annotated
from app.CRUD import goals_crud, session_crud
from app.database import get_db
from sqlalchemy.orm import Session
from app.routes.auth_router import get_current_user, security
from app.schemas.goals_schema import CreateGoalSchema, UpdateGoalSchema
import logging
import re

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

goals_router = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]

@goals_router.get("/goals", tags=["goals"], dependencies=[Depends(security)])
async def get_all_goals(request: Request, db: Session = Depends(get_db)):
    """
    Get all goals for user
    :param user_id: user id
    :param db: Database session
    :return: a list of goals
    """
    user_id = request.state.user_id
    return goals_crud.get_all_goals(db, user_id)

@goals_router.get("/goals/{goal_id}", tags=["goals"], dependencies=[Depends(security)])
async def get_goal(request: Request, goal_id: str, db: Session = Depends(get_db)):
    """
    Get a goal by id (READ)
    :param goal_id: goal id
    :param db: database session
    :return: a goal
    """
    # Get goal
    goal = goals_crud.get_goal(db, goal_id)
    user_id = request.state.user_id

    # Verify if the goal exists
    if not goal:
        return {"message": "Hey dude, this goal doesn't exist"}

    # Verify if the user is the correct one
    if str(goal.user_id) != str(user_id):
        return {"message": "Hey dude, this goal doesn't belong to you"}

    return goal

@goals_router.post("/goals", tags=["goals"], dependencies=[Depends(security)])
async def create_goal(request: Request, goal: CreateGoalSchema, db: Session = Depends(get_db)):
    """
    Create a goal (CREATE)
    :param goal: Create schema
    :param db: Database session
    :return: Result message
    """
    logger.info(f"Creating goal: {goal}")

    # Create Goal
    goal = goals_crud.create_goal(request, db, goal)
    goal_id = goal.id
    text = goal.ia_suggestion

    #Get Sessions
    session_pattern = r"### Session \d+: .*"
    sessions = re.split(session_pattern, text)
    session_titles = re.findall(session_pattern, text)

    session_list = [
        {
            'session_no': i + 1,
            "title": session_titles[i].strip(),
            "content": sessions[i + 1].strip()
        }
        for i in range(len(session_titles))
    ]
    logger.info(f'No. Sessions: {len(session_list)}')
    logger.info(f'Session List: {session_list}')
    logger.info(f'Goal id: {goal_id}')
    if goal:
        for session in session_list:
            return {"message": "Goal created successfully"}


    return {"message": "Error creating the goal"}

@goals_router.put('/goals/{goal_id}', tags=["goals"], dependencies=[Depends(security)])
async def update_goal(request: Request, goal_id: str, updates: UpdateGoalSchema, db: Session = Depends(get_db)):
    """
    Update a goal (UPDATE)
    :param request: Request object, contains the user id
    :param goal_id: goal id
    :param updates: Update schema, data to be updated
    :param db: Database session
    :return: Result message
    """
    logger.info(f"Updating goal: {goal_id}")
    goal = goals_crud.get_goal(db, goal_id)
    user_id = request.state.user_id

    logger.info(f"Goal: {goal}")


    # Verify if the goal exists
    if goal is None:
        return {"message": "Goal not found"}
    # Verify if the user is the correct one
    if str(goal.user_id) != str(user_id):
        return {"message": "Hey dude, you can't update this goal"}

    return goals_crud.update_goal(db, goal_id, updates)

@goals_router.delete("/goals/{goal_id}", tags=["goals"], dependencies=[Depends(security)])
async def delete_goal(request: Request, goal_id: str, db: Session = Depends(get_db)):
    goal = goals_crud.get_goal(db, goal_id)
    user_id = request.state.user_id

    # Verify if the goal exists
    if goal is None:
        return {"message": "Goal not found"}
    # Verify if the user is the correct one
    if str(goal.user_id) != str(user_id):
        return {"message": "Hey dude, this goal doesn't belong to you"}

    return goals_crud.delete_goal(db, goal_id)

