from fastapi import Request
from sqlalchemy.orm import Session
from app.models.Goals import Goals
from app.schemas.goals_schema import CreateGoalSchema, UpdateGoalSchema
import uuid
import logging


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

def create_goal(request: Request, db: Session, goal: CreateGoalSchema) -> dict:
    """
    Create a new goal in database. (CREATE)
    :param db: Database session
    :param goal: CreateGoalSchema
    :return: A dictionary with the result message
    """
    # TODO: Is it necessary to validate if the goal already exists?
    user_id = request.state.user_id
    new_goal = Goals(
        id = str(uuid.uuid4()),
        user_id = user_id,
        title = goal.title,
        current_level = goal.current_level,
        resources = goal.resources,
        target_date = goal.target_date,
        days_per_week = goal.days_per_week,
        hours_per_day = goal.hours_per_day,
        status = goal.status,
    )
    db.add(new_goal)
    db.commit()
    db.refresh(new_goal)
    return {"message": "Goal created successfully"}

def get_all_goals(db: Session, user_id: str):
    """
    Get all the goals for a user.
    :param db: Database session
    :param user_id:  user id
    :return: A list of goals for specific user
    """
    #user_id = uuid.UUID(user_id).hex
    logger.info(f"Getting goals for user: {user_id}")
    goals = db.query(Goals).filter(Goals.user_id == user_id).all()
    return [
        {
            "id": goal.id,
            "title": goal.title,
            "current_level": goal.current_level,
            "resources": goal.resources.split(","),
            "target_date": goal.target_date,
            "days_per_week": goal.days_per_week,
            "hours_per_day": goal.hours_per_day,
            "status": goal.status
        }
        for goal in goals
    ]

def get_goal(db: Session, goal_id: str) -> Goals:
    """
    Get task by id
    :param db: Database session
    :param goal_id: Goal id
    :return: return the goal
    """
    goal = db.query(Goals).filter(Goals.id == goal_id).first()
    return goal if goal else None

def update_goal(db: Session, goal_id: str, update: UpdateGoalSchema) -> dict:
    """
    Update a goal.
    :param db: Database session
    :param goal_id: Goal id
    :param update: data to update
    :return: a result message
    """
    # Get the goal
    goal = get_goal(db = db, goal_id = goal_id)
    if not goal:
        return {"message": "Goal not found"}

    goal.title = update.title if update.title else goal.title
    goal.current_level = update.current_level if update.current_level else goal.current_level
    goal.resources = update.resources if update.resources else goal.resources
    goal.target_date = update.target_date if update.target_date else goal.target_date
    goal.days_per_week = update.days_per_week if update.days_per_week else goal.days_per_week
    goal.hours_per_day = update.hours_per_day if update.hours_per_day else goal.hours_per_day
    goal.status = update.status if update.status else goal.status

    db.commit()
    db.refresh(goal)
    return {"message": "Goal updated successfully"}

def delete_goal(db: Session, goal_id) -> dict:
    """
    Delete a goal.
    :param db: Database session
    :param goal_id:  Goal id
    :return: a result message
    """
    goal = get_goal(db = db, goal_id = goal_id)
    if not goal:
        return {"message": "Goal not found"}
    db.delete(goal)
    db.commit()
    return {"message": "Goal deleted successfully"}