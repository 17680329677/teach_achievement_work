/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : teach_achievement

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2019-07-21 16:44:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【出版教材】教师提交',
  `book_name` varchar(255) NOT NULL COMMENT '教材名称（展示）中午括号转英文，例：计算机网络安全基础（第5版）',
  `publish_year_month` timestamp NULL DEFAULT NULL COMMENT '出版时间',
  `pages` int(11) DEFAULT NULL COMMENT '教材页数',
  `words` int(11) DEFAULT NULL COMMENT '总字数',
  `isbn` varchar(255) DEFAULT NULL COMMENT '出版的书籍的 ISBN号 （展示）',
  `press` varchar(100) DEFAULT NULL COMMENT '出版社（展示）',
  `version` varchar(60) DEFAULT NULL COMMENT '版本类型   (新编，修订，译本)',
  `style` varchar(60) DEFAULT NULL COMMENT '教材形式(文字、电子)',
  `rank_id` int(11) DEFAULT NULL COMMENT '教材级别，指向book_rank表的id（展示）',
  `college_id` int(11) NOT NULL COMMENT '所属学院id （指向college表的id，而不是college_id）',
  `source_project` varchar(255) DEFAULT NULL COMMENT '来源项目',
  `cover_path` varchar(255) DEFAULT NULL COMMENT '封面图片路径',
  `copyright_path` varchar(255) DEFAULT NULL COMMENT '版权页图片路径',
  `content_path` varchar(255) DEFAULT NULL COMMENT '目录图片路径',
  `participate_teacher` varchar(255) DEFAULT NULL COMMENT '作者【参与教师（多个）】格式：例：[陈志泊(主编),韩慧(参编),王建新(参编),孙俏(参编),聂耿青(参编)]',
  `submit_teacher` varchar(255) DEFAULT NULL COMMENT '提交教师（姓名）只有管理员能看到',
  `submit_time` timestamp NULL DEFAULT NULL COMMENT '提交时间（展示）',
  `status` varchar(255) DEFAULT NULL COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `rank_id` (`rank_id`),
  KEY `book_college_id` (`college_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of book
-- ----------------------------

-- ----------------------------
-- Table structure for book_rank
-- ----------------------------
DROP TABLE IF EXISTS `book_rank`;
CREATE TABLE `book_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(255) NOT NULL COMMENT '教材等级',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of book_rank
-- ----------------------------
INSERT INTO `book_rank` VALUES ('1', '国家级精品教材', '1');
INSERT INTO `book_rank` VALUES ('2', '北京市精品教材', '1');
INSERT INTO `book_rank` VALUES ('3', '校级教材', '1');
INSERT INTO `book_rank` VALUES ('4', '“十一五”规划教材', '1');
INSERT INTO `book_rank` VALUES ('5', '“十二五”规划教材', '1');
INSERT INTO `book_rank` VALUES ('6', '  ', '1');
INSERT INTO `book_rank` VALUES ('7', '“十三五”规划教材', '1');

-- ----------------------------
-- Table structure for certificate_info
-- ----------------------------
DROP TABLE IF EXISTS `certificate_info`;
CREATE TABLE `certificate_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【证书】 教师证书，学生证书等等，功能先不实现',
  `certificate_name` varchar(255) NOT NULL COMMENT '证书名称',
  `ranking` varchar(50) NOT NULL COMMENT '获奖等级',
  `rank_id` int(11) NOT NULL COMMENT '证书级别id（指向certificate_rank表的id）',
  `organize_unit` varchar(255) NOT NULL COMMENT '组织单位',
  `teacher_number` varchar(80) NOT NULL COMMENT '教师工号',
  `grant_time` timestamp NOT NULL COMMENT '证书发放时间',
  `project_id` int(11) DEFAULT NULL COMMENT '依托项目的id，指向teach_reform_project（可以不依托项目）',
  `type` varchar(60) DEFAULT NULL COMMENT '证书类型（教师证书或学生证书）',
  `certificate_pic_path` varchar(255) DEFAULT NULL COMMENT '证书图片路径',
  `status` varchar(255) NOT NULL COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `college_id` int(11) DEFAULT NULL COMMENT '所属学院id ( 不知道是否一定属于某个学院，可为空 )',
  `participate_student` varchar(255) DEFAULT NULL COMMENT '参与学生',
  `submit_time` timestamp NOT NULL COMMENT '提交时间',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cetification_rank_id` (`rank_id`),
  KEY `tea_ref_project_id` (`project_id`),
  KEY `tea_college_id` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of certificate_info
-- ----------------------------

-- ----------------------------
-- Table structure for certificate_rank
-- ----------------------------
DROP TABLE IF EXISTS `certificate_rank`;
CREATE TABLE `certificate_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(80) NOT NULL COMMENT '证书等级名称',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of certificate_rank
-- ----------------------------
INSERT INTO `certificate_rank` VALUES ('1', '国家级', '1');
INSERT INTO `certificate_rank` VALUES ('2', '省部级', '1');
INSERT INTO `certificate_rank` VALUES ('3', '北京市', '1');
INSERT INTO `certificate_rank` VALUES ('4', '校级', '1');

-- ----------------------------
-- Table structure for class_info
-- ----------------------------
DROP TABLE IF EXISTS `class_info`;
CREATE TABLE `class_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_name` varchar(255) NOT NULL COMMENT '班级名称',
  `college_id` int(11) NOT NULL COMMENT '所属学院',
  `grade` varchar(60) NOT NULL COMMENT '年级',
  `status` varchar(20) NOT NULL COMMENT '状态（有效无效的标志）',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `class_college` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of class_info
-- ----------------------------

-- ----------------------------
-- Table structure for college
-- ----------------------------
DROP TABLE IF EXISTS `college`;
CREATE TABLE `college` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '学院名称',
  `department_num` int(11) DEFAULT NULL,
  `teacher_num` int(11) DEFAULT NULL,
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=100119 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of college
-- ----------------------------
INSERT INTO `college` VALUES ('100101', '林学院', '1', '1', '1');
INSERT INTO `college` VALUES ('100102', '水土保持学院', '4', '23', '1');
INSERT INTO `college` VALUES ('100103', '生物科学与技术学院', '6', '44', '1');
INSERT INTO `college` VALUES ('100104', '园林学院', '2', '32', '1');
INSERT INTO `college` VALUES ('100105', '经济管理学院', '5', '32', '1');
INSERT INTO `college` VALUES ('100106', '工学院', '6', '12', '1');
INSERT INTO `college` VALUES ('100107', '材料科学与技术学院', '9', '34', '1');
INSERT INTO `college` VALUES ('100108', '人文社会科学学院', '4', '32', '1');
INSERT INTO `college` VALUES ('100109', '外语学院', '6', '24', '1');
INSERT INTO `college` VALUES ('100110', '信息学院', '3', '1', '1');
INSERT INTO `college` VALUES ('100111', '理学院', '6', '5', '1');
INSERT INTO `college` VALUES ('100112', '自然保护区学院', '4', '7', '1');
INSERT INTO `college` VALUES ('100113', '环境科学与工程学院', '6', '42', '1');
INSERT INTO `college` VALUES ('100114', '艺术设计学院', '5', '24', '1');
INSERT INTO `college` VALUES ('100115', '马克思主义学院', '4', '32', '1');
INSERT INTO `college` VALUES ('100116', '继续教育学院', '3', '11', '1');
INSERT INTO `college` VALUES ('100117', '国际学院', null, null, '1');
INSERT INTO `college` VALUES ('100118', '体育教学部', null, null, '1');

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'course课程表',
  `course_name` varchar(255) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL COMMENT '必修/专选',
  `all_teaching_time` int(11) DEFAULT NULL COMMENT '总学时',
  `credit` double DEFAULT NULL COMMENT '学分',
  `classes` varchar(255) DEFAULT NULL,
  `choose_number` int(11) DEFAULT NULL COMMENT '选课人数',
  `teacher` varchar(255) DEFAULT NULL COMMENT '主讲教师id',
  `submit_time` timestamp NULL DEFAULT NULL,
  `college_id` int(11) DEFAULT NULL COMMENT '所属学院',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of course
-- ----------------------------

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL COMMENT '教研室名称',
  `number` int(10) unsigned zerofill NOT NULL COMMENT '教研室人数， 每次查询教研室的时候会更新教研室数量',
  `director` varchar(255) NOT NULL COMMENT '教研室主任工号',
  `college_id` int(255) NOT NULL COMMENT '所属学院id',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `college_id` (`college_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES ('26', '计算机软件教研室', '0000000002', '536656', '100110', '1');
INSERT INTO `department` VALUES ('28', '信息教研室', '0000000003', '654652', '100110', '1');
INSERT INTO `department` VALUES ('29', '数字媒体教研室', '0000000001', '551232', '100110', '1');
INSERT INTO `department` VALUES ('30', '网络教研室', '0000000001', '654654', '100110', '1');
INSERT INTO `department` VALUES ('31', '计算机实验教学中心', '0000000001', '461232', '100110', '1');
INSERT INTO `department` VALUES ('32', '行政', '0000000001', '654654', '100110', '1');
INSERT INTO `department` VALUES ('33', '  ', '0000000000', '0', '100110', '1');

-- ----------------------------
-- Table structure for distribution_desire
-- ----------------------------
DROP TABLE IF EXISTS `distribution_desire`;
CREATE TABLE `distribution_desire` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college_id` int(11) NOT NULL COMMENT '所属学院id',
  `student_id` int(11) NOT NULL COMMENT '学生学号',
  `distribution_id` int(11) NOT NULL COMMENT '分流方向id（distribution_info的id）',
  `desire_rank` int(11) NOT NULL COMMENT '志愿顺序，区分第一、第二..志愿',
  `submit_time` timestamp NOT NULL COMMENT '提交时间',
  `status` varchar(20) NOT NULL COMMENT '状态，是否确认分流结果【1.是、0。否】',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `desire_stu` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of distribution_desire
-- ----------------------------

-- ----------------------------
-- Table structure for distribution_info
-- ----------------------------
DROP TABLE IF EXISTS `distribution_info`;
CREATE TABLE `distribution_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college_id` int(11) NOT NULL COMMENT '所属学院id',
  `orientation_name` varchar(255) NOT NULL COMMENT '分流方向（专业）名称（是否和学院专业出入？从属于学院专业？）',
  `num_limit` int(11) NOT NULL COMMENT '人数限制',
  `start_time` timestamp NOT NULL COMMENT '开始时间',
  `end_time` timestamp NOT NULL COMMENT '结束时间',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `distribution_college` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of distribution_info
-- ----------------------------

-- ----------------------------
-- Table structure for distribution_result
-- ----------------------------
DROP TABLE IF EXISTS `distribution_result`;
CREATE TABLE `distribution_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college_id` int(11) NOT NULL COMMENT '所属学院id',
  `student_id` int(11) NOT NULL COMMENT '学生学号',
  `distribution_id` int(11) NOT NULL COMMENT '分流id',
  `status` varchar(255) NOT NULL COMMENT '状态，是否确认分流结果【1.是、0。否】',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `result_stu` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of distribution_result
-- ----------------------------

-- ----------------------------
-- Table structure for innovation_project
-- ----------------------------
DROP TABLE IF EXISTS `innovation_project`;
CREATE TABLE `innovation_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【大创项目】 由院级管理员导入，教师端不做录入功能',
  `project_name` varchar(255) NOT NULL COMMENT '项目名称',
  `project_number` varchar(80) NOT NULL COMMENT '项目编号',
  `rank_id` int(11) NOT NULL COMMENT '大创项目等级id 指向innovation_rank的id',
  `college_id` int(11) NOT NULL COMMENT '所属学院id 指向college表的id',
  `begin_year_month` timestamp NULL DEFAULT NULL COMMENT '立项年月',
  `mid_check_year_month` timestamp NULL DEFAULT NULL COMMENT '中期检查年月',
  `end_year_month` timestamp NULL DEFAULT NULL COMMENT '结项年月',
  `mid_check_rank` varchar(50) DEFAULT NULL COMMENT '中期检查等级 [优秀、良好、中、合格、不合格]',
  `end_check_rank` varchar(50) DEFAULT NULL COMMENT '结项成绩 [优秀、良好、中、合格、不合格]',
  `subject` varchar(60) DEFAULT NULL COMMENT '所属一级学科',
  `host_student` varchar(255) NOT NULL COMMENT '主持学生',
  `participant_student` varchar(255) DEFAULT NULL COMMENT '参与学生（多个）',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `submit_time` timestamp NOT NULL COMMENT '提交时间',
  `status` varchar(60) NOT NULL COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `innovation_rank_id` (`rank_id`),
  KEY `innovation_college_id` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of innovation_project
-- ----------------------------

-- ----------------------------
-- Table structure for innovation_rank
-- ----------------------------
DROP TABLE IF EXISTS `innovation_rank`;
CREATE TABLE `innovation_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(80) NOT NULL COMMENT '大创项目等级 【国家级/北京市级/校级】',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of innovation_rank
-- ----------------------------
INSERT INTO `innovation_rank` VALUES ('1', '国家级', '1');
INSERT INTO `innovation_rank` VALUES ('2', '北京市级', '1');
INSERT INTO `innovation_rank` VALUES ('3', '校级', '1');

-- ----------------------------
-- Table structure for invigilate_info
-- ----------------------------
DROP TABLE IF EXISTS `invigilate_info`;
CREATE TABLE `invigilate_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【监考信息】教师提交',
  `apply_teacher` varchar(255) NOT NULL COMMENT '申请教师的工号',
  `subject` int(11) NOT NULL COMMENT '考试科目id 对应course表的id',
  `semester_id` int(11) DEFAULT NULL COMMENT '所属学期id',
  `class` varchar(255) NOT NULL COMMENT '班级（多个id）',
  `exam_time` timestamp NULL DEFAULT NULL COMMENT '考试时间',
  `location` varchar(255) NOT NULL COMMENT '考试地点',
  `participate_teacher` varchar(255) NOT NULL COMMENT '参与监考教师（如果申请人参与了监考，那就包含申请人。统计监考次数的时候只统计participate_teacher中的。因为申请人有可能没参加监考。）',
  `submit_time` timestamp NOT NULL COMMENT '提交时间',
  `college_id` int(11) NOT NULL COMMENT '所属学院id',
  `status` varchar(80) DEFAULT NULL COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `invigilate_semester` (`semester_id`),
  KEY `invigilate_teacher` (`apply_teacher`),
  KEY `subject_course` (`subject`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of invigilate_info
-- ----------------------------

-- ----------------------------
-- Table structure for major_info
-- ----------------------------
DROP TABLE IF EXISTS `major_info`;
CREATE TABLE `major_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `major_name` varchar(255) NOT NULL COMMENT '专业名称（方向）',
  `college_id` int(11) NOT NULL COMMENT '所属学院id',
  `department_id` int(11) NOT NULL COMMENT '所属教研室id',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `major_department` (`department_id`),
  KEY `major_college` (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of major_info
-- ----------------------------

-- ----------------------------
-- Table structure for project_change_record
-- ----------------------------
DROP TABLE IF EXISTS `project_change_record`;
CREATE TABLE `project_change_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL COMMENT '项目id (指向teach_reform_project表的id，状态处于立项与结项之间的项目)',
  `reason` varchar(255) NOT NULL COMMENT '变更原因（申请延期，教师负责人变更、学生负责人变更等）',
  `change_time` timestamp NOT NULL COMMENT '变更时间',
  `describe` varchar(255) NOT NULL COMMENT '项目描述（根据用户填写的信息自动生成）',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teach_reform_project_id` (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of project_change_record
-- ----------------------------

-- ----------------------------
-- Table structure for project_child_type
-- ----------------------------
DROP TABLE IF EXISTS `project_child_type`;
CREATE TABLE `project_child_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `child_type_name` varchar(255) NOT NULL COMMENT '子项目名称 用户自定义：如11、教材建设12、教改重点项目',
  `parent_type_id` int(11) NOT NULL COMMENT '所属的父级项目类型 指向project_type表的id',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `project_type_id` (`parent_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of project_child_type
-- ----------------------------
INSERT INTO `project_child_type` VALUES ('1', '教学团队', '1', '1');
INSERT INTO `project_child_type` VALUES ('2', '专业建设', '1', '1');
INSERT INTO `project_child_type` VALUES ('3', '精品课程', '1', '1');
INSERT INTO `project_child_type` VALUES ('4', '教材建设', '2', '1');
INSERT INTO `project_child_type` VALUES ('5', '教学改革研究项目', '3', '1');
INSERT INTO `project_child_type` VALUES ('6', '国家级大学生创新创业训练计划项目', '4', '1');
INSERT INTO `project_child_type` VALUES ('7', '北京市大学生科学研究与创业行动计划项目', '4', '1');
INSERT INTO `project_child_type` VALUES ('8', '校级大学生科研训练计划项目', '4', '1');

-- ----------------------------
-- Table structure for project_rank
-- ----------------------------
DROP TABLE IF EXISTS `project_rank`;
CREATE TABLE `project_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(255) NOT NULL COMMENT '教改项目等级名称',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of project_rank
-- ----------------------------
INSERT INTO `project_rank` VALUES ('1', '国家级', '1');
INSERT INTO `project_rank` VALUES ('2', '北京市', '1');
INSERT INTO `project_rank` VALUES ('3', '校级', '1');

-- ----------------------------
-- Table structure for project_type
-- ----------------------------
DROP TABLE IF EXISTS `project_type`;
CREATE TABLE `project_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(255) NOT NULL COMMENT '类型名称 ,用户根据实际情况配置(如1、教改项目2、创新创业训练项目)',
  `student_attend` varchar(20) NOT NULL COMMENT '（是/否）为学生参与的项目',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of project_type
-- ----------------------------
INSERT INTO `project_type` VALUES ('1', '本科教学工程', '否', '1');
INSERT INTO `project_type` VALUES ('2', '教材建设', '否', '1');
INSERT INTO `project_type` VALUES ('3', '教学改革研究项目', '否', '1');
INSERT INTO `project_type` VALUES ('4', '大学生创新创业训练项目', '否', '1');

-- ----------------------------
-- Table structure for semester_info
-- ----------------------------
DROP TABLE IF EXISTS `semester_info`;
CREATE TABLE `semester_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `semester_name` varchar(80) NOT NULL COMMENT '学期名称',
  `status` varchar(20) NOT NULL COMMENT '学期状态（系统中是否可选）',
  `using` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of semester_info
-- ----------------------------
INSERT INTO `semester_info` VALUES ('3', '2018-2019 第1学期', '过期', '1');
INSERT INTO `semester_info` VALUES ('4', '2018-2019 第2学期', '当前', '1');

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int(11) NOT NULL COMMENT '学生学号',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `name` varchar(40) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL COMMENT '性别',
  `class_id` int(11) NOT NULL COMMENT '班级（id）',
  `college_id` int(11) NOT NULL,
  `gpa` double NOT NULL COMMENT '大一学年gpa',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stu_class` (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('7180278', '123456', '111', '11', '1', '10', '1', '1');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(60) NOT NULL COMMENT '教师工号',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `type` int(11) NOT NULL COMMENT '教师类型（1-系统管理员、2-学院管理员、3、普通教师）',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teacher_teach_type` (`type`),
  KEY `number` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('1', 'root', 'pbkdf2:sha256:50000$iVuYIAgB$c55f7337cf770fd3bb0c1e66c779a3e1ad60a650d768562b2226fc58c775f8df', '1', '1');
INSERT INTO `teacher` VALUES ('2', 'xxxy-admin', 'pbkdf2:sha256:50000$ZOJdcV7b$d76d628248542c020e927f6e0d2c7a69a7e2e6aa2a1c25bd2506f6819bba51d8', '2', '1');
INSERT INTO `teacher` VALUES ('12', 'lxy-admin', 'pbkdf2:sha256:50000$Fso0AkKV$b2c79d3fee313fc118b89b727d957cc713592601bb32843a7d69ec4311422fd8', '2', '1');
INSERT INTO `teacher` VALUES ('13', '670103', 'pbkdf2:sha256:50000$Fso0AkKV$b2c79d3fee313fc118b89b727d957cc713592601bb32843a7d69ec4311422fd8', '5', '1');
INSERT INTO `teacher` VALUES ('20', '650909', 'pbkdf2:sha256:50000$Fso0AkKV$b2c79d3fee313fc118b89b727d957cc713592601bb32843a7d69ec4311422fd8', '5', '1');
INSERT INTO `teacher` VALUES ('21', '550401', 'pbkdf2:sha256:50000$Fso0AkKV$b2c79d3fee313fc118b89b727d957cc713592601bb32843a7d69ec4311422fd8', '5', '1');
INSERT INTO `teacher` VALUES ('22', '610202', 'pbkdf2:sha256:50000$Fso0AkKV$b2c79d3fee313fc118b89b727d957cc713592601bb32843a7d69ec4311422fd8', '5', '1');
INSERT INTO `teacher` VALUES ('23', '536656', 'pbkdf2:sha256:50000$Fso0AkKV$b2c79d3fee313fc118b89b727d957cc713592601bb32843a7d69ec4311422fd8', '5', '1');
INSERT INTO `teacher` VALUES ('24', '654654', 'pbkdf2:sha256:50000$Fso0AkKV$b2c79d3fee313fc118b89b727d957cc713592601bb32843a7d69ec4311422fd8', '5', '1');
INSERT INTO `teacher` VALUES ('25', '551232', 'pbkdf2:sha256:50000$Fso0AkKV$b2c79d3fee313fc118b89b727d957cc713592601bb32843a7d69ec4311422fd8', '5', '1');
INSERT INTO `teacher` VALUES ('26', '654652', 'pbkdf2:sha256:50000$Fso0AkKV$b2c79d3fee313fc118b89b727d957cc713592601bb32843a7d69ec4311422fd8', '5', '1');

-- ----------------------------
-- Table structure for teacher_category
-- ----------------------------
DROP TABLE IF EXISTS `teacher_category`;
CREATE TABLE `teacher_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT ' teacher_category表',
  `name` varchar(255) DEFAULT NULL COMMENT '教师类型名称（教师系列/管理系列/其他专技）',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teacher_category
-- ----------------------------
INSERT INTO `teacher_category` VALUES ('1', '教师系列', '1');
INSERT INTO `teacher_category` VALUES ('2', '管理系列', '1');
INSERT INTO `teacher_category` VALUES ('3', '其他专技', '1');
INSERT INTO `teacher_category` VALUES ('4', '教师系列+管理系列', '1');

-- ----------------------------
-- Table structure for teacher_info
-- ----------------------------
DROP TABLE IF EXISTS `teacher_info`;
CREATE TABLE `teacher_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(60) NOT NULL COMMENT '教师工号;校内老师，必有字段.',
  `name` varchar(100) DEFAULT NULL COMMENT '教师姓名',
  `gender` varchar(20) DEFAULT NULL COMMENT '性别（文字）',
  `nationality` varchar(20) DEFAULT NULL COMMENT '民族',
  `birth_year_month` timestamp NULL DEFAULT NULL COMMENT '出生年月',
  `college_id` int(11) DEFAULT NULL COMMENT '所属学院id',
  `department_id` int(11) DEFAULT NULL COMMENT '所属教研室id，初始化默认为0，表示未分配,等待学院管理员分配',
  `teachertitle_id` int(11) DEFAULT NULL COMMENT '对应教师职称表id (指向teacher_title表的id), 功能：教师|非教师系列职称',
  `managertitle_id` int(11) DEFAULT NULL COMMENT '指向teacher_title表的id 功能：增加管理级别职称 。如果是双肩挑，就有第二个职称(管理职称)',
  `teacher_category_id` int(11) DEFAULT NULL COMMENT '教师类型 (教师系列/管理系列/其他专技), teacher_category表的id',
  `type` varchar(20) DEFAULT NULL COMMENT '是否为“双肩挑”；值：【是/否】；默认为(否)；',
  `type_id` int(11) DEFAULT NULL COMMENT '指向teacher_type表的id',
  `work_begin_year_month` timestamp NULL DEFAULT NULL COMMENT '参加工作年月',
  `bjfu_join_year_month` timestamp NULL DEFAULT NULL COMMENT '入校年月',
  `highest_education` varchar(255) DEFAULT NULL COMMENT '最高学历（博士后、博士、硕士、研究生同等、本科、大专、）',
  `highest_education_accord_year_month` timestamp NULL DEFAULT NULL COMMENT '最高学历取得年月',
  `graduate_paper_title` varchar(255) DEFAULT NULL COMMENT '毕业论文题目（用户不再需要，这里做保留；前台做隐藏，目前没有用过）',
  `graduate_school` varchar(255) DEFAULT NULL COMMENT '毕业院校',
  `research_direction` varchar(255) DEFAULT NULL COMMENT '研究方向',
  `telephone` varchar(60) DEFAULT NULL COMMENT '联系方式',
  `email` varchar(255) DEFAULT NULL COMMENT '邮箱',
  `status` varchar(60) DEFAULT NULL COMMENT '教师：在职/非在职/离岗；值：【在职/非在职/离岗】',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `number` (`number`) USING BTREE,
  KEY `teachertitle_id` (`teachertitle_id`),
  KEY `managertitle_id` (`managertitle_id`),
  KEY `teacher_type_id` (`type_id`),
  KEY `teachercategory` (`teacher_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_info
-- ----------------------------
INSERT INTO `teacher_info` VALUES ('1', 'xxxy-admin', '信息学院管理员', ' ', null, null, '100110', '0', null, null, null, null, '2', null, null, null, null, null, null, null, null, null, null, '1');
INSERT INTO `teacher_info` VALUES ('4', 'lxy-admin', '林学院管理员', null, null, null, '100101', null, null, null, null, null, '2', null, null, null, null, null, null, null, null, null, null, '1');
INSERT INTO `teacher_info` VALUES ('8', '670103', '陈志泊', '男', '汉族', null, '100110', '26', '5', '30', '1', '是', '5', null, null, '博士', null, '', '北京林业大学', '计算机应用', '13910400825', 'zhibo@bjfu.edu.cn', '在职', '1');
INSERT INTO `teacher_info` VALUES ('12', '650909', '黄心渊', '男', '汉族', null, '100110', '0', '3', '27', '1', '是', '5', null, null, '博士', null, null, null, null, null, null, '在职', '1');
INSERT INTO `teacher_info` VALUES ('13', '550401', '吴保国', '男', '汉族', null, '100110', '28', '4', '27', '1', '是', '5', null, null, '本科', null, null, '北京林业大学', '森林经理学/林业信息管理', '13621224251', 'wubg@bjfu.edu.cn', '在职', '1');
INSERT INTO `teacher_info` VALUES ('14', '610202', '赵天忠', '男', '汉族', null, '100110', '28', '5', '39', '1', '否', '5', null, null, '博士', null, null, '北京林业大学', '资源信息管理/企业信息管理', '13601108182', 'ztz@bjfu.edu.cn', '在职', '1');
INSERT INTO `teacher_info` VALUES ('15', '536656', '王春玲', '女', '汉族', null, '100110', '26', '6', '39', '1', '否', '5', null, null, '博士', null, null, null, null, '13910400825', 'wcl@bjfu.edu.cn', '在职', '1');
INSERT INTO `teacher_info` VALUES ('16', '654654', '齐建东', '男', '汉族', null, '100110', '30', '8', '39', '1', '否', '5', null, null, '博士', null, null, '中国农业大学', null, '', 'qijd@bjfu.edu.cn', '在职', '1');
INSERT INTO `teacher_info` VALUES ('17', '551232', '淮永建', '男', '汉族', null, '100110', '29', '5', '39', '1', '否', '5', null, null, '博士', null, null, null, null, null, 'hyj@bjfu.edu.cn', '在职', '1');
INSERT INTO `teacher_info` VALUES ('18', '654652', '李昀', '男', '汉族', null, '100110', '28', '7', '39', '1', '否', '5', null, null, '博士', null, null, null, null, null, '@bjfu.edu.cn', '在职', '1');
INSERT INTO `teacher_info` VALUES ('19', '654655', '韩静华', null, '汉族', null, '100110', '0', '6', '39', '1', '否', '5', null, null, '博士', null, null, null, null, null, '@bjfu.edu.cn', '在职', '1');
INSERT INTO `teacher_info` VALUES ('20', '461232', '郑云', null, '汉族', null, '100110', '31', '5', '39', '1', '否', '5', null, null, '博士', null, null, null, null, null, '@bjfu.edu.cn', '在职', '1');
INSERT INTO `teacher_info` VALUES ('21', '654654', '郭小平', null, '汉族', null, '100110', '32', '6', '39', '1', '否', '5', null, null, '博士', null, null, null, null, null, '@bjfu.edu.cn', '在职', '1');

-- ----------------------------
-- Table structure for teacher_title
-- ----------------------------
DROP TABLE IF EXISTS `teacher_title`;
CREATE TABLE `teacher_title` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL COMMENT '职称名称',
  `teacher_category_id` int(11) NOT NULL COMMENT '教师所属系列  指向教师类型teacher_type表的id',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teach_type` (`teacher_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_title
-- ----------------------------
INSERT INTO `teacher_title` VALUES ('1', '特设1级', '1', '1');
INSERT INTO `teacher_title` VALUES ('2', '特设2级', '1', '1');
INSERT INTO `teacher_title` VALUES ('3', '教授A1', '1', '1');
INSERT INTO `teacher_title` VALUES ('4', '教授A2', '1', '1');
INSERT INTO `teacher_title` VALUES ('5', '教授A3', '1', '1');
INSERT INTO `teacher_title` VALUES ('6', '教授A4', '1', '1');
INSERT INTO `teacher_title` VALUES ('7', '副教授B1', '1', '1');
INSERT INTO `teacher_title` VALUES ('8', '副教授B2', '1', '1');
INSERT INTO `teacher_title` VALUES ('9', '副教授B3', '1', '1');
INSERT INTO `teacher_title` VALUES ('10', '讲师C1', '1', '1');
INSERT INTO `teacher_title` VALUES ('11', '讲师C2', '1', '1');
INSERT INTO `teacher_title` VALUES ('12', '助教D1', '1', '1');
INSERT INTO `teacher_title` VALUES ('13', '助教D2', '1', '1');
INSERT INTO `teacher_title` VALUES ('14', '正高职A1', '3', '1');
INSERT INTO `teacher_title` VALUES ('15', '正高职A2', '3', '1');
INSERT INTO `teacher_title` VALUES ('16', '正高职A3', '3', '1');
INSERT INTO `teacher_title` VALUES ('17', '副高职B1', '3', '1');
INSERT INTO `teacher_title` VALUES ('18', '副高职B2', '3', '1');
INSERT INTO `teacher_title` VALUES ('19', '副高职B3', '3', '1');
INSERT INTO `teacher_title` VALUES ('20', '中职C1', '3', '1');
INSERT INTO `teacher_title` VALUES ('21', '中职C2', '3', '1');
INSERT INTO `teacher_title` VALUES ('22', '中职C3', '3', '1');
INSERT INTO `teacher_title` VALUES ('23', '初职D1', '3', '1');
INSERT INTO `teacher_title` VALUES ('24', '初职D2', '3', '1');
INSERT INTO `teacher_title` VALUES ('25', '初职D3', '3', '1');
INSERT INTO `teacher_title` VALUES ('26', '正处级A1', '2', '1');
INSERT INTO `teacher_title` VALUES ('27', '正处级A2', '2', '1');
INSERT INTO `teacher_title` VALUES ('28', '正处级A3', '2', '1');
INSERT INTO `teacher_title` VALUES ('29', '副处级B1', '2', '1');
INSERT INTO `teacher_title` VALUES ('30', '副处级B2', '2', '1');
INSERT INTO `teacher_title` VALUES ('31', '副处级B3', '2', '1');
INSERT INTO `teacher_title` VALUES ('32', 'C1', '2', '1');
INSERT INTO `teacher_title` VALUES ('33', 'C2', '2', '1');
INSERT INTO `teacher_title` VALUES ('34', 'C3', '2', '1');
INSERT INTO `teacher_title` VALUES ('35', 'D1', '2', '1');
INSERT INTO `teacher_title` VALUES ('36', 'D2', '2', '1');
INSERT INTO `teacher_title` VALUES ('37', 'D3', '2', '1');
INSERT INTO `teacher_title` VALUES ('38', '助教', '1', '1');
INSERT INTO `teacher_title` VALUES ('39', '  ', '2', '1');

-- ----------------------------
-- Table structure for teacher_type
-- ----------------------------
DROP TABLE IF EXISTS `teacher_type`;
CREATE TABLE `teacher_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(255) NOT NULL COMMENT '1教师，2管理，3其他专技类型，4校外教师',
  `role` varchar(255) NOT NULL,
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_type
-- ----------------------------
INSERT INTO `teacher_type` VALUES ('1', '校级管理员', 'sadmin', '1');
INSERT INTO `teacher_type` VALUES ('2', '院级管理员', 'cadmin', '1');
INSERT INTO `teacher_type` VALUES ('3', '科研院长', 'research_dean', '1');
INSERT INTO `teacher_type` VALUES ('4', '教研室（系）主任', 'department_director', '1');
INSERT INTO `teacher_type` VALUES ('5', '教师', 'normal', '1');

-- ----------------------------
-- Table structure for teach_reform_paper
-- ----------------------------
DROP TABLE IF EXISTS `teach_reform_paper`;
CREATE TABLE `teach_reform_paper` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【教改论文】如果算工作量，或者此论文是否是本院论文，仅看第一作者',
  `paper_name` varchar(255) DEFAULT NULL COMMENT '论文名称',
  `paper_number` int(11) DEFAULT NULL COMMENT '论文编号',
  `journal_name` varchar(255) DEFAULT NULL COMMENT '发表期刊名称',
  `publish_year_month` timestamp NULL DEFAULT NULL COMMENT '发表年月',
  `journal_year` varchar(255) DEFAULT NULL COMMENT '期刊年号',
  `journal_number` varchar(255) DEFAULT NULL COMMENT '期刊期号',
  `journal_volum` varchar(255) DEFAULT NULL COMMENT '期刊卷号',
  `source_project` varchar(255) DEFAULT NULL COMMENT '来源项目',
  `cover_path` varchar(255) DEFAULT NULL COMMENT '封面图片路径',
  `content_path` varchar(255) DEFAULT NULL COMMENT '目录图片路径',
  `text_path` varchar(255) DEFAULT NULL COMMENT '论文路径',
  `cnki_url` varchar(255) DEFAULT NULL COMMENT '中国知网链接',
  `participate_teacher` varchar(255) DEFAULT NULL COMMENT '论文作者 （【教改论文】如果算工作量，或者此论文是否是本院论文，仅看第一作者）',
  `college_id` int(11) DEFAULT NULL COMMENT '所属学院id',
  `status` varchar(40) DEFAULT NULL COMMENT '状态【用户：未提交、待存档、已存档】 ；【管理员：待存档、已存档】',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teach_reform_paper
-- ----------------------------

-- ----------------------------
-- Table structure for teach_reform_project
-- ----------------------------
DROP TABLE IF EXISTS `teach_reform_project`;
CREATE TABLE `teach_reform_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '【教改项目】 由院级管理员导入，教师端不做录入功能',
  `project_name` varchar(255) NOT NULL COMMENT '教改项目名称',
  `project_number` varchar(255) DEFAULT NULL COMMENT '项目编号 例如【X201610022125】',
  `type_child_id` int(11) NOT NULL COMMENT '项目子类型（指向project_type_child)  （项目有类型和子类型，子类关联父类型）',
  `rank_id` int(11) NOT NULL COMMENT '项目所属级别id（指向project_rank表）',
  `college_id` int(11) NOT NULL COMMENT '所属学院id,指向college表的id',
  `begin_year_month` timestamp NULL DEFAULT NULL COMMENT '项目立项时间',
  `mid_check_year_month` timestamp NULL DEFAULT NULL COMMENT '中期检查时间',
  `mid_check_rank` varchar(20) DEFAULT NULL COMMENT '中期检查等级：[优秀、良好、中、合格、不合格]',
  `end_year_month` timestamp NULL DEFAULT NULL COMMENT '项目结项时间\r\n',
  `end_check_rank` varchar(20) DEFAULT NULL COMMENT '结项等级：[优秀、良好、中、合格、不合格]',
  `subject` varchar(80) DEFAULT NULL COMMENT '所属一级学科：工学、管理学、农学、经济学、教育学、其他',
  `host_person` varchar(255) DEFAULT NULL COMMENT '项目负责人',
  `participate_person` varchar(255) DEFAULT NULL COMMENT '参加人',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注信息',
  `grade` varchar(255) DEFAULT NULL COMMENT '项目最终成绩     [优秀、良好、中、合格、不合格]',
  `submit_time` timestamp NOT NULL COMMENT '提交时间',
  `status` varchar(20) DEFAULT NULL COMMENT '状态：立项、中期检查通过、结题',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `project_rank_id` (`rank_id`),
  KEY `college_id_pro` (`college_id`),
  KEY `project_type_child_id` (`type_child_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teach_reform_project
-- ----------------------------

-- ----------------------------
-- Table structure for title_record
-- ----------------------------
DROP TABLE IF EXISTS `title_record`;
CREATE TABLE `title_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` timestamp NOT NULL COMMENT '任职变更时间',
  `teacher_number` varchar(60) NOT NULL COMMENT '授予教师工号',
  `teacher_title_id` int(11) DEFAULT NULL COMMENT '授予的教学职称id',
  `manager_title_id` int(11) DEFAULT NULL COMMENT '授予的教学职称id',
  `using` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teacher_title_id` (`teacher_title_id`),
  KEY `manage_teacher_title_id` (`manager_title_id`),
  KEY `record_teacher_number` (`teacher_number`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of title_record
-- ----------------------------
INSERT INTO `title_record` VALUES ('1', '2008-01-01 09:29:37', '670103', '6', null, '1');
INSERT INTO `title_record` VALUES ('2', '2012-01-01 09:31:33', '670103', '5', null, '1');
