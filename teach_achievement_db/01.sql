/*
修正表参数，删除多余冗余字段，都用对应表的id做索引。
*/
ALTER TABLE `teacher_role`
CHANGE COLUMN `type_name` `role_name_cn`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '1教师，2管理，3其他专技类型，4校外教师' AFTER `id`,
CHANGE COLUMN `role` `role_name_en`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL AFTER `role_name_cn`;

ALTER TABLE teacher_type RENAME TO teacher_role;
ALTER TABLE `teacher`
CHANGE COLUMN `number` `account`  varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '教师工号' AFTER `id`,
CHANGE COLUMN `type` `role`  int(11) NOT NULL COMMENT '教师类型（1-系统管理员、2-学院管理员、3、普通教师）' AFTER `password`;
ALTER TABLE `teacher`
ADD COLUMN `teacher_info_id`  int(11) NOT NULL DEFAULT 0 COMMENT '指向teacher_info的id' AFTER `password`;
ALTER TABLE `teacher_info`
DROP COLUMN `number`,
CHANGE COLUMN `teachertitle_id` `teacher_title_id`  int(11) NULL DEFAULT NULL COMMENT '对应教师职称表id (指向teacher_title表的id), 功能：教师|非教师系列职称' AFTER `department_id`,
CHANGE COLUMN `managertitle_id` `manager_title_id`  int(11) NULL DEFAULT NULL COMMENT '指向teacher_title表的id 功能：增加管理级别职称 。如果是双肩挑，就有第二个职称(管理职称)' AFTER `teacher_title_id`,
CHANGE COLUMN `type` `double_position`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '是否为“双肩挑”；值：【是/否】；默认为(否)；' AFTER `teacher_category_id`,
CHANGE COLUMN `type_id` `teacher_role_id`  int(11) NULL DEFAULT NULL COMMENT '指向teacher_type表的id' AFTER `double_position`;
ALTER TABLE `college`
DROP COLUMN `department_num`,
DROP COLUMN `teacher_num`;
ALTER TABLE `department`
DROP COLUMN `number`,
ALTER TABLE `department`
ADD COLUMN `major_name`  varchar(255) NULL COMMENT '专业名称 虽然一个教研室对应一个专业，但是教研室名称和专业名称还是有所不同' AFTER `name`;

CHANGE COLUMN `director` `director_teacher_id`  int(11) NOT NULL COMMENT '教研室主任id,对应teacher表id' AFTER `name`,
MODIFY COLUMN `college_id`  int(11) NOT NULL COMMENT '所属学院id' AFTER `director_teacher_id`;

DROP TABLE `major_info`;

ALTER TABLE `teacher_title`
MODIFY COLUMN `teacher_category_id`  int(11) NOT NULL COMMENT '教师所属系列  指向教师类型teacher_category表的id' AFTER `name`;
ALTER TABLE `teacher_info`
CHANGE COLUMN `teacher_category_id` `teacher_category`  varchar(255) NULL DEFAULT NULL COMMENT '教师类型 (教师系列/管理系列/其他专技),值还有可能是教师+管理系列，所以 直接字符串，手动输入' AFTER `manager_title_id`;
ALTER TABLE `title_record`
DROP COLUMN `manager_title_id`,
CHANGE COLUMN `datetime` `title_change_time`  timestamp NOT NULL COMMENT '任职变更时间' AFTER `id`,
CHANGE COLUMN `teacher_number` `teacher_id`  int(11) NOT NULL COMMENT '授予教师id' AFTER `title_change_time`,
MODIFY COLUMN `teacher_title_id`  int(11) NULL DEFAULT NULL COMMENT '授予的教学职称id,不管是教学职称还是管理职称都是从teacher_title表中来' AFTER `teacher_id`;

ALTER TABLE `teach_reform_project`
CHANGE COLUMN `project_name` `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '教改项目名称' AFTER `id`,
CHANGE COLUMN `project_number` `number`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '项目编号 例如【X201610022125】' AFTER `name`,
CHANGE COLUMN `type_child_id` `project_type_child_id`  int(11) NOT NULL COMMENT '项目子类型（指向project_type_child)  （项目有类型和子类型，子类关联父类型）' AFTER `number`;

ALTER TABLE `project_child_type`
CHANGE COLUMN `parent_type_id` `project_type_id`  int(11) NOT NULL COMMENT '所属的父级项目类型 指向project_type表的id' AFTER `child_type_name`;

ALTER TABLE `project_change_record`
CHANGE COLUMN `project_id` `teach_reform_project_id`  int(11) NOT NULL COMMENT '项目id (指向teach_reform_project表的id，状态处于立项与结项之间的项目)' AFTER `id`;

ALTER TABLE `invigilate_info`
CHANGE COLUMN `apply_teacher` `apply_teacher_id`  int(11) NOT NULL COMMENT '申请教师的id ， teacher表的id' AFTER `id`,
CHANGE COLUMN `subject` `course_id`  int(11) NOT NULL COMMENT '考试科目id 对应course表的id' AFTER `apply_teacher_id`,
CHANGE COLUMN `semester_id` `semester_info_id`  int(11) NULL DEFAULT NULL COMMENT '所属学期id' AFTER `course_id`,
CHANGE COLUMN `class` `class_info_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '参与考试的班级（多个，对应course表name）' AFTER `semester_info_id`;

ALTER TABLE `semester_info`
CHANGE COLUMN `semester_name` `name`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '学期名称' AFTER `id`;

ALTER TABLE `course`
CHANGE COLUMN `course_name` `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '课程名称' AFTER `id`,
MODIFY COLUMN `all_teaching_time`  int(11) NULL DEFAULT NULL COMMENT '总学时（单位小时）' AFTER `category`,
CHANGE COLUMN `classes` `class_info_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '选择此课程的班级' AFTER `credit`,
CHANGE COLUMN `teacher` `teacher_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '主讲教师姓名，有可能多个' AFTER `choose_number`;
ALTER TABLE `course`
CHANGE COLUMN `class_info_names` `course_class_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '选择此课程的班级,此字段的班级名称跟学生分流的班级不通用！！！！！ 班级字段（名称）其实不太重要' AFTER `credit`;

ALTER TABLE `innovation_project`
CHANGE COLUMN `project_name` `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '项目名称' AFTER `id`,
CHANGE COLUMN `project_number` `number`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '项目编号' AFTER `name`,
CHANGE COLUMN `host_student` `host_student_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '主持学生' AFTER `subject`,
CHANGE COLUMN `participant_student` `participant_student_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '参与学生（多个）' AFTER `host_student_names`;

ALTER TABLE `book`
CHANGE COLUMN `book_name` `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '教材名称（展示）中午括号转英文，例：计算机网络安全基础（第5版）' AFTER `id`,
CHANGE COLUMN `participate_teacher` `participate_teacher_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '作者【参与教师（多个）】格式：例：[陈志泊(主编),韩慧(参编),王建新(参编),孙俏(参编),聂耿青(参编)]' AFTER `content_path`,
CHANGE COLUMN `submit_teacher` `submit_teacher_id`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '提交教师（姓名）只有管理员能看到' AFTER `participate_teacher_names`;

ALTER TABLE `certificate_info`
CHANGE COLUMN `certificate_name` `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '证书名称' AFTER `id`,
CHANGE COLUMN `teacher_number` `teacher_id`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '教师id' AFTER `organize_unit`,
CHANGE COLUMN `project_id` `teach_reform_project_id`  int(11) NULL DEFAULT NULL COMMENT '依托项目的id，指向teach_reform_project（可以不依托项目）' AFTER `grant_time`,
CHANGE COLUMN `participate_student` `participate_student_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '参与学生' AFTER `college_id`;

ALTER TABLE `teach_reform_paper`
CHANGE COLUMN `paper_name` `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '论文名称' AFTER `id`,
CHANGE COLUMN `paper_number` `number`  int(11) NULL DEFAULT NULL COMMENT '论文编号' AFTER `name`,
CHANGE COLUMN `participate_teacher` `participate_teacher_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '论文作者 （【教改论文】如果算工作量，或者此论文是否是本院论文，仅看第一作者）' AFTER `cnki_url`;

ALTER TABLE `students`
MODIFY COLUMN `id`  int(11) NOT NULL AUTO_INCREMENT COMMENT '学生学号' FIRST ,
MODIFY COLUMN `name`  varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '姓名' AFTER `password`,
ADD COLUMN `number`  int(11) NOT NULL DEFAULT 0 COMMENT '学号' AFTER `id`;
ALTER TABLE `students`
CHANGE COLUMN `class_id` `class_info_id`  int(11) NULL COMMENT '大类分流后的班级（id）' AFTER `gender`,
ADD COLUMN `old_class_name`  varchar(255) NULL COMMENT '老的班级名称；大类分流之前导入数据中学生们大一时候的老的班级' AFTER `gender`;

ALTER TABLE `class_info`
CHANGE COLUMN `class_name` `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '班级名称' AFTER `id`,
MODIFY COLUMN `grade`  int(11) NOT NULL COMMENT '年级 按照入学年份组成的班级（2015、2016.....）' AFTER `college_id`;

ALTER TABLE `distribution_info`
CHANGE COLUMN `orientation_name` `department_id`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '分流方向，从教研室中的major_name取得分流专业名称' AFTER `college_id`;

ALTER TABLE `distribution_desire`
CHANGE COLUMN `distribution_id` `distribution_info_id`  int(11) NOT NULL COMMENT '分流方向id（distribution_info的id）' AFTER `student_id`;

ALTER TABLE `distribution_info`
DROP COLUMN `num_limit`;

ALTER TABLE `class_info`
ADD COLUMN `distribution_info_id`  int(11) NULL AFTER `college_id`;

ALTER TABLE `distribution_info`
ADD COLUMN `grade`  int(11) NULL COMMENT '那个年级的分流专业，按照学生入学年份来分年级。' AFTER `department_id`;

ALTER TABLE `class_info`
DROP COLUMN `grade`;

ALTER TABLE `class_info`
DROP COLUMN `status`;

ALTER TABLE `distribution_result`
MODIFY COLUMN `distribution_id`  int(11) NOT NULL COMMENT '被分配到的（志愿）专业id' AFTER `student_id`,
ADD COLUMN `class_info_id`  int(11) NULL COMMENT '被分配到的班级id' AFTER `distribution_id`;

