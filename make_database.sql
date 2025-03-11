ATTACH DATABASE 'nypd_date.db' AS mydb2;

CREATE TABLE mydb2.felony AS SELECT * FROM read_csv('NYPD_Hate_Crimes_20250131.csv');

SELECT* FROM mydb2.felony;

CREATE TABLE mydb2.users (
    username TEXT,
    age INTEGER,
    country TEXT
);

INSERT INTO mydb2.users (username, age, country) VALUES 
    ('Alexa', 23, 'USA'),
    ('Ijaz', 28, 'Bangladesh'),
    ('Ana', 15, 'Italy'),
    ('Sarah', 35, 'Canada'),
    ('James', 21, 'USA'),
    ('Jack', 29, 'USA'),
    ('Owen', 45, 'USA'),
    ('Madison', 33, 'Canada'),
    ('Ryan', 23, 'Bangladesh'),
    ('Jean', 13, 'Canada');

SELECT* FROM mydb2.users;