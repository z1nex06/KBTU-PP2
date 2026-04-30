DROP TABLE IF EXISTS phones;
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS groups;

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO groups(name) VALUES
('Family'), ('Work'), ('Friend'), ('Other');

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    surname VARCHAR(50),
    email VARCHAR(100),
    birthday DATE,
    group_id INT REFERENCES groups(id)
);

CREATE TABLE phones (
    id SERIAL PRIMARY KEY,
    contact_id INT REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20),
    type VARCHAR(10) CHECK (type IN ('home','work','mobile'))
);