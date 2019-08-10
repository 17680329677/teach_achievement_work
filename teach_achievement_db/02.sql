/* 去除所有表的 using 改用 BussinessDao标准中是的字段来代替 */
ALTER TABLE `college` DROP COLUMN `using`;
ALTER TABLE `department` DROP COLUMN `using`;


ALTER TABLE `teacher` DROP COLUMN `using`;
ALTER TABLE `teacher_role` DROP COLUMN `using`;
ALTER TABLE `teacher_info` DROP COLUMN `using`;
ALTER TABLE `teacher_category` DROP COLUMN `using`;
ALTER TABLE `teacher_title` DROP COLUMN `using`;
ALTER TABLE `title_record` DROP COLUMN `using`;

ALTER TABLE `teach_reform_project` DROP COLUMN `using`;
ALTER TABLE `project_type` DROP COLUMN `using`;
ALTER TABLE `project_child_type` DROP COLUMN `using`;
ALTER TABLE `project_rank` DROP COLUMN `using`;
ALTER TABLE `project_change_record` DROP COLUMN `using`;

ALTER TABLE `invigilate_info` DROP COLUMN `using`;
ALTER TABLE `semester_info` DROP COLUMN `using`;
ALTER TABLE `course` DROP COLUMN `using`;

ALTER TABLE `innovation_project` DROP COLUMN `using`;
ALTER TABLE `innovation_rank` DROP COLUMN `using`;

ALTER TABLE `book` DROP COLUMN `using`;
ALTER TABLE `book_rank` DROP COLUMN `using`;

ALTER TABLE `certificate_info` DROP COLUMN `using`;
ALTER TABLE `certificate_rank` DROP COLUMN `using`;

ALTER TABLE `teach_reform_paper` DROP COLUMN `using`;

ALTER TABLE `students` DROP COLUMN `using`;
ALTER TABLE `distribution_info` DROP COLUMN `using`;
ALTER TABLE `class_info` DROP COLUMN `using`;
ALTER TABLE `distribution_desire` DROP COLUMN `using`;
ALTER TABLE `distribution_result` DROP COLUMN `using`;