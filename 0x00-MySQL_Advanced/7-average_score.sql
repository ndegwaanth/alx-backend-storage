-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE sum_ INT;
	UPDATE users SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id) WHERE id = user_id;
END//
DELIMITER ;
