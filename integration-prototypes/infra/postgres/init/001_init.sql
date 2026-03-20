CREATE TABLE IF NOT EXISTS demo_items (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT NOT NULL
);

INSERT INTO demo_items (name, description)
VALUES
  ('alpha', 'seed row alpha'),
  ('beta', 'seed row beta'),
  ('gamma', 'seed row gamma')
ON CONFLICT DO NOTHING;
