ALTER TABLE `teach_reform_projects`
CHANGE COLUMN `project_type_child_id` `project_child_type_id`  int(11) NOT NULL DEFAULT 0 COMMENT '项目子类型（指向project_type_child)  （项目有类型和子类型，子类关联父类型）' AFTER `number`;

ALTER TABLE `teacher_infos`
MODIFY COLUMN `teacher_role_id`  int(11) NOT NULL DEFAULT 0 COMMENT '指向teacher_role表的id' AFTER `double_position`;

