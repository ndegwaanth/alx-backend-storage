-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE n INT DEFAULT 0;
	DECLARE i INT DEFAULT 0;
	DECLARE user_id INT;
	DECLARE average DOUBLE;
	SELECT COUNT(*) FROM users INTO n;
	SET i=1;
	WHILE i<=n DO
		SELECT id INTO user_id FROM users WHERE id = i;
        	SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) INTO average FROM corrections JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = user_id GROUP BY corrections.user_id;
        	UPDATE users SET average_score = average WHERE users.id = user_id;
		-- CALL ComputeAverageWeightedScoreForUser((SELECT id FROM users WHERE id = i));
		SET i = i + 1;
	END WHILE;
END //
DELIMITER ;
