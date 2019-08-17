ALTER TABLE `distribution_infos`
MODIFY COLUMN `department_id`  int(11) NOT NULL DEFAULT '0' COMMENT '分流方向，从教研室中的major_name取得分流专业名称' AFTER `college_id`;

ALTER TABLE `distribution_results`
CHANGE COLUMN `distribution_id` `distribution_info_id`  int(11) NOT NULL DEFAULT 0 COMMENT '被分配到的（志愿）专业id' AFTER `student_id`;

ALTER TABLE `students`
ADD COLUMN `created_at`  timestamp NULL DEFAULT NULL AFTER `gpa`,
ADD COLUMN `updated_at`  timestamp NULL DEFAULT NULL AFTER `created_at`,
ADD COLUMN `deleted_at`  timestamp NULL DEFAULT NULL AFTER `updated_at`,
ADD COLUMN `updated_by`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' AFTER `deleted_at`,
ADD COLUMN `created_by`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' AFTER `updated_by`;

