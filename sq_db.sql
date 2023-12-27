CREATE TABLE IF NOT EXISTS versions (
id integer PRIMARY KEY AUTOINCREMENT,
ip text NOT NULL,
config text NOT NULL,
revision text NOT NULL
)