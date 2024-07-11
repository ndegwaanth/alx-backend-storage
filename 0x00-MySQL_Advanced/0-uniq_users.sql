-- script that create table users

CREATE TABLE users IF NOT EXISTS (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);