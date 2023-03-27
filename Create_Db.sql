CREATE TABLE `project` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Prj_id` varchar(20) DEFAULT NULL,
  `emp_id` varchar(20) DEFAULT NULL,
  `Dept_id` varchar(20) DEFAULT NULL,
  `Prj_name` varchar(45) DEFAULT NULL,
  `Prj_team_size` int DEFAULT NULL,
  `Prj_budget` int DEFAULT NULL,
  `Budget_currency` varchar(5) DEFAULT NULL,
  `Prj_client` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);

CREATE TABLE `employee` (
  `Emp_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Emp_firstname` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_lastname` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_Address` varchar(90) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_country` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_dateofbirth` date DEFAULT NULL,
  `Emp_work_policy` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Employee_join_date` date DEFAULT NULL,
  `Employee_end_date` date DEFAULT NULL,
  `Employee_new_role_date` date DEFAULT NULL,
  PRIMARY KEY (`Emp_id`)
);

CREATE TABLE `department` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Dept_id` varchar(20) DEFAULT NULL,
  `Emp_id` varchar(20) DEFAULT NULL,
  `Dept_name` varchar(45) DEFAULT NULL,
  `Dept_code` varchar(45) DEFAULT NULL,
  `Dept_count` varchar(45) DEFAULT NULL,
  `Dept_function` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);

CREATE TABLE `finance` (
  `Fin_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Emp_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Dept_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Tech_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_Salary` int DEFAULT NULL,
  `Fin_month` date DEFAULT NULL,
  `Fin_year` year DEFAULT NULL,
  `Fin_bonus` int DEFAULT NULL,
  PRIMARY KEY (`Fin_id`)
);

CREATE TABLE `technology` (
  `Tech_id` varchar(20) NOT NULL,
  `Tech_name` varchar(45) DEFAULT NULL,
  `Emp_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Tech_id`)
);

CREATE TABLE `LIVE` (
  `Emp_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Emp_firstname` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_lastname` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_Address` varchar(90) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_country` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_dateofbirth` date DEFAULT NULL,
  `Emp_work_policy` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `date_join` date DEFAULT NULL,
  `date_end` date DEFAULT NULL,
  `date_new_role` date DEFAULT NULL,
  PRIMARY KEY (`Emp_id`)
);

CREATE TABLE `HISTORY` (
  `Emp_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Emp_firstname` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_lastname` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_Address` varchar(90) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_country` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Emp_dateofbirth` date DEFAULT NULL,
  `Emp_work_policy` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `date_join` date DEFAULT NULL,
  `date_end` date DEFAULT NULL,
  `date_new_role` date DEFAULT NULL,
  PRIMARY KEY (`Emp_id`)
);

CREATE DEFINER=`root`@`localhost` PROCEDURE `TDD`.`is_active_emp`()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE id varchar(20);
    DECLARE firstname varchar(45);
    DECLARE lastname varchar(45);
    DECLARE address varchar(90);
    DECLARE country varchar(45);
    DECLARE dob date;
    DECLARE work_policy varchar(45);
    DECLARE join_date date;
    DECLARE end_date date;
    DECLARE new_role_date date;

    DECLARE cur CURSOR FOR SELECT * FROM TDD.employee;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
	DELETE FROM TDD.HISTORY;
	DELETE FROM TDD.LIVE;
    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO id, firstname, lastname, address, country, dob, work_policy, join_date, end_date, new_role_date;
        IF done THEN
            LEAVE read_loop;
        END IF;

        IF end_date IS NULL THEN
            INSERT INTO TDD.LIVE (Emp_id, Emp_firstname, Emp_lastname, Emp_Address, Emp_country, Emp_dateofbirth, Emp_work_policy, date_join, date_end, date_new_role) 
            VALUES (id, firstname, lastname, address, country, dob, work_policy, join_date, end_date, new_role_date);
        ELSE
            INSERT INTO TDD.HISTORY  (Emp_id, Emp_firstname, Emp_lastname, Emp_Address, Emp_country, Emp_dateofbirth, Emp_work_policy, date_join, date_end, date_new_role) 
            VALUES (id, firstname, lastname, address, country, dob, work_policy, join_date, end_date, new_role_date);
        END IF;
    END LOOP;

    CLOSE cur;
END