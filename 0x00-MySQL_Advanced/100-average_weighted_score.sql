-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER //
DROP PROCEDURE IF EXISTS  computeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
	-- DECLARE average DECIMAL(10, 2);
	DECLARE average DOUBLE;
	SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) INTO average FROM corrections JOIN projects ON corrections.project_id = projects.id WHERE corrections.user_id = user_id GROUP BY corrections.user_id;
	UPDATE users SET average_score = average WHERE users.id = user_id;
END//
DELIMITER ;
