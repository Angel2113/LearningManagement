-- Goals table
CREATE TABLE goals (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    current_level VARCHAR(255),
    resources VARCHAR(255),
    target_date DATE,
    days_per_week INT,
    hours_per_day INT,
    status VARCHAR(20) NOT NULL DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);