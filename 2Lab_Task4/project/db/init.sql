CREATE TABLE IF NOT EXISTS links (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  url TEXT NOT NULL,
  category VARCHAR(100) DEFAULT 'General'
);

-- Опционально: добавим тестовые данные
INSERT INTO links (name, url, category) VALUES ('Google', 'https://google.com', 'Search');