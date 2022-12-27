CREATE TABLE white(
	white_id CHAR(100) NOT NULL,
	white_rating INT,
	PRIMARY KEY(white_id)
);

CREATE TABLE black(
	black_id CHAR(100) NOT NULL,
	black_rating INT,
	PRIMARY KEY(black_id)
);

CREATE TABLE game(
	game_id CHAR(15) NOT NULL,
	white_player_id CHAR(100) NOT NULL,
	black_player_id CHAR(100) NOT NULL,
	winner CHAR(6),
	turns INT,
	victory_status CHAR(20),
	PRIMARY KEY(game_id),
	FOREIGN KEY(white_player_id) REFERENCES white(white_id),
	FOREIGN KEY(black_player_id) REFERENCES black(black_id)
);

DROP TABLE game;
DROP TABLE black;
DROP TABLE white;

SELECT * FROM game;

