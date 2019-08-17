/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : teach_achievement

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2019-08-15 18:09:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for books
-- ----------------------------
DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【出版教材】教师提交',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '教材名称（展示）中午括号转英文，例：计算机网络安全基础（第5版）',
  `publish_year_month` timestamp NULL DEFAULT NULL COMMENT '出版时间',
  `pages` int(11) NOT NULL DEFAULT '0' COMMENT '教材页数',
  `words` int(11) NOT NULL DEFAULT '0' COMMENT '总字数',
  `isbn` varchar(255) NOT NULL DEFAULT '' COMMENT '出版的书籍的 ISBN号 （展示）',
  `press` varchar(100) NOT NULL DEFAULT '' COMMENT '出版社（展示）',
  `version` varchar(60) NOT NULL DEFAULT '' COMMENT '版本类型   (新编，修订，译本)',
  `style` varchar(60) NOT NULL DEFAULT '' COMMENT '教材形式(文字、电子)',
  `rank_id` int(11) NOT NULL DEFAULT '0' COMMENT '教材级别，指向book_rank表的id（展示）',
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id （指向college表的id，而不是college_id）',
  `source_project` varchar(255) NOT NULL DEFAULT '' COMMENT '来源项目',
  `cover_path` varchar(255) NOT NULL DEFAULT '' COMMENT '封面图片路径',
  `copyright_path` varchar(255) NOT NULL DEFAULT '' COMMENT '版权页图片路径',
  `content_path` varchar(255) NOT NULL DEFAULT '' COMMENT '目录图片路径',
  `participate_teacher_names` varchar(255) NOT NULL DEFAULT '' COMMENT '作者【参与教师（多个）】格式：例：[陈志泊(主编),韩慧(参编),王建新(参编),孙俏(参编),聂耿青(参编)]',
  `submit_teacher_id` varchar(255) NOT NULL DEFAULT '' COMMENT '提交教师（姓名）只有管理员能看到',
  `submit_time` timestamp NULL DEFAULT NULL COMMENT '提交时间（展示）',
  `status` varchar(255) NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `rank_id` (`rank_id`),
  KEY `book_college_id` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for book_ranks
-- ----------------------------
DROP TABLE IF EXISTS `book_ranks`;
CREATE TABLE `book_ranks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(255) NOT NULL DEFAULT '' COMMENT '教材等级',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for certificate_infos
-- ----------------------------
DROP TABLE IF EXISTS `certificate_infos`;
CREATE TABLE `certificate_infos` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【证书】 教师证书，学生证书等等，功能先不实现',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '证书名称',
  `ranking` varchar(50) NOT NULL DEFAULT '' COMMENT '获奖等级',
  `rank_id` int(11) NOT NULL COMMENT '证书级别id（指向certificate_rank表的id）',
  `organize_unit` varchar(255) NOT NULL DEFAULT '' COMMENT '组织单位',
  `teacher_id` varchar(80) NOT NULL DEFAULT '' COMMENT '教师id',
  `grant_time` timestamp NULL DEFAULT NULL COMMENT '证书发放时间',
  `teach_reform_project_id` int(11) NOT NULL DEFAULT '0' COMMENT '依托项目的id，指向teach_reform_project（可以不依托项目）',
  `type` varchar(60) NOT NULL DEFAULT '' COMMENT '证书类型（教师证书或学生证书）',
  `certificate_pic_path` varchar(255) NOT NULL DEFAULT '' COMMENT '证书图片路径',
  `status` varchar(255) NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id ( 不知道是否一定属于某个学院，可为空 )',
  `participate_student_names` varchar(255) NOT NULL DEFAULT '' COMMENT '参与学生',
  `submit_time` timestamp NULL DEFAULT NULL COMMENT '提交时间',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cetification_rank_id` (`rank_id`),
  KEY `tea_ref_project_id` (`teach_reform_project_id`),
  KEY `tea_college_id` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for certificate_ranks
-- ----------------------------
DROP TABLE IF EXISTS `certificate_ranks`;
CREATE TABLE `certificate_ranks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(80) NOT NULL DEFAULT '' COMMENT '证书等级名称',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for class_infos
-- ----------------------------
DROP TABLE IF EXISTS `class_infos`;
CREATE TABLE `class_infos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '班级名称',
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院',
  `distribution_info_id` int(11) NOT NULL DEFAULT '0' COMMENT '志愿配置id，取出里面的专业名称',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `class_college` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for colleges
-- ----------------------------
DROP TABLE IF EXISTS `colleges`;
CREATE TABLE `colleges` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '学院名称',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=100119 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for courses
-- ----------------------------
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'course课程表',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '课程名称',
  `category` varchar(20) NOT NULL DEFAULT '' COMMENT '必修/专选',
  `all_teaching_time` int(11) NOT NULL DEFAULT '0' COMMENT '总学时（单位小时）',
  `credit` double NOT NULL DEFAULT '0' COMMENT '学分',
  `course_class_names` varchar(255) NOT NULL DEFAULT '' COMMENT '选择此课程的班级,此字段的班级名称跟学生分流的班级不通用！！！！！ 班级字段（名称）其实不太重要',
  `choose_number` int(11) NOT NULL DEFAULT '0' COMMENT '选课人数',
  `teacher_names` varchar(255) NOT NULL DEFAULT '' COMMENT '主讲教师姓名，有可能多个',
  `submit_time` timestamp NULL DEFAULT NULL,
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for departments
-- ----------------------------
DROP TABLE IF EXISTS `departments`;
CREATE TABLE `departments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '教研室名称',
  `major_name` varchar(255) NOT NULL DEFAULT '' COMMENT '专业名称 虽然一个教研室对应一个专业，但是教研室名称和专业名称还是有所不同',
  `director_teacher_id` int(11) NOT NULL DEFAULT '0' COMMENT '教研室主任id,对应teacher表id',
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `college_id` (`college_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for distribution_desires
-- ----------------------------
DROP TABLE IF EXISTS `distribution_desires`;
CREATE TABLE `distribution_desires` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id',
  `student_id` int(11) NOT NULL DEFAULT '0' COMMENT '学生学号',
  `distribution_info_id` int(11) NOT NULL COMMENT '分流方向id（distribution_info的id）',
  `desire_rank` int(11) NOT NULL DEFAULT '0' COMMENT '志愿顺序，区分第一、第二..志愿',
  `submit_time` timestamp NULL DEFAULT NULL COMMENT '提交时间',
  `status` varchar(20) NOT NULL DEFAULT '' COMMENT '状态，是否确认分流结果【是、否】',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `desire_stu` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for distribution_infos
-- ----------------------------
DROP TABLE IF EXISTS `distribution_infos`;
CREATE TABLE `distribution_infos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id',
  `department_id` varchar(255) NOT NULL DEFAULT '0' COMMENT '分流方向，从教研室中的major_name取得分流专业名称',
  `grade` int(11) NOT NULL DEFAULT '0' COMMENT '那个年级的分流专业，按照学生入学年份来分年级。',
  `start_time` timestamp NULL DEFAULT NULL COMMENT '开始时间',
  `end_time` timestamp NULL DEFAULT NULL COMMENT '结束时间',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `distribution_college` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for distribution_results
-- ----------------------------
DROP TABLE IF EXISTS `distribution_results`;
CREATE TABLE `distribution_results` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id',
  `student_id` int(11) NOT NULL DEFAULT '0' COMMENT '学生学号',
  `distribution_id` int(11) NOT NULL DEFAULT '0' COMMENT '被分配到的（志愿）专业id',
  `class_info_id` int(11) NOT NULL DEFAULT '0' COMMENT '被分配到的班级id',
  `status` varchar(255) NOT NULL DEFAULT '' COMMENT '状态，是否确认分流结果【是、否】',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `result_stu` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for innovation_projects
-- ----------------------------
DROP TABLE IF EXISTS `innovation_projects`;
CREATE TABLE `innovation_projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【大创项目】 由院级管理员导入，教师端不做录入功能',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '项目名称',
  `number` varchar(80) NOT NULL DEFAULT '' COMMENT '项目编号',
  `rank_id` int(11) NOT NULL DEFAULT '0' COMMENT '大创项目等级id 指向innovation_rank的id',
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id 指向college表的id',
  `begin_year_month` timestamp NULL DEFAULT NULL COMMENT '立项年月',
  `mid_check_year_month` timestamp NULL DEFAULT NULL COMMENT '中期检查年月',
  `end_year_month` timestamp NULL DEFAULT NULL COMMENT '结项年月',
  `mid_check_rank` varchar(50) NOT NULL DEFAULT '' COMMENT '中期检查等级 [优秀、良好、中、合格、不合格]',
  `end_check_rank` varchar(50) NOT NULL DEFAULT '' COMMENT '结项成绩 [优秀、良好、中、合格、不合格]',
  `subject` varchar(60) NOT NULL DEFAULT '' COMMENT '所属一级学科',
  `host_student_names` varchar(255) NOT NULL DEFAULT '' COMMENT '主持学生',
  `participant_student_names` varchar(255) NOT NULL DEFAULT '' COMMENT '参与学生（多个）',
  `remark` varchar(255) NOT NULL DEFAULT '' COMMENT '备注',
  `submit_time` timestamp NULL DEFAULT NULL COMMENT '提交时间',
  `status` varchar(60) NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `innovation_rank_id` (`rank_id`),
  KEY `innovation_college_id` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for innovation_ranks
-- ----------------------------
DROP TABLE IF EXISTS `innovation_ranks`;
CREATE TABLE `innovation_ranks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(80) NOT NULL DEFAULT '' COMMENT '大创项目等级 【国家级/北京市级/校级】',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for invigilate_infos
-- ----------------------------
DROP TABLE IF EXISTS `invigilate_infos`;
CREATE TABLE `invigilate_infos` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【监考信息】教师提交',
  `apply_teacher_id` int(11) NOT NULL DEFAULT '0' COMMENT '申请教师的id ， teacher表的id',
  `course_id` int(11) NOT NULL DEFAULT '0' COMMENT '考试科目id 对应course表的id',
  `semester_info_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学期id',
  `class_info_names` varchar(255) NOT NULL DEFAULT '' COMMENT '参与考试的班级（多个，对应course表name）',
  `exam_time` timestamp NULL DEFAULT NULL COMMENT '考试时间',
  `location` varchar(255) NOT NULL DEFAULT '' COMMENT '考试地点',
  `participate_teacher` varchar(255) NOT NULL DEFAULT '' COMMENT '参与监考教师（如果申请人参与了监考，那就包含申请人。统计监考次数的时候只统计participate_teacher中的。因为申请人有可能没参加监考。）',
  `submit_time` timestamp NULL DEFAULT NULL COMMENT '提交时间',
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id',
  `status` varchar(80) NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `invigilate_semester` (`semester_info_id`),
  KEY `invigilate_teacher` (`apply_teacher_id`),
  KEY `subject_course` (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for project_change_records
-- ----------------------------
DROP TABLE IF EXISTS `project_change_records`;
CREATE TABLE `project_change_records` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teach_reform_project_id` int(11) NOT NULL DEFAULT '0' COMMENT '项目id (指向teach_reform_project表的id，状态处于立项与结项之间的项目)',
  `reason` varchar(255) NOT NULL DEFAULT '' COMMENT '变更原因（申请延期，教师负责人变更、学生负责人变更等）',
  `change_time` timestamp NULL DEFAULT NULL COMMENT '变更时间',
  `describe` varchar(255) NOT NULL DEFAULT '' COMMENT '项目描述（根据用户填写的信息自动生成）',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teach_reform_project_id` (`teach_reform_project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for project_child_types
-- ----------------------------
DROP TABLE IF EXISTS `project_child_types`;
CREATE TABLE `project_child_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `child_type_name` varchar(255) NOT NULL DEFAULT '' COMMENT '子项目名称 用户自定义：如11、教材建设12、教改重点项目',
  `project_type_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属的父级项目类型 指向project_type表的id',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `project_type_id` (`project_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for project_ranks
-- ----------------------------
DROP TABLE IF EXISTS `project_ranks`;
CREATE TABLE `project_ranks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(255) NOT NULL DEFAULT '' COMMENT '教改项目等级名称',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for project_types
-- ----------------------------
DROP TABLE IF EXISTS `project_types`;
CREATE TABLE `project_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(255) NOT NULL DEFAULT '' COMMENT '类型名称 ,用户根据实际情况配置(如1、教改项目2、创新创业训练项目)',
  `student_attend` varchar(20) NOT NULL DEFAULT '' COMMENT '（是/否）为学生参与的项目',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for semester_infos
-- ----------------------------
DROP TABLE IF EXISTS `semester_infos`;
CREATE TABLE `semester_infos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL DEFAULT '' COMMENT '学期名称',
  `status` varchar(20) NOT NULL DEFAULT '' COMMENT '学期状态（系统中是否可选）',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '学生学号',
  `number` int(11) NOT NULL DEFAULT '0' COMMENT '学号',
  `password` varchar(255) NOT NULL DEFAULT '' COMMENT '密码',
  `name` varchar(40) NOT NULL DEFAULT '' COMMENT '姓名',
  `gender` varchar(20) NOT NULL DEFAULT '' COMMENT '性别',
  `old_class_name` varchar(255) NOT NULL DEFAULT '' COMMENT '老的班级名称；大类分流之前导入数据中学生们大一时候的老的班级',
  `class_info_id` int(11) NOT NULL DEFAULT '0' COMMENT '大类分流后的班级（id）',
  `college_id` int(11) NOT NULL DEFAULT '0',
  `gpa` double NOT NULL DEFAULT '0' COMMENT '大一学年gpa',
  PRIMARY KEY (`id`),
  KEY `stu_class` (`class_info_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for teachers
-- ----------------------------
DROP TABLE IF EXISTS `teachers`;
CREATE TABLE `teachers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(60) NOT NULL DEFAULT '' COMMENT '教师工号',
  `password` varchar(255) NOT NULL DEFAULT '' COMMENT '密码',
  `teacher_info_id` int(11) NOT NULL DEFAULT '0' COMMENT '指向teacher_info的id',
  `role` varchar(255) NOT NULL DEFAULT '' COMMENT '教师类型（sadmin-系统管理员、cadmin-学院管理员、normal-普通教师）',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teacher_teach_type` (`role`),
  KEY `number` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for teacher_categorys
-- ----------------------------
DROP TABLE IF EXISTS `teacher_categorys`;
CREATE TABLE `teacher_categorys` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT ' teacher_category表',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '教师类型名称（教师系列/管理系列/其他专技）',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for teacher_infos
-- ----------------------------
DROP TABLE IF EXISTS `teacher_infos`;
CREATE TABLE `teacher_infos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT '' COMMENT '教师姓名',
  `gender` varchar(20) NOT NULL DEFAULT '' COMMENT '性别（文字）',
  `nationality` varchar(20) NOT NULL DEFAULT '' COMMENT '民族',
  `birth_year_month` timestamp NULL DEFAULT NULL COMMENT '出生年月',
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id',
  `department_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属教研室id，初始化默认为0，表示未分配,等待学院管理员分配',
  `teacher_title_id` int(11) NOT NULL DEFAULT '0' COMMENT '对应教师职称表id (指向teacher_title表的id), 功能：教师|非教师系列职称',
  `manager_title_id` int(11) NOT NULL DEFAULT '0' COMMENT '指向teacher_title表的id 功能：增加管理级别职称 。如果是双肩挑，就有第二个职称(管理职称)',
  `teacher_category` varchar(255) NOT NULL DEFAULT '' COMMENT '教师类型 (教师系列/管理系列/其他专技),值还有可能是教师+管理系列，所以 直接字符串，手动输入',
  `double_position` varchar(20) NOT NULL DEFAULT '' COMMENT '是否为“双肩挑”；值：【是/否】；默认为(否)；',
  `teacher_role_id` int(11) NOT NULL DEFAULT '0' COMMENT '指向teacher_role表的id',
  `work_begin_year_month` timestamp NULL DEFAULT NULL COMMENT '参加工作年月',
  `bjfu_join_year_month` timestamp NULL DEFAULT NULL COMMENT '入校年月',
  `highest_education` varchar(255) NOT NULL DEFAULT '' COMMENT '最高学历（博士后、博士、硕士、研究生同等、本科、大专、）',
  `highest_education_accord_year_month` timestamp NULL DEFAULT NULL COMMENT '最高学历取得年月',
  `graduate_paper_title` varchar(255) NOT NULL DEFAULT '' COMMENT '毕业论文题目（用户不再需要，这里做保留；前台做隐藏，目前没有用过）',
  `graduate_school` varchar(255) NOT NULL DEFAULT '' COMMENT '毕业院校',
  `research_direction` varchar(255) NOT NULL DEFAULT '' COMMENT '研究方向',
  `telephone` varchar(60) NOT NULL DEFAULT '' COMMENT '联系方式',
  `email` varchar(255) NOT NULL DEFAULT '' COMMENT '邮箱',
  `status` varchar(60) NOT NULL DEFAULT '' COMMENT '教师：在职/非在职/离岗；值：【在职/非在职/离岗】',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teachertitle_id` (`teacher_title_id`),
  KEY `managertitle_id` (`manager_title_id`),
  KEY `teacher_type_id` (`teacher_role_id`),
  KEY `teachercategory` (`teacher_category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for teacher_roles
-- ----------------------------
DROP TABLE IF EXISTS `teacher_roles`;
CREATE TABLE `teacher_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name_cn` varchar(255) NOT NULL DEFAULT '' COMMENT '1教师，2管理，3其他专技类型，4校外教师',
  `role_name_en` varchar(255) NOT NULL DEFAULT '',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for teacher_titles
-- ----------------------------
DROP TABLE IF EXISTS `teacher_titles`;
CREATE TABLE `teacher_titles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '职称名称',
  `teacher_category_id` int(11) NOT NULL DEFAULT '0' COMMENT '教师所属系列  指向教师类型teacher_category表的id',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teach_type` (`teacher_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for teach_reform_papers
-- ----------------------------
DROP TABLE IF EXISTS `teach_reform_papers`;
CREATE TABLE `teach_reform_papers` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【教改论文】如果算工作量，或者此论文是否是本院论文，仅看第一作者',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '论文名称',
  `number` int(11) NOT NULL DEFAULT '0' COMMENT '论文编号',
  `journal_name` varchar(255) NOT NULL DEFAULT '' COMMENT '发表期刊名称',
  `publish_year_month` timestamp NULL DEFAULT NULL COMMENT '发表年月',
  `journal_year` varchar(255) NOT NULL DEFAULT '' COMMENT '期刊年号',
  `journal_number` varchar(255) NOT NULL DEFAULT '' COMMENT '期刊期号',
  `journal_volum` varchar(255) NOT NULL DEFAULT '' COMMENT '期刊卷号',
  `source_project` varchar(255) NOT NULL DEFAULT '' COMMENT '来源项目',
  `cover_path` varchar(255) NOT NULL DEFAULT '' COMMENT '封面图片路径',
  `content_path` varchar(255) NOT NULL DEFAULT '' COMMENT '目录图片路径',
  `text_path` varchar(255) NOT NULL DEFAULT '' COMMENT '论文路径',
  `cnki_url` varchar(255) NOT NULL DEFAULT '' COMMENT '中国知网链接',
  `participate_teacher_names` varchar(255) NOT NULL DEFAULT '' COMMENT '论文作者 （【教改论文】如果算工作量，或者此论文是否是本院论文，仅看第一作者）',
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id',
  `status` varchar(40) NOT NULL DEFAULT '' COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for teach_reform_projects
-- ----------------------------
DROP TABLE IF EXISTS `teach_reform_projects`;
CREATE TABLE `teach_reform_projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【教改项目】 由院级管理员导入，教师端不做录入功能',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '教改项目名称',
  `number` varchar(255) NOT NULL DEFAULT '' COMMENT '项目编号 例如【X201610022125】',
  `project_child_type_id` int(11) NOT NULL DEFAULT '0' COMMENT '项目子类型（指向project_type_child)  （项目有类型和子类型，子类关联父类型）',
  `rank_id` int(11) NOT NULL DEFAULT '0' COMMENT '项目所属级别id（指向project_rank表）',
  `college_id` int(11) NOT NULL DEFAULT '0' COMMENT '所属学院id,指向college表的id',
  `begin_year_month` timestamp NULL DEFAULT NULL COMMENT '项目立项时间',
  `mid_check_year_month` timestamp NULL DEFAULT NULL COMMENT '中期检查时间',
  `mid_check_rank` varchar(20) NOT NULL DEFAULT '' COMMENT '中期检查等级：[优秀、良好、中、合格、不合格]',
  `end_year_month` timestamp NULL DEFAULT NULL COMMENT '项目结项时间\r\n',
  `end_check_rank` varchar(20) NOT NULL DEFAULT '' COMMENT '结项等级：[优秀、良好、中、合格、不合格]',
  `subject` varchar(80) NOT NULL DEFAULT '' COMMENT '所属一级学科：工学、管理学、农学、经济学、教育学、其他',
  `host_person` varchar(255) NOT NULL DEFAULT '' COMMENT '项目负责人',
  `participate_person` varchar(255) NOT NULL DEFAULT '' COMMENT '参加人',
  `remark` varchar(255) NOT NULL DEFAULT '' COMMENT '备注信息',
  `grade` varchar(255) NOT NULL DEFAULT '' COMMENT '项目最终成绩     [优秀、良好、中、合格、不合格]',
  `submit_time` timestamp NULL DEFAULT NULL COMMENT '提交时间',
  `status` varchar(20) NOT NULL DEFAULT '' COMMENT '状态：立项、中期检查通过、结题',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `project_rank_id` (`rank_id`),
  KEY `college_id_pro` (`college_id`),
  KEY `project_type_child_id` (`project_child_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for title_records
-- ----------------------------
DROP TABLE IF EXISTS `title_records`;
CREATE TABLE `title_records` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title_change_time` timestamp NULL DEFAULT NULL COMMENT '任职变更时间',
  `teacher_id` int(11) NOT NULL DEFAULT '0' COMMENT '授予教师id',
  `teacher_title_id` int(11) NOT NULL DEFAULT '0' COMMENT '授予的教学职称id,不管是教学职称还是管理职称都是从teacher_title表中来',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_by` varchar(255) NOT NULL DEFAULT '',
  `created_by` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teacher_title_id` (`teacher_title_id`),
  KEY `record_teacher_number` (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
