SELECT * FROM black;
DO $$
DECLARE
    player CHAR(25);
	player_id INT;
BEGIN
	player_id := 10;
    FOR counter IN 1..10
        LOOP
		   INSERT INTO black(black_id, black_rating) 
		   VALUES (CONCAT('player_' ,CAST(player_id + counter AS CHAR(5))), 2000+counter);
        END LOOP;
END;
$$

