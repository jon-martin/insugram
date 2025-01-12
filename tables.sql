CREATE TABLE IF NOT EXISTS items ( 
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	usual_weight INTEGER,
	carbs_per_100 INTEGER);

CREATE TABLE IF NOT EXISTS meal_item ( 
	item_id INTEGER,
	meal_id INTEGER,
	quantity INTEGER,
	PRIMARY KEY (item_id, meal_id),
	FOREIGN KEY (item_id) REFERENCES items(id),
	FOREIGN KEY (meal_id) REFERENCES meals(id));

CREATE TABLE IF NOT EXISTS meals ( 
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	insulin REAL,
	log_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);

-- hit is a number from 1-5
-- 1 - way too much
-- 2 - too much
-- 3 - good
-- 4 - too little
-- 5 - way too little
CREATE TABLE IF NOT EXISTS comments ( 
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	meal_id INTEGER,
	hit INTEGER,
	note TEXT,
	FOREIGN KEY (meal_id) REFERENCES meals(id));

-- TODO: Fill in items
INSERT INTO items (name, usual_weight, carbs_per_100) VALUES ( 'Ris', 70, 28 );

-- To be filled in through API
INSERT INTO meals (insulin) VALUES ( 20 );
INSERT INTO meal_item VALUES ( 1, 1, 70 );
INSERT INTO comments (meal_id, hit, note) VALUES ( 1, 5, 'way too little..');
