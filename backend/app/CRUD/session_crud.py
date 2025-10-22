from fastapi import Request
from sqlalchemy.orm import Session
from app.models.Sessions import Sessions
import uuid
import logging


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

def create_session(request: Request, db: Session, session: Sessions, goal_id: str):
     user_id = request.state.user_id
     new_session = Sessions(
         id = str(uuid.uuid4()),
         session_no = session.session_no,
         title = session.title,
         content = session.content,
         status = 'new',
         user_id = user_id,
         goal_id = goal_id,
     )
     logger.info(f"Creating session: {session.session_no}")
     db.add(new_session)
     db.commit()
     db.refresh(new_session)
     return {"message": "New session created"}
