ALTER TABLE `teachers`
MODIFY COLUMN `role`  varchar(255) NOT NULL DEFAULT '' COMMENT '教师类型（sadmin-系统管理员、cadmin-学院管理员、normal-普通教师）' AFTER `teacher_info_id`;

