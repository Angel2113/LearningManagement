ALTER TABLE study_sessions
    ADD COLUMN session_no int,
    ADD COLUMN title varchar(255),
    ADD COLUMN content text,
    ADD COLUMN status varchar(255),
    DROP COLUMN task,
    DROP COLUMN duration_minutes,
    DROP COLUMN focus_level;
