ALTER TABLE `distribution_infos`
MODIFY COLUMN `department_id`  int(11) NOT NULL DEFAULT '0' COMMENT '分流方向，从教研室中的major_name取得分流专业名称' AFTER `college_id`;

