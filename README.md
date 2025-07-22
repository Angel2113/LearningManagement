# Learning Management 

A productivity tracking web application designed for students and professionals who want to monitor their study or work sessions, set personal goals, and receive AI-powered recommendations to improve focus and habits.

## Installation

Clone this repository
```bash
    git clone https://github.com/Angel2113/LearningManagement
```

## Usage 


```mermaid

erDiagram
    USERS {
        UUID id
        VARCHAR name
        VARCHAR email
        VARCHAR password_hash
        TIMESTAMP created_at
    }

    SESSIONS {
        UUID id
        UUID user_id
        TIMESTAMP start_time
        TIMESTAMP end_time
        TEXT notes
    }

    GOALS {
        UUID id
        UUID user_id
        VARCHAR title
        TEXT description
        DATE target_date
        BOOLEAN completed
    }

    USERS ||--o{ SESSIONS : has
    USERS ||--o{ GOALS : sets
    USERS ||--o{ RECOMMENDATIONS : receives
```

```mermaid
flowchart TD
    subgraph Frontend [React + Shadcn UI]
        A1[Login / Register Page]
        A2[Dashboard Page]
        A3[Session Tracker]
        A4[Goals Manager]
        A5[Recommendations View]
    end

    subgraph Backend [FastAPI]
        B1[Auth API]
        B2[Session API]
        B3[Goals API]
        B4[Recommendation Engine]
        B5[PostgreSQL DB]
    end

    A1 --> B1
    A2 --> B2
    A3 --> B2
    A4 --> B3
    A5 --> B4

    B1 --> B5
    B2 --> B5
    B3 --> B5
    B4 --> B5
```

