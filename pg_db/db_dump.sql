CREATE TABLE IF NOT EXISTS person (
    id uuid PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT DEFAULT ''
);