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
- users: user_id PK, user_name, password_hash, email UNIQUE
- habits: habit_id PK, habit_name, user_id FK, frequency, interval_count, created_date
- completions: completion_id PK, habit_id FK, date_checked, UNIQUE (habit_id, date_checked)
- Principle: store facts, derive state. Streaks, "checked today," and completion % are calculated from completions, never stored.
- Un-checking a habit = deleting the completion row.

## Build order
1. Skeleton: docker-compose (db, backend, frontend), schema.sql, GET /api/health doing SELECT 1, frontend shows the result.
2. Vertical slice: create a daily habit, list habits, mark done today (single hardcoded user, no auth).
3. One pytest test + GitHub Actions running it.
4. Streaks, then non-daily frequencies.
5. Analytics (weekly/monthly summaries, completion %).
6. Reminders/push notifications last.
7. Auth, AWS deployment, README (screenshot, live link, architecture diagram, setup steps).
