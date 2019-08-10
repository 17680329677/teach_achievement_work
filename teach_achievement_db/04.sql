/* 将所有数据表名称变为负数 */
ALTER TABLE `college` RENAME TO `colleges`;
ALTER TABLE `department` RENAME TO `departments`;

ALTER TABLE `teacher` RENAME TO `teachers`;
ALTER TABLE `teacher_role` RENAME TO `teacher_roles`;
ALTER TABLE `teacher_info` RENAME TO `teacher_infos`;
ALTER TABLE `teacher_category` RENAME TO `teacher_categorys`;
ALTER TABLE `teacher_title` RENAME TO `teacher_titles`;
ALTER TABLE `title_record` RENAME TO `title_records`;

ALTER TABLE `teach_reform_project` RENAME TO `teach_reform_projects`;
ALTER TABLE `project_type` RENAME TO `project_types`;
ALTER TABLE `project_child_type` RENAME TO `project_child_types`;
ALTER TABLE `project_rank` RENAME TO `project_ranks`;
ALTER TABLE `project_change_record` RENAME TO `project_change_records`;

ALTER TABLE `invigilate_info` RENAME TO `invigilate_infos`;
ALTER TABLE `semester_info` RENAME TO `semester_infos`;
ALTER TABLE `course` RENAME TO `courses`;

ALTER TABLE `innovation_project` RENAME TO `innovation_projects`;
ALTER TABLE `innovation_rank` RENAME TO `innovation_ranks`;

ALTER TABLE `book` RENAME TO `books`;
ALTER TABLE `book_rank` RENAME TO `book_ranks`;

ALTER TABLE `certificate_info` RENAME TO `certificate_infos`;
ALTER TABLE `certificate_rank` RENAME TO `certificate_ranks`;

ALTER TABLE `teach_reform_paper` RENAME TO `teach_reform_papers`;

ALTER TABLE `distribution_info` RENAME TO `distribution_infos`;
ALTER TABLE `class_info` RENAME TO `class_infos`;
ALTER TABLE `distribution_desire` RENAME TO `distribution_desires`;
ALTER TABLE `distribution_result` RENAME TO `distribution_results`;

