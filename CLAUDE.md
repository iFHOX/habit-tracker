# How to work with me
- Give direct, honest feedback without sugarcoating.
- Skip unnecessary encouragement.
- Engage critically and point out flaws in my thinking.
- My working style: make it work first, make it clean later.
- When I'm genuinely learning, give hints instead of full solutions. If I'm on a deadline, I'll ask for the complete answer directly.
- Context: I'm a CS student building this as a portfolio project for internship interviews, so I need to be able to defend every line.
- Follow the build order below. Don't jump ahead to auth, AWS, reminders, or analytics.

# Project: Habit tracker
Stack: Flask + PostgreSQL backend, React + TypeScript (Vite) frontend, Docker Compose. Pytest + Vitest. GitHub Actions CI. AWS deployment later.

## Data model
Reviewed and approved (week 1). Relationships: one user has 0..* habits; one habit has 0..* completions.

- users: user_id PK, user_name, password_hash, email UNIQUE
- habits: habit_id PK, habit_name, user_id FK -> users, frequency, interval_count, created_date
- completions: completion_id PK, habit_id FK -> habits, date_checked
  - UNIQUE (habit_id, date_checked) — a table constraint, not a column
- Completions store a DATE, not a timestamp: one check per habit per day, which is what streaks and completion % count.
- Principle: store facts, derive state. Streaks, "checked today," and completion % are calculated from completions, never stored.
- Un-checking a habit = deleting the completion row.
- Only daily habits for now; frequency + interval_count leave room for other schedules later.

Open decisions (settle when writing schema.sql):
- ON DELETE behavior for each FK: deleting a habit -> its completions? deleting a user -> their habits? (look into ON DELETE CASCADE)
- Whose "today" date_checked uses: the client's local date, or a timezone stored on the user.

## Build order
Numbering follows my mentor's plan. Current target: step 3 (due this week).

1. ~~Pick the backend~~ — done: Flask.
2. ~~Sketch the data model~~ — done and reviewed (see above). Redraw the ER diagram cleanly for the README later.
3. Skeleton (current):
   - Repo with /backend (Flask) and /frontend (React + TS, Vite).
   - docker-compose.yml with three services: db (postgres image), backend, frontend.
   - schema.sql with the three tables, written by me from the model above, loaded into Postgres on startup.
   - GET /api/health runs SELECT 1 against the database and returns JSON.
   - Frontend calls that route and shows the result.
   - Done when `docker compose up` gives a page that says the database is connected.
4. Vertical slice: create a daily habit, list habits, mark done today (single hardcoded user, no auth).
5. One pytest test + GitHub Actions workflow running it.

Don't touch AWS, reminders, custom intervals, or analytics until step 4 works.

Later, in this order:
6. Streaks, then non-daily frequencies.
7. Analytics (weekly/monthly summaries, completion %).
8. Reminders/push notifications.
9. Auth, AWS deployment, README (screenshot, live link, architecture diagram, setup steps).
