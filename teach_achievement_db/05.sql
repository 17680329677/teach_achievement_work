/* 将所有表增加 created_at updated_at deleted_at updated_by created_by 字段，修改为BussinessDAO的格式 */
ALTER TABLE `colleges` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `departments` ADD created_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `teachers` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_roles` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_infos` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_categorys` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_titles` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `title_records` ADD created_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `teach_reform_projects` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_types` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_child_types` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_ranks` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_change_records` ADD created_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `invigilate_infos` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `semester_infos` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `courses` ADD created_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `innovation_projects` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `innovation_ranks` ADD created_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `books` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `book_ranks` ADD created_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `certificate_infos` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `certificate_ranks` ADD created_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `teach_reform_papers` ADD created_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `distribution_infos` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `class_infos` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `distribution_desires` ADD created_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `distribution_results` ADD created_at TIMESTAMP DEFAULT  NULL;


ALTER TABLE `colleges` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `departments` ADD updated_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `teachers` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_roles` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_infos` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_categorys` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_titles` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `title_records` ADD updated_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `teach_reform_projects` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_types` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_child_types` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_ranks` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_change_records` ADD updated_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `invigilate_infos` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `semester_infos` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `courses` ADD updated_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `innovation_projects` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `innovation_ranks` ADD updated_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `books` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `book_ranks` ADD updated_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `certificate_infos` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `certificate_ranks` ADD updated_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `teach_reform_papers` ADD updated_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `distribution_infos` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `class_infos` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `distribution_desires` ADD updated_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `distribution_results` ADD updated_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `colleges` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `departments` ADD deleted_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `teachers` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_roles` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_infos` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_categorys` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `teacher_titles` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `title_records` ADD deleted_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `teach_reform_projects` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_types` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_child_types` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_ranks` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `project_change_records` ADD deleted_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `invigilate_infos` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `semester_infos` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `courses` ADD deleted_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `innovation_projects` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `innovation_ranks` ADD deleted_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `books` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `book_ranks` ADD deleted_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `certificate_infos` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `certificate_ranks` ADD deleted_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `teach_reform_papers` ADD deleted_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `distribution_infos` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `class_infos` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `distribution_desires` ADD deleted_at TIMESTAMP DEFAULT  NULL;
ALTER TABLE `distribution_results` ADD deleted_at TIMESTAMP DEFAULT  NULL;

ALTER TABLE `colleges` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `departments` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `teachers` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `teacher_roles` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `teacher_infos` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `teacher_categorys` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `teacher_titles` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `title_records` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `teach_reform_projects` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `project_types` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `project_child_types` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `project_ranks` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `project_change_records` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `invigilate_infos` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `semester_infos` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `courses` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `innovation_projects` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `innovation_ranks` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `books` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `book_ranks` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `certificate_infos` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `certificate_ranks` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `teach_reform_papers` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `distribution_infos` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `class_infos` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `distribution_desires` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `distribution_results` ADD updated_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `colleges` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `departments` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `teachers` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `teacher_roles` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `teacher_infos` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `teacher_categorys` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `teacher_titles` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `title_records` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `teach_reform_projects` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `project_types` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `project_child_types` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `project_ranks` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `project_change_records` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `invigilate_infos` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `semester_infos` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `courses` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `innovation_projects` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `innovation_ranks` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `books` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `book_ranks` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `certificate_infos` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `certificate_ranks` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `teach_reform_papers` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';

ALTER TABLE `distribution_infos` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `class_infos` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `distribution_desires` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
ALTER TABLE `distribution_results` ADD created_by VARCHAR(255) NOT NULL DEFAULT '';
