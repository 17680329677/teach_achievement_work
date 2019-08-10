/* 规范所有字段默认数据，将所有字段尽可能设为非空，并设置默认数据*/
ALTER TABLE `college`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '学院名称' AFTER `id`;

ALTER TABLE `department`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教研室名称' AFTER `id`,
MODIFY COLUMN `major_name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '专业名称 虽然一个教研室对应一个专业，但是教研室名称和专业名称还是有所不同' AFTER `name`,
MODIFY COLUMN `director_teacher_id`  int(11) NOT NULL DEFAULT 0 COMMENT '教研室主任id,对应teacher表id' AFTER `major_name`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id' AFTER `director_teacher_id`;

ALTER TABLE `teacher`
MODIFY COLUMN `account`  varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教师工号' AFTER `id`,
MODIFY COLUMN `password`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '密码' AFTER `account`,
MODIFY COLUMN `role`  int(11) NOT NULL DEFAULT 0 COMMENT '教师类型（1-系统管理员、2-学院管理员、3、普通教师）' AFTER `teacher_info_id`;

ALTER TABLE `teacher_role`
MODIFY COLUMN `role_name_cn`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '1教师，2管理，3其他专技类型，4校外教师' AFTER `id`,
MODIFY COLUMN `role_name_en`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' AFTER `role_name_cn`;

ALTER TABLE `teacher_info`
MODIFY COLUMN `name`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教师姓名' AFTER `id`,
MODIFY COLUMN `gender`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '性别（文字）' AFTER `name`,
MODIFY COLUMN `nationality`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '民族' AFTER `gender`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id' AFTER `birth_year_month`,
MODIFY COLUMN `department_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属教研室id，初始化默认为0，表示未分配,等待学院管理员分配' AFTER `college_id`,
MODIFY COLUMN `teacher_title_id`  int(11) NOT NULL DEFAULT 0 COMMENT '对应教师职称表id (指向teacher_title表的id), 功能：教师|非教师系列职称' AFTER `department_id`,
MODIFY COLUMN `manager_title_id`  int(11) NOT NULL DEFAULT 0 COMMENT '指向teacher_title表的id 功能：增加管理级别职称 。如果是双肩挑，就有第二个职称(管理职称)' AFTER `teacher_title_id`,
MODIFY COLUMN `teacher_category`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教师类型 (教师系列/管理系列/其他专技),值还有可能是教师+管理系列，所以 直接字符串，手动输入' AFTER `manager_title_id`,
MODIFY COLUMN `double_position`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '是否为“双肩挑”；值：【是/否】；默认为(否)；' AFTER `teacher_category`,
MODIFY COLUMN `teacher_role_id`  int(11) NOT NULL DEFAULT 0 COMMENT '指向teacher_type表的id' AFTER `double_position`,
MODIFY COLUMN `highest_education`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '最高学历（博士后、博士、硕士、研究生同等、本科、大专、）' AFTER `bjfu_join_year_month`,
MODIFY COLUMN `graduate_paper_title`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '毕业论文题目（用户不再需要，这里做保留；前台做隐藏，目前没有用过）' AFTER `highest_education_accord_year_month`,
MODIFY COLUMN `graduate_school`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '毕业院校' AFTER `graduate_paper_title`,
MODIFY COLUMN `research_direction`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '研究方向' AFTER `graduate_school`,
MODIFY COLUMN `telephone`  varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '联系方式' AFTER `research_direction`,
MODIFY COLUMN `email`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '邮箱' AFTER `telephone`,
MODIFY COLUMN `status`  varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教师：在职/非在职/离岗；值：【在职/非在职/离岗】' AFTER `email`;

ALTER TABLE `teacher_category`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教师类型名称（教师系列/管理系列/其他专技）' AFTER `id`;

ALTER TABLE `teacher_title`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '职称名称' AFTER `id`,
MODIFY COLUMN `teacher_category_id`  int(11) NOT NULL DEFAULT 0 COMMENT '教师所属系列  指向教师类型teacher_category表的id' AFTER `name`;

ALTER TABLE `title_record`
MODIFY COLUMN `title_change_time`  timestamp NULL DEFAULT NULL COMMENT '任职变更时间' AFTER `id`,
MODIFY COLUMN `teacher_id`  int(11) NOT NULL DEFAULT 0 COMMENT '授予教师id' AFTER `title_change_time`,
MODIFY COLUMN `teacher_title_id`  int(11) NOT NULL DEFAULT 0 COMMENT '授予的教学职称id,不管是教学职称还是管理职称都是从teacher_title表中来' AFTER `teacher_id`;

ALTER TABLE `teach_reform_project`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教改项目名称' AFTER `id`,
MODIFY COLUMN `number`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '项目编号 例如【X201610022125】' AFTER `name`,
MODIFY COLUMN `project_type_child_id`  int(11) NOT NULL DEFAULT 0 COMMENT '项目子类型（指向project_type_child)  （项目有类型和子类型，子类关联父类型）' AFTER `number`,
MODIFY COLUMN `rank_id`  int(11) NOT NULL DEFAULT 0 COMMENT '项目所属级别id（指向project_rank表）' AFTER `project_type_child_id`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id,指向college表的id' AFTER `rank_id`,
MODIFY COLUMN `mid_check_rank`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '中期检查等级：[优秀、良好、中、合格、不合格]' AFTER `mid_check_year_month`,
MODIFY COLUMN `end_check_rank`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '结项等级：[优秀、良好、中、合格、不合格]' AFTER `end_year_month`,
MODIFY COLUMN `subject`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '所属一级学科：工学、管理学、农学、经济学、教育学、其他' AFTER `end_check_rank`,
MODIFY COLUMN `host_person`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '项目负责人' AFTER `subject`,
MODIFY COLUMN `participate_person`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '参加人' AFTER `host_person`,
MODIFY COLUMN `remark`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '备注信息' AFTER `participate_person`,
MODIFY COLUMN `grade`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '项目最终成绩     [优秀、良好、中、合格、不合格]' AFTER `remark`,
MODIFY COLUMN `submit_time`  timestamp NULL DEFAULT NULL COMMENT '提交时间' AFTER `grade`,
MODIFY COLUMN `status`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '状态：立项、中期检查通过、结题' AFTER `submit_time`;

ALTER TABLE `project_type`
MODIFY COLUMN `type_name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '类型名称 ,用户根据实际情况配置(如1、教改项目2、创新创业训练项目)' AFTER `id`,
MODIFY COLUMN `student_attend`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '（是/否）为学生参与的项目' AFTER `type_name`;

ALTER TABLE `project_child_type`
MODIFY COLUMN `child_type_name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '子项目名称 用户自定义：如11、教材建设12、教改重点项目' AFTER `id`,
MODIFY COLUMN `project_type_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属的父级项目类型 指向project_type表的id' AFTER `child_type_name`;

ALTER TABLE `project_rank`
MODIFY COLUMN `rank_name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教改项目等级名称' AFTER `id`;

ALTER TABLE `project_change_record`
MODIFY COLUMN `teach_reform_project_id`  int(11) NOT NULL DEFAULT 0 COMMENT '项目id (指向teach_reform_project表的id，状态处于立项与结项之间的项目)' AFTER `id`,
MODIFY COLUMN `reason`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '变更原因（申请延期，教师负责人变更、学生负责人变更等）' AFTER `teach_reform_project_id`,
MODIFY COLUMN `change_time`  timestamp NULL DEFAULT NULL COMMENT '变更时间' AFTER `reason`,
MODIFY COLUMN `describe`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '项目描述（根据用户填写的信息自动生成）' AFTER `change_time`;

ALTER TABLE `invigilate_info`
MODIFY COLUMN `apply_teacher_id`  int(11) NOT NULL DEFAULT 0 COMMENT '申请教师的id ， teacher表的id' AFTER `id`,
MODIFY COLUMN `course_id`  int(11) NOT NULL DEFAULT 0 COMMENT '考试科目id 对应course表的id' AFTER `apply_teacher_id`,
MODIFY COLUMN `semester_info_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学期id' AFTER `course_id`,
MODIFY COLUMN `class_info_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '参与考试的班级（多个，对应course表name）' AFTER `semester_info_id`,
MODIFY COLUMN `location`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '考试地点' AFTER `exam_time`,
MODIFY COLUMN `participate_teacher`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '参与监考教师（如果申请人参与了监考，那就包含申请人。统计监考次数的时候只统计participate_teacher中的。因为申请人有可能没参加监考。）' AFTER `location`,
MODIFY COLUMN `submit_time`  timestamp NULL COMMENT '提交时间' AFTER `participate_teacher`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id' AFTER `submit_time`,
MODIFY COLUMN `status`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】' AFTER `college_id`;

ALTER TABLE `semester_info`
MODIFY COLUMN `name`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '学期名称' AFTER `id`,
MODIFY COLUMN `status`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '学期状态（系统中是否可选）' AFTER `name`;

ALTER TABLE `course`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '课程名称' AFTER `id`,
MODIFY COLUMN `category`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '必修/专选' AFTER `name`,
MODIFY COLUMN `all_teaching_time`  int(11) NOT NULL DEFAULT 0 COMMENT '总学时（单位小时）' AFTER `category`,
MODIFY COLUMN `credit`  double NOT NULL DEFAULT 0 COMMENT '学分' AFTER `all_teaching_time`,
MODIFY COLUMN `course_class_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '选择此课程的班级,此字段的班级名称跟学生分流的班级不通用！！！！！ 班级字段（名称）其实不太重要' AFTER `credit`,
MODIFY COLUMN `choose_number`  int(11) NOT NULL DEFAULT 0 COMMENT '选课人数' AFTER `course_class_names`,
MODIFY COLUMN `teacher_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '主讲教师姓名，有可能多个' AFTER `choose_number`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院' AFTER `submit_time`;

ALTER TABLE `innovation_project`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '项目名称' AFTER `id`,
MODIFY COLUMN `number`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '项目编号' AFTER `name`,
MODIFY COLUMN `rank_id`  int(11) NOT NULL DEFAULT 0 COMMENT '大创项目等级id 指向innovation_rank的id' AFTER `number`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id 指向college表的id' AFTER `rank_id`,
MODIFY COLUMN `mid_check_rank`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '中期检查等级 [优秀、良好、中、合格、不合格]' AFTER `end_year_month`,
MODIFY COLUMN `end_check_rank`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '结项成绩 [优秀、良好、中、合格、不合格]' AFTER `mid_check_rank`,
MODIFY COLUMN `subject`  varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '所属一级学科' AFTER `end_check_rank`,
MODIFY COLUMN `host_student_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '主持学生' AFTER `subject`,
MODIFY COLUMN `participant_student_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '参与学生（多个）' AFTER `host_student_names`,
MODIFY COLUMN `remark`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '备注' AFTER `participant_student_names`,
MODIFY COLUMN `submit_time`  timestamp NULL COMMENT '提交时间' AFTER `remark`,
MODIFY COLUMN `status`  varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】' AFTER `submit_time`;

ALTER TABLE `innovation_rank`
MODIFY COLUMN `rank_name`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '大创项目等级 【国家级/北京市级/校级】' AFTER `id`;

ALTER TABLE `book`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教材名称（展示）中午括号转英文，例：计算机网络安全基础（第5版）' AFTER `id`,
MODIFY COLUMN `pages`  int(11) NOT NULL DEFAULT 0 COMMENT '教材页数' AFTER `publish_year_month`,
MODIFY COLUMN `words`  int(11) NOT NULL DEFAULT 0 COMMENT '总字数' AFTER `pages`,
MODIFY COLUMN `isbn`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '出版的书籍的 ISBN号 （展示）' AFTER `words`,
MODIFY COLUMN `press`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '出版社（展示）' AFTER `isbn`,
MODIFY COLUMN `version`  varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '版本类型   (新编，修订，译本)' AFTER `press`,
MODIFY COLUMN `style`  varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教材形式(文字、电子)' AFTER `version`,
MODIFY COLUMN `rank_id`  int(11) NOT NULL DEFAULT 0 COMMENT '教材级别，指向book_rank表的id（展示）' AFTER `style`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id （指向college表的id，而不是college_id）' AFTER `rank_id`,
MODIFY COLUMN `source_project`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '来源项目' AFTER `college_id`,
MODIFY COLUMN `cover_path`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '封面图片路径' AFTER `source_project`,
MODIFY COLUMN `copyright_path`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '版权页图片路径' AFTER `cover_path`,
MODIFY COLUMN `content_path`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '目录图片路径' AFTER `copyright_path`,
MODIFY COLUMN `participate_teacher_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '作者【参与教师（多个）】格式：例：[陈志泊(主编),韩慧(参编),王建新(参编),孙俏(参编),聂耿青(参编)]' AFTER `content_path`,
MODIFY COLUMN `submit_teacher_id`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '提交教师（姓名）只有管理员能看到' AFTER `participate_teacher_names`,
MODIFY COLUMN `status`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】' AFTER `submit_time`;

ALTER TABLE `book_rank`
MODIFY COLUMN `rank_name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教材等级' AFTER `id`;

ALTER TABLE `certificate_info`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '证书名称' AFTER `id`,
MODIFY COLUMN `ranking`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '获奖等级' AFTER `name`,
MODIFY COLUMN `organize_unit`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '组织单位' AFTER `rank_id`,
MODIFY COLUMN `teacher_id`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '教师id' AFTER `organize_unit`,
MODIFY COLUMN `grant_time`  timestamp NULL COMMENT '证书发放时间' AFTER `teacher_id`,
MODIFY COLUMN `teach_reform_project_id`  int(11) NOT NULL DEFAULT 0 COMMENT '依托项目的id，指向teach_reform_project（可以不依托项目）' AFTER `grant_time`,
MODIFY COLUMN `type`  varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '证书类型（教师证书或学生证书）' AFTER `teach_reform_project_id`,
MODIFY COLUMN `certificate_pic_path`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '证书图片路径' AFTER `type`,
MODIFY COLUMN `status`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】' AFTER `certificate_pic_path`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id ( 不知道是否一定属于某个学院，可为空 )' AFTER `status`,
MODIFY COLUMN `participate_student_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '参与学生' AFTER `college_id`,
MODIFY COLUMN `submit_time`  timestamp NULL COMMENT '提交时间' AFTER `participate_student_names`;

ALTER TABLE `certificate_rank`
MODIFY COLUMN `rank_name`  varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '证书等级名称' AFTER `id`;

ALTER TABLE `teach_reform_paper`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '论文名称' AFTER `id`,
MODIFY COLUMN `number`  int(11) NOT NULL DEFAULT 0 COMMENT '论文编号' AFTER `name`,
MODIFY COLUMN `journal_name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '发表期刊名称' AFTER `number`,
MODIFY COLUMN `journal_year`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '期刊年号' AFTER `publish_year_month`,
MODIFY COLUMN `journal_number`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '期刊期号' AFTER `journal_year`,
MODIFY COLUMN `journal_volum`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '期刊卷号' AFTER `journal_number`,
MODIFY COLUMN `source_project`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '来源项目' AFTER `journal_volum`,
MODIFY COLUMN `cover_path`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '封面图片路径' AFTER `source_project`,
MODIFY COLUMN `content_path`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '目录图片路径' AFTER `cover_path`,
MODIFY COLUMN `text_path`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '论文路径' AFTER `content_path`,
MODIFY COLUMN `cnki_url`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '中国知网链接' AFTER `text_path`,
MODIFY COLUMN `participate_teacher_names`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '论文作者 （【教改论文】如果算工作量，或者此论文是否是本院论文，仅看第一作者）' AFTER `cnki_url`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id' AFTER `participate_teacher_names`,
MODIFY COLUMN `status`  varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】' AFTER `college_id`;

ALTER TABLE `students`
MODIFY COLUMN `password`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '密码' AFTER `number`,
MODIFY COLUMN `name`  varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '姓名' AFTER `password`,
MODIFY COLUMN `gender`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '性别' AFTER `name`,
MODIFY COLUMN `old_class_name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '老的班级名称；大类分流之前导入数据中学生们大一时候的老的班级' AFTER `gender`,
MODIFY COLUMN `class_info_id`  int(11) NOT NULL DEFAULT 0 COMMENT '大类分流后的班级（id）' AFTER `old_class_name`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 AFTER `class_info_id`,
MODIFY COLUMN `gpa`  double NOT NULL DEFAULT 0 COMMENT '大一学年gpa' AFTER `college_id`;

ALTER TABLE `distribution_info`
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id' AFTER `id`,
MODIFY COLUMN `department_id`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 0 COMMENT '分流方向，从教研室中的major_name取得分流专业名称' AFTER `college_id`,
MODIFY COLUMN `grade`  int(11) NOT NULL DEFAULT 0 COMMENT '那个年级的分流专业，按照学生入学年份来分年级。' AFTER `department_id`,
MODIFY COLUMN `start_time`  timestamp NULL COMMENT '开始时间' AFTER `grade`,
MODIFY COLUMN `end_time`  timestamp NULL COMMENT '结束时间' AFTER `start_time`;

ALTER TABLE `class_info`
MODIFY COLUMN `name`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '班级名称' AFTER `id`,
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院' AFTER `name`,
MODIFY COLUMN `distribution_info_id`  int(11) NOT NULL DEFAULT 0 COMMENT '志愿配置id，取出里面的专业名称' AFTER `college_id`;

ALTER TABLE `distribution_desire`
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id' AFTER `id`,
MODIFY COLUMN `student_id`  int(11) NOT NULL DEFAULT 0 COMMENT '学生学号' AFTER `college_id`,
MODIFY COLUMN `desire_rank`  int(11) NOT NULL DEFAULT 0 COMMENT '志愿顺序，区分第一、第二..志愿' AFTER `distribution_info_id`,
MODIFY COLUMN `submit_time`  timestamp NULL COMMENT '提交时间' AFTER `desire_rank`,
MODIFY COLUMN `status`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '状态，是否确认分流结果【是、否】' AFTER `submit_time`;

ALTER TABLE `distribution_result`
MODIFY COLUMN `college_id`  int(11) NOT NULL DEFAULT 0 COMMENT '所属学院id' AFTER `id`,
MODIFY COLUMN `student_id`  int(11) NOT NULL DEFAULT 0 COMMENT '学生学号' AFTER `college_id`,
MODIFY COLUMN `distribution_id`  int(11) NOT NULL DEFAULT 0 COMMENT '被分配到的（志愿）专业id' AFTER `student_id`,
MODIFY COLUMN `class_info_id`  int(11) NOT NULL DEFAULT 0 COMMENT '被分配到的班级id' AFTER `distribution_id`,
MODIFY COLUMN `status`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '状态，是否确认分流结果【是、否】' AFTER `class_info_id`;

