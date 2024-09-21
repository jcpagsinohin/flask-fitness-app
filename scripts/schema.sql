CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  birthday DATE NOT NULL,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
  updated_at TIMESTAMP DEFAULT NOW()
)

CREATE TABLE IF NOT EXISTS exercises (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  muscle_group_id INTEGER REFERENCES muscle_groups(id)
)

CREATE TABLE IF NOT EXISTS muscle_groups (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
)

CREATE TABLE IF NOT EXISTS sessions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW(),
    ended_at TIMESTAMP NOT NULL
)

CREATE TABLE workout_logs (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    session_id INT REFERENCES sessions(id),
    exercise_id INT REFERENCES exercises(id),
    sets INT NOT NULL
)

CREATE TABLE IF NOT EXISTS workout_sets (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    workout_log_id INT REFERENCES workout_logs(id),
    reps INT NOT NULL,
    set_number INT NOT NULL,
    weight_kg DECIMAL(5,2) NOT NULL,
)
