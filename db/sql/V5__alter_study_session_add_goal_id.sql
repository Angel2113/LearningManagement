ALTER TABLE study_sessions
ADD COLUMN goal_id UUID;

ALTER TABLE study_sessions
ADD CONSTRAINT fk_study_sessions_goals
FOREIGN KEY (goal_id)
REFERENCES goals(id);
