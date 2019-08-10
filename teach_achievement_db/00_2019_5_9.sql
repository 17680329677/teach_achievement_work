/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : teach_achievement

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2019-05-09 16:36:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '（展示）',
  `book_name` varchar(255) NOT NULL COMMENT '教材名称（展示）',
  `book_number` varchar(255) NOT NULL COMMENT '教材编号（展示）鉴于部分数据ISBN丢失，因此系统需自动生成论文编号',
  `publish_year_month` bigint(20) NOT NULL COMMENT '出版年月',
  `pages` int(11) DEFAULT NULL COMMENT '教材页数',
  `words` int(11) DEFAULT NULL COMMENT '总字数',
  `isbn` varchar(255) DEFAULT NULL COMMENT '出版的书籍的 ISBN号 （展示）',
  `press` varchar(100) DEFAULT NULL COMMENT '出版社（展示）',
  `version` varchar(60) NOT NULL COMMENT '教材版本   (新编，修订，译本)',
  `style` varchar(60) DEFAULT NULL COMMENT '出版形式    1文字，2电子，\r\n3文字+电子\r\n',
  `rank_id` int(11) NOT NULL COMMENT '教材级别，指向book_rank表的id（展示）',
  `college_id` int(11) NOT NULL COMMENT '所属学院id （指向college表的id，而不是college_id）',
  `source_project` varchar(255) DEFAULT NULL COMMENT '来源项目',
  `status` varchar(255) DEFAULT NULL COMMENT '状态【1.地编辑状态、2.待审批状态、3.立项状态】',
  `cover_path` varchar(255) DEFAULT NULL COMMENT '封面图片路径',
  `copyright_path` varchar(255) DEFAULT NULL COMMENT '版权页图片路径',
  `content_path` varchar(255) DEFAULT NULL COMMENT '目录图片路径',
  `participate_teacher` varchar(255) DEFAULT NULL COMMENT '参与教师（多个）',
  `submit_teacher` varchar(255) NOT NULL COMMENT '提交教师（工号）',
  `submit_time` bigint(20) DEFAULT NULL COMMENT '提交时间（展示）',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `rank_id` (`rank_id`),
  KEY `book_college_id` (`college_id`),
  CONSTRAINT `book_college_id` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`),
  CONSTRAINT `rank_id` FOREIGN KEY (`rank_id`) REFERENCES `book_rank` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES ('1', 'java web基础', '123123', '20180101000000', '500', '50', 'KB-826698', '人民教育出版社', '新编', '文字', '1', '10', '国家级项目', '1', 'http://img12.360buyimg.com/n1/jfs/t3118/82/6138623695/29784/bc7dab00/589c5513N88c62571.jpg', 'http://image5.suning.cn/uimg/b2c/newcatentries/0070083569-000000000101961340_2_800x800.jpg', 'http://image5.suning.cn/uimg/b2c/newcatentries/0070083569-000000000101961340_2_800x800.jpg', ';杜何哲;李启巍;朱玉;', '7180266', '20190221104655');
INSERT INTO `book` VALUES ('2', 'java 基础', '123123', '20180101000000', '500', '50', 'KB-826698', '人民教育出版社', '新编', '文字', '1', '10', '国家级项目', '1', null, null, null, null, '7180266', '20190221104655');
INSERT INTO `book` VALUES ('3', 'python web基础', '3333333333333', '20180101000000', '500', '50', 'KB-826698', '人民教育出版社', '新编', '文字', '4', '10', '国家级项目', '2', '', '', '', null, '7180266', '20190221104655');
INSERT INTO `book` VALUES ('4', 'python 基础++++', '123123', '20180101000000', '500', '50', 'KB-826698', '人民教育出版社', '新编', '文字', '1', '10', '国家级项目', '2', '', '', null, null, '7180278', '20190221104655');

-- ----------------------------
-- Table structure for book_rank
-- ----------------------------
DROP TABLE IF EXISTS `book_rank`;
CREATE TABLE `book_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(255) NOT NULL COMMENT '教材等级',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of book_rank
-- ----------------------------
INSERT INTO `book_rank` VALUES ('1', '国家级精品教材');
INSERT INTO `book_rank` VALUES ('2', '北京市精品教材');
INSERT INTO `book_rank` VALUES ('3', '校级教材');
INSERT INTO `book_rank` VALUES ('4', '“十一五”规划教材');
INSERT INTO `book_rank` VALUES ('5', '“十二五”规划教材');

-- ----------------------------
-- Table structure for certificate_info
-- ----------------------------
DROP TABLE IF EXISTS `certificate_info`;
CREATE TABLE `certificate_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `certificate_name` varchar(255) NOT NULL COMMENT '证书名称',
  `ranking` varchar(50) NOT NULL COMMENT '获奖等级',
  `rank_id` int(11) NOT NULL COMMENT '证书级别id（指向certificate_rank表的id）',
  `organize_unit` varchar(255) NOT NULL COMMENT '组织单位',
  `teacher_number` varchar(80) NOT NULL COMMENT '教师工号',
  `grant_time` bigint(20) NOT NULL COMMENT '证书发放时间',
  `project_id` int(11) DEFAULT NULL COMMENT '依托项目的id，指向teach_reform_project（可以不依托项目）',
  `type` varchar(60) DEFAULT NULL COMMENT '证书类型（教师证书或学生证书）',
  `certificate_pic_path` varchar(255) DEFAULT NULL COMMENT '证书图片路径',
  `status` varchar(255) NOT NULL COMMENT '状态【1.地编辑状态、2.待审批状态、3.入库状态】',
  `college_id` int(11) DEFAULT NULL COMMENT '所属学院id ( 不知道是否一定属于某个学院，可为空 )',
  `participate_student` varchar(255) DEFAULT NULL COMMENT '参与学生',
  `submit_time` bigint(20) NOT NULL COMMENT '提交时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cetification_rank_id` (`rank_id`),
  KEY `tea_ref_project_id` (`project_id`),
  KEY `tea_college_id` (`college_id`),
  CONSTRAINT `cetification_rank_id` FOREIGN KEY (`rank_id`) REFERENCES `certificate_rank` (`id`),
  CONSTRAINT `tea_college_id` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`),
  CONSTRAINT `tea_ref_project_id` FOREIGN KEY (`project_id`) REFERENCES `teach_reform_project` (`id`)
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
  `rank_name` varchar(80) NOT NULL COMMENT '证书级别名称 如：1国家级 2北京市',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of certificate_rank
-- ----------------------------
INSERT INTO `certificate_rank` VALUES ('1', '国家级一等奖');
INSERT INTO `certificate_rank` VALUES ('2', '国家级二等奖');
INSERT INTO `certificate_rank` VALUES ('3', '国家级三等奖');
INSERT INTO `certificate_rank` VALUES ('4', '省级一等奖');
INSERT INTO `certificate_rank` VALUES ('5', '省级二等奖');
INSERT INTO `certificate_rank` VALUES ('6', '省级三等奖');
INSERT INTO `certificate_rank` VALUES ('7', '市级一等奖');
INSERT INTO `certificate_rank` VALUES ('8', '市级二等奖');
INSERT INTO `certificate_rank` VALUES ('9', '市级三等奖');
INSERT INTO `certificate_rank` VALUES ('10', '校级一等奖');
INSERT INTO `certificate_rank` VALUES ('11', '校级二等奖');
INSERT INTO `certificate_rank` VALUES ('12', '校级三等奖');

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
  PRIMARY KEY (`id`) USING BTREE,
  KEY `class_college` (`college_id`),
  CONSTRAINT `class_college` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of class_info
-- ----------------------------
INSERT INTO `class_info` VALUES ('1', '信息一班', '10', '2018', '1');

-- ----------------------------
-- Table structure for college
-- ----------------------------
DROP TABLE IF EXISTS `college`;
CREATE TABLE `college` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '学院名称',
  `department_num` int(11) DEFAULT NULL,
  `teacher_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of college
-- ----------------------------
INSERT INTO `college` VALUES ('1', '林学院', '1', '1');
INSERT INTO `college` VALUES ('2', '水土保持学院', '4', '23');
INSERT INTO `college` VALUES ('3', '生物科学与技术学院', '6', '44');
INSERT INTO `college` VALUES ('4', '园林学院', '2', '32');
INSERT INTO `college` VALUES ('5', '经济管理学院', '5', '32');
INSERT INTO `college` VALUES ('6', '工学院', '6', '12');
INSERT INTO `college` VALUES ('7', '材料科学与技术学院', '9', '34');
INSERT INTO `college` VALUES ('8', '人文社会科学学院', '4', '32');
INSERT INTO `college` VALUES ('9', '外语学院', '6', '24');
INSERT INTO `college` VALUES ('10', '信息学院', '3', '1');
INSERT INTO `college` VALUES ('11', '理学院', '6', '5');
INSERT INTO `college` VALUES ('12', '自然保护区学院', '4', '7');
INSERT INTO `college` VALUES ('13', '环境科学与工程学院', '6', '42');
INSERT INTO `college` VALUES ('14', '艺术设计学院', '5', '24');
INSERT INTO `college` VALUES ('15', '马克思主义学院', '4', '32');
INSERT INTO `college` VALUES ('16', '继续教育学院', '3', '11');

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL COMMENT '教研室名称',
  `number` int(10) unsigned zerofill DEFAULT NULL COMMENT '教研室人数， 每次查询教研室的时候会更新教研室数量',
  `director` varchar(255) DEFAULT NULL COMMENT '教研室主任工号',
  `college_id` int(255) NOT NULL COMMENT '所属学院id',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `college_id` (`college_id`) USING BTREE,
  CONSTRAINT `college_id` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES ('22', 'test1', '0000000000', '7180278', '10');
INSERT INTO `department` VALUES ('23', '软件工程教研室', '0000000002', '7180208', '10');
INSERT INTO `department` VALUES ('24', '特色同时3', '0000000000', '7180266', '10');
INSERT INTO `department` VALUES ('25', '特色同时3', '0000000001', '7180266', '10');
INSERT INTO `department` VALUES ('27', 'new2', '0000000001', '7180288', '10');

-- ----------------------------
-- Table structure for distribution_desire
-- ----------------------------
DROP TABLE IF EXISTS `distribution_desire`;
CREATE TABLE `distribution_desire` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college_id` int(11) NOT NULL COMMENT '所属学院id',
  `student_id` int(11) NOT NULL COMMENT '学生学号',
  `distribution_id` int(11) NOT NULL COMMENT '方向',
  `desire_rank` int(11) NOT NULL COMMENT '志愿顺序，区分第一、第二..志愿',
  `submit_time` bigint(20) NOT NULL COMMENT '提交时间',
  `status` varchar(20) NOT NULL COMMENT '状态，是否确认分流结果【1.是、0。否】',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `desire_stu` (`student_id`),
  CONSTRAINT `desire_stu` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`)
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
  `orientation_name` varchar(255) NOT NULL COMMENT '分流方向（专业）名称',
  `num_limit` varchar(255) NOT NULL COMMENT '人数限制',
  `start_time` bigint(20) NOT NULL COMMENT '开始时间',
  `end_time` bigint(20) NOT NULL COMMENT '结束时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `distribution_college` (`college_id`),
  CONSTRAINT `distribution_college` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`)
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
  `status` varchar(255) NOT NULL COMMENT '状态',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `result_stu` (`student_id`),
  CONSTRAINT `result_stu` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of distribution_result
-- ----------------------------

-- ----------------------------
-- Table structure for innovation_project
-- ----------------------------
DROP TABLE IF EXISTS `innovation_project`;
CREATE TABLE `innovation_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(255) NOT NULL COMMENT '项目名称',
  `project_number` varchar(80) NOT NULL COMMENT '项目编号',
  `rank_id` int(11) NOT NULL COMMENT '大创项目等级id 指向innovation_rank的id',
  `college_id` int(11) NOT NULL COMMENT '所属学院id 指向college表的id',
  `begin_year_month` bigint(20) DEFAULT NULL COMMENT '立项年月',
  `mid_check_year_month` bigint(20) DEFAULT NULL COMMENT '中期检查年月',
  `end_year_month` bigint(20) DEFAULT NULL COMMENT '结项年月',
  `mid_check_rank` varchar(50) DEFAULT NULL COMMENT '中期检查等级',
  `end_check_rank` varchar(50) DEFAULT NULL COMMENT '结项成绩',
  `subject` varchar(60) DEFAULT NULL COMMENT '所属一级学科',
  `status` varchar(60) NOT NULL COMMENT '状态【1.地编辑状态、2.待审批状态、3.立项状态】',
  `host_student` varchar(255) NOT NULL COMMENT '主持学生',
  `participant_student` varchar(255) DEFAULT NULL COMMENT '参与学生（多个）',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `submit_time` bigint(20) NOT NULL COMMENT '提交时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `innovation_rank_id` (`rank_id`),
  KEY `innovation_college_id` (`college_id`),
  CONSTRAINT `innovation_college_id` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`),
  CONSTRAINT `innovation_rank_id` FOREIGN KEY (`rank_id`) REFERENCES `innovation_rank` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of innovation_project
-- ----------------------------
INSERT INTO `innovation_project` VALUES ('1', '测试大创项目', '100000001', '1', '10', '1530374400000', '1559750400000', '1565712000000', 'ok啊', '100', 'test', '2', '***学生', '***学生,***学生,***学生', 'beizhu 备注s++++', '1565712000000');

-- ----------------------------
-- Table structure for innovation_rank
-- ----------------------------
DROP TABLE IF EXISTS `innovation_rank`;
CREATE TABLE `innovation_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(80) NOT NULL COMMENT '大创项目等级',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of innovation_rank
-- ----------------------------
INSERT INTO `innovation_rank` VALUES ('1', '国家级');
INSERT INTO `innovation_rank` VALUES ('2', '省级');
INSERT INTO `innovation_rank` VALUES ('3', '市级+');

-- ----------------------------
-- Table structure for innovation_teacher
-- ----------------------------
DROP TABLE IF EXISTS `innovation_teacher`;
CREATE TABLE `innovation_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_number` varchar(80) NOT NULL COMMENT '教师工号',
  `project_id` int(11) NOT NULL COMMENT '项目id',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `innovation_teacher_number` (`teacher_number`),
  KEY `innovation_project_id` (`project_id`),
  CONSTRAINT `innovation_project_id` FOREIGN KEY (`project_id`) REFERENCES `innovation_project` (`id`),
  CONSTRAINT `innovation_teacher_number` FOREIGN KEY (`teacher_number`) REFERENCES `teacher` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of innovation_teacher
-- ----------------------------
INSERT INTO `innovation_teacher` VALUES ('1', '5000010', '1');

-- ----------------------------
-- Table structure for invigilate_info
-- ----------------------------
DROP TABLE IF EXISTS `invigilate_info`;
CREATE TABLE `invigilate_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `apply_teacher` varchar(255) NOT NULL COMMENT '申请教师的工号',
  `subject` varchar(255) NOT NULL COMMENT '考试科目',
  `semester_id` int(11) DEFAULT NULL COMMENT '所属学期id',
  `class` varchar(255) NOT NULL COMMENT '班级（多个id）',
  `college_id` int(11) NOT NULL COMMENT '所属学院id',
  `exam_time` bigint(20) DEFAULT NULL COMMENT '考试时间',
  `location` varchar(255) NOT NULL COMMENT '考试地点',
  `participate_teacher` varchar(255) NOT NULL COMMENT '参与监考教师（如果申请人参与了监考，那就包含申请人。统计监考次数的时候只统计participate_teacher中的。因为申请人有可能没参加监考。）',
  `submit_time` bigint(20) NOT NULL COMMENT '提交时间',
  `status` varchar(80) DEFAULT NULL COMMENT '状态【1.地编辑状态、2.待审批状态、3.立项状态】',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `invigilate_semester` (`semester_id`),
  KEY `invigilate_teacher` (`apply_teacher`),
  CONSTRAINT `invigilate_semester` FOREIGN KEY (`semester_id`) REFERENCES `semester_info` (`id`),
  CONSTRAINT `invigilate_teacher` FOREIGN KEY (`apply_teacher`) REFERENCES `teacher` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of invigilate_info
-- ----------------------------
INSERT INTO `invigilate_info` VALUES ('1', '5000010', '测试科目', '1', '1', '10', '1556640000000', '二教楼', '5000010,7180266,5003,7180278,7180288', '1556899200000', '3');
INSERT INTO `invigilate_info` VALUES ('2', '5000010', '测2', '1', '1', '10', '1556899200000', '1', '5000010,7180266', '1556899200000', '3');

-- ----------------------------
-- Table structure for major_info
-- ----------------------------
DROP TABLE IF EXISTS `major_info`;
CREATE TABLE `major_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `major_name` varchar(255) NOT NULL COMMENT '专业名称（方向）',
  `college_id` int(11) NOT NULL COMMENT '所属学院id',
  `department_id` int(11) NOT NULL COMMENT '所属教研室id',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `major_department` (`department_id`),
  KEY `major_college` (`college_id`),
  CONSTRAINT `major_college` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`),
  CONSTRAINT `major_department` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`)
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
  `change_time` bigint(20) NOT NULL COMMENT '变更时间',
  `describe` varchar(255) NOT NULL COMMENT '项目描述（根据用户填写的信息自动生成）',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teach_reform_project_id` (`project_id`),
  CONSTRAINT `teach_reform_project_id` FOREIGN KEY (`project_id`) REFERENCES `teach_reform_project` (`id`)
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
  PRIMARY KEY (`id`) USING BTREE,
  KEY `project_type_id` (`parent_type_id`),
  CONSTRAINT `project_type_id` FOREIGN KEY (`parent_type_id`) REFERENCES `project_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of project_child_type
-- ----------------------------
INSERT INTO `project_child_type` VALUES ('1', '教改项目子类型1', '1');
INSERT INTO `project_child_type` VALUES ('2', '教改项目子类型2', '1');
INSERT INTO `project_child_type` VALUES ('3', '创新训练项目子类型1', '2');
INSERT INTO `project_child_type` VALUES ('4', '创新训练项目子类型2', '2');

-- ----------------------------
-- Table structure for project_rank
-- ----------------------------
DROP TABLE IF EXISTS `project_rank`;
CREATE TABLE `project_rank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_name` varchar(255) NOT NULL COMMENT '项目级别名称',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of project_rank
-- ----------------------------
INSERT INTO `project_rank` VALUES ('1', '级别一');
INSERT INTO `project_rank` VALUES ('2', '级别二');
INSERT INTO `project_rank` VALUES ('3', '级别三');
INSERT INTO `project_rank` VALUES ('5', '新添加的教改项目等级名称');

-- ----------------------------
-- Table structure for project_type
-- ----------------------------
DROP TABLE IF EXISTS `project_type`;
CREATE TABLE `project_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(255) NOT NULL COMMENT '类型名称 ,用户根据实际情况配置(如1、教改项目2、创新创业训练项目)',
  `student_attend` varchar(20) NOT NULL COMMENT '是否为学生参与的项目',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of project_type
-- ----------------------------
INSERT INTO `project_type` VALUES ('1', '教改项目', '否');
INSERT INTO `project_type` VALUES ('2', '创新创业训练项目', '是');

-- ----------------------------
-- Table structure for semester_info
-- ----------------------------
DROP TABLE IF EXISTS `semester_info`;
CREATE TABLE `semester_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `semester_name` varchar(80) NOT NULL COMMENT '学期名称',
  `status` varchar(20) NOT NULL COMMENT '学期状态（系统中是否可选）',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of semester_info
-- ----------------------------
INSERT INTO `semester_info` VALUES ('1', '2019-2020年第一学期', '正在进行(已生效)');
INSERT INTO `semester_info` VALUES ('2', '2019-2020年第二学期', '(未生效)');

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
  `gpa` double(255,0) NOT NULL COMMENT '大一学年gpa',
  PRIMARY KEY (`id`),
  KEY `stu_class` (`class_id`),
  CONSTRAINT `stu_class` FOREIGN KEY (`class_id`) REFERENCES `class_info` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES ('15008023', '123456', null, '男', '1', '4');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(60) NOT NULL COMMENT '教师工号',
  `password` varchar(255) NOT NULL COMMENT '密码',
  `type` int(11) NOT NULL COMMENT '教师类型（1-系统管理员、2-学院管理员、3、普通教师）',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teacher_teach_type` (`type`),
  KEY `number` (`number`),
  CONSTRAINT `teacher_teach_type` FOREIGN KEY (`type`) REFERENCES `teacher_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('1', '7280278', 'pbkdf2:sha256:50000$iVuYIAgB$c55f7337cf770fd3bb0c1e66c779a3e1ad60a650d768562b2226fc58c775f8df', '1');
INSERT INTO `teacher` VALUES ('2', '7180278', 'pbkdf2:sha256:50000$ZOJdcV7b$d76d628248542c020e927f6e0d2c7a69a7e2e6aa2a1c25bd2506f6819bba51d8', '1');
INSERT INTO `teacher` VALUES ('3', '7180288', 'pbkdf2:sha256:50000$7Ep9NKFI$3bd5f0b3dbf37b177274bf6de07670d5a4c8f332cf738fb3d54c0a74d575d3b7', '2');
INSERT INTO `teacher` VALUES ('4', '7180298', 'pbkdf2:sha256:50000$dxUfhM1Y$b1a45429ba71ca9b303b4e6ceb0e2ff904ee0ca8f2444af9b1c0abbc8c3b2934', '3');
INSERT INTO `teacher` VALUES ('5', '7180208', 'pbkdf2:sha256:50000$jduVozhc$0bf691732f0d2559c7531fd697f45fee22c307f590755fac91d95b0fde9d2189', '4');
INSERT INTO `teacher` VALUES ('6', '7180266', 'pbkdf2:sha256:50000$bnC9a9rU$4a403554017d4bafaaf3f7e4302635c7575314f14bf4c1512922ae46d70ad67c', '5');
INSERT INTO `teacher` VALUES ('7', '5000010', 'pbkdf2:sha256:50000$bnC9a9rU$4a403554017d4bafaaf3f7e4302635c7575314f14bf4c1512922ae46d70ad67c', '5');
INSERT INTO `teacher` VALUES ('8', '5002', 'pbkdf2:sha256:50000$4kRibY4d$1dc5d9ad4054eab1b53f3c0792a131d0528a83144bd19c7432ea890f2991b402', '5');
INSERT INTO `teacher` VALUES ('9', '5003', 'pbkdf2:sha256:50000$4kRibY4d$1dc5d9ad4054eab1b53f3c0792a131d0528a83144bd19c7432ea890f2991b402', '5');

-- ----------------------------
-- Table structure for teacher_book
-- ----------------------------
DROP TABLE IF EXISTS `teacher_book`;
CREATE TABLE `teacher_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_number` varchar(60) NOT NULL COMMENT '教师工号 ( 指向teacher表的number)',
  `book_id` int(11) NOT NULL COMMENT '教材id 指向book表的id',
  `order` varchar(60) DEFAULT NULL COMMENT '作者顺序（通过作者顺序，确定主编、副主编、参编、主译、副主译、参译，0-6数字记录）',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teacher_number` (`teacher_number`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `book_id` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`),
  CONSTRAINT `teacher_number` FOREIGN KEY (`teacher_number`) REFERENCES `teacher` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_book
-- ----------------------------
INSERT INTO `teacher_book` VALUES ('1', '7180266', '1', '1');
INSERT INTO `teacher_book` VALUES ('2', '7180266', '2', '1');
INSERT INTO `teacher_book` VALUES ('3', '7180266', '3', '1');
INSERT INTO `teacher_book` VALUES ('4', '7180278', '4', '1');

-- ----------------------------
-- Table structure for teacher_certificate
-- ----------------------------
DROP TABLE IF EXISTS `teacher_certificate`;
CREATE TABLE `teacher_certificate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_number` varchar(255) NOT NULL COMMENT '教师工号 指向teacher表的id',
  `certificate_id` int(11) NOT NULL COMMENT '证书id，指向certificate_info的id',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `tea_number` (`teacher_number`),
  KEY `certificate_id` (`certificate_id`),
  CONSTRAINT `certificate_id` FOREIGN KEY (`certificate_id`) REFERENCES `certificate_info` (`id`),
  CONSTRAINT `tea_number` FOREIGN KEY (`teacher_number`) REFERENCES `teacher` (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_certificate
-- ----------------------------

-- ----------------------------
-- Table structure for teacher_info
-- ----------------------------
DROP TABLE IF EXISTS `teacher_info`;
CREATE TABLE `teacher_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(60) NOT NULL COMMENT '教师工号;校内老师，必有字段.',
  `name` varchar(100) NOT NULL COMMENT '教师姓名',
  `gender` varchar(20) NOT NULL COMMENT '性别（文字）',
  `nationality` varchar(20) DEFAULT NULL COMMENT '民族',
  `birth_year_month` bigint(20) DEFAULT NULL COMMENT '出生年月',
  `department_id` int(11) NOT NULL COMMENT '所属教研室id，初始化默认为0，表示未分配,等待学院管理员分配',
  `college_id` int(11) DEFAULT NULL COMMENT '所属学院id',
  `teachertitle_id` int(11) DEFAULT NULL COMMENT '对应教师职称表id (指向teacher_title表的id), 功能：教师|非教师系列职称',
  `managertitle_id` int(11) DEFAULT NULL COMMENT '指向teacher_title表的id 功能：增加管理级别职称 。如果是双肩挑，就有第二个职称(管理职称)',
  `type` varchar(20) DEFAULT NULL COMMENT '是否为“双肩挑”；值：【1/0】；默认为0 (否)；',
  `type_id` int(11) NOT NULL COMMENT '指向teacher_type表的id',
  `status` varchar(60) DEFAULT NULL COMMENT '教师在职/非在职；值：【1/0】',
  `work_begin_year_month` bigint(20) DEFAULT NULL COMMENT '参加工作年月',
  `bjfu_join_year_month` bigint(20) DEFAULT NULL COMMENT '入校年月',
  `highest_education` varchar(255) DEFAULT NULL COMMENT '最高学历（博士后、博士、硕士、研究生同等、本科、大专、）',
  `highest_education_accord_year_month` bigint(20) DEFAULT NULL COMMENT '最高学历取得年月',
  `graduate_paper_title` varchar(255) DEFAULT NULL COMMENT '毕业论文题目（用户不再需要，这里做保留；前台做隐藏，目前没有用过）',
  `graduate_school` varchar(255) DEFAULT NULL COMMENT '毕业院校',
  `research_direction` varchar(255) DEFAULT NULL COMMENT '研究方向',
  `telephone` varchar(60) DEFAULT NULL COMMENT '联系方式',
  `email` varchar(255) DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `number` (`number`) USING BTREE,
  KEY `teachertitle_id` (`teachertitle_id`),
  KEY `managertitle_id` (`managertitle_id`),
  KEY `teacher_type_id` (`type_id`),
  CONSTRAINT `managertitle_id` FOREIGN KEY (`managertitle_id`) REFERENCES `teacher_title` (`id`),
  CONSTRAINT `number` FOREIGN KEY (`number`) REFERENCES `teacher` (`number`),
  CONSTRAINT `teacher_type_id` FOREIGN KEY (`type_id`) REFERENCES `teacher_type` (`id`),
  CONSTRAINT `teachertitle_id` FOREIGN KEY (`teachertitle_id`) REFERENCES `teacher_title` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_info
-- ----------------------------
INSERT INTO `teacher_info` VALUES ('1', '7180278', 'wukunze+', '男', '汉族', '199', '0', '10', '1', '1', '1', '5', '1', '2010', '201', '博士', '201', '《机器学习》', '北京林业大学', '机器学习', '18510363933', '18510363933@163.com');
INSERT INTO `teacher_info` VALUES ('9', '7180288', '杜何哲', '男', '汉族', '199', '27', '10', '1', '1', '1', '2', '1', '540', '201', '博士', '20', '《机器学习》', '北京林业大学', '机器学习', '18510363933', '18510363933@163.com');
INSERT INTO `teacher_info` VALUES ('20', '7180208', '二分法', '男', '汉族', '19', '23', '10', '1', '1', '1', '4', '1', null, null, null, null, null, null, null, '18510363933', '18510363933@163.com');
INSERT INTO `teacher_info` VALUES ('21', '7180266', '普通66', '男', '汉族', '196', '25', '10', '1', '1', '1', '5', '1', null, null, null, null, null, null, null, '18510363933', '18510363933@163.com');
INSERT INTO `teacher_info` VALUES ('22', '5000010', '普通教师2', '女', null, null, '10', '10', null, null, '0', '5', '1', null, null, null, null, null, null, null, null, null);
INSERT INTO `teacher_info` VALUES ('23', '5002', '普通教师3号', '女', '1', '1', '23', '10', '1', '1', '1', '5', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `teacher_info` VALUES ('27', '5003', '测试教师5号', '男', null, null, '0', '10', '1', '2', '1', '5', '在编', null, null, null, null, null, null, null, null, null);

-- ----------------------------
-- Table structure for teacher_paper
-- ----------------------------
DROP TABLE IF EXISTS `teacher_paper`;
CREATE TABLE `teacher_paper` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_number` varchar(255) NOT NULL COMMENT '教师工号 指向teacher表的number',
  `paper_id` int(11) NOT NULL COMMENT '教改论文id,指向teach_reform_paper表的id',
  `order` varchar(255) NOT NULL COMMENT '教师参与名次',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teacher_id` (`teacher_number`),
  KEY `paper_id` (`paper_id`),
  CONSTRAINT `paper_id` FOREIGN KEY (`paper_id`) REFERENCES `teach_reform_paper` (`id`),
  CONSTRAINT `teacher_id` FOREIGN KEY (`teacher_number`) REFERENCES `teacher` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_paper
-- ----------------------------
INSERT INTO `teacher_paper` VALUES ('1', '5000010', '1', '1');

-- ----------------------------
-- Table structure for teacher_project
-- ----------------------------
DROP TABLE IF EXISTS `teacher_project`;
CREATE TABLE `teacher_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_number` varchar(80) NOT NULL COMMENT '教师工号 指向teacher表的teacher_number',
  `project_id` int(11) NOT NULL COMMENT '所属教改项目id  指向teach_reform_project的id',
  `participate_type` varchar(20) NOT NULL COMMENT '参与类型（负责人、参与人）',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teacher_reform_project_id` (`project_id`),
  KEY `the_teacher_number` (`teacher_number`),
  CONSTRAINT `teacher_reform_project_id` FOREIGN KEY (`project_id`) REFERENCES `teach_reform_project` (`id`),
  CONSTRAINT `the_teacher_number` FOREIGN KEY (`teacher_number`) REFERENCES `teacher` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_project
-- ----------------------------
INSERT INTO `teacher_project` VALUES ('1', '5000010', '1', '主持');

-- ----------------------------
-- Table structure for teacher_title
-- ----------------------------
DROP TABLE IF EXISTS `teacher_title`;
CREATE TABLE `teacher_title` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL COMMENT '职称名称',
  `type_id` int(11) DEFAULT NULL COMMENT '教师所属系列  指向教师类型teacher_type表的id',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teach_type` (`type_id`),
  CONSTRAINT `teach_type` FOREIGN KEY (`type_id`) REFERENCES `teacher_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_title
-- ----------------------------
INSERT INTO `teacher_title` VALUES ('1', '校级管理-职称A', '1');
INSERT INTO `teacher_title` VALUES ('2', '校级管理-职称B', '1');
INSERT INTO `teacher_title` VALUES ('3', '院级管理-职称A', '2');
INSERT INTO `teacher_title` VALUES ('4', '院级行政-职称A+', '2');
INSERT INTO `teacher_title` VALUES ('5', '教师-教学-职称A', '5');
INSERT INTO `teacher_title` VALUES ('6', '教师-教学-职称A+', '5');
INSERT INTO `teacher_title` VALUES ('7', '科研院长-职称A++', '3');
INSERT INTO `teacher_title` VALUES ('8', '教研室（系）主任-职称A++', '4');
INSERT INTO `teacher_title` VALUES ('13', '教师测试', '5');

-- ----------------------------
-- Table structure for teacher_type
-- ----------------------------
DROP TABLE IF EXISTS `teacher_type`;
CREATE TABLE `teacher_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(255) NOT NULL COMMENT '1教师，2管理，3其他专技类型，4校外教师',
  `role` varchar(255) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teacher_type
-- ----------------------------
INSERT INTO `teacher_type` VALUES ('1', '校级管理员', 'sadmin');
INSERT INTO `teacher_type` VALUES ('2', '教务秘书', 'cadmin');
INSERT INTO `teacher_type` VALUES ('3', '科研院长', 'research_dean');
INSERT INTO `teacher_type` VALUES ('4', '教研室（系）主任', 'department_director');
INSERT INTO `teacher_type` VALUES ('5', '教师', 'normal');

-- ----------------------------
-- Table structure for teach_reform_paper
-- ----------------------------
DROP TABLE IF EXISTS `teach_reform_paper`;
CREATE TABLE `teach_reform_paper` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paper_name` varchar(255) DEFAULT NULL COMMENT '论文名称',
  `paper_number` int(11) DEFAULT NULL COMMENT '论文编号',
  `journal_name` varchar(255) DEFAULT NULL COMMENT '发表期刊名称',
  `publish_year_month` bigint(20) DEFAULT NULL COMMENT '发表年月',
  `journal_year` varchar(255) DEFAULT NULL COMMENT '期刊年号',
  `journal_number` varchar(255) DEFAULT NULL COMMENT '期刊期号',
  `college_id` int(11) DEFAULT NULL COMMENT '所属学院id',
  `journal_volum` varchar(255) DEFAULT NULL COMMENT '期刊卷号',
  `status` varchar(40) DEFAULT NULL COMMENT '状态【1.地编辑状态、2.待审批状态、3.立项状态】',
  `source_project` varchar(255) DEFAULT NULL COMMENT '来源项目',
  `cover_path` varchar(255) DEFAULT NULL COMMENT '封面图片路径',
  `content_path` varchar(255) DEFAULT NULL COMMENT '目录图片路径',
  `text_path` varchar(255) DEFAULT NULL COMMENT '论文路径',
  `cnki_url` varchar(255) DEFAULT NULL COMMENT '中国知网链接',
  `participate_teacher` varchar(255) DEFAULT NULL COMMENT '参与教师',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teach_reform_paper
-- ----------------------------
INSERT INTO `teach_reform_paper` VALUES ('1', '测试论文', '10000010', '11111', '1489507200000', '11111', '111', '10', '111', '2', '3123123', '0f78813a-1aaf-4efc-b09e-f59c9fab5d93.jpg', 'c68eb414-408d-4294-8459-284ce5a0befb.jpg', '论文本身	形式不做限制？？？ 文件路径/URL？？待定', 'http://testUrl', 'fdaadf,adsfasdf,afdasdf');

-- ----------------------------
-- Table structure for teach_reform_project
-- ----------------------------
DROP TABLE IF EXISTS `teach_reform_project`;
CREATE TABLE `teach_reform_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(255) NOT NULL COMMENT '教改项目名称',
  `project_number` varchar(255) NOT NULL COMMENT '项目编号',
  `type_child_id` int(11) NOT NULL COMMENT '项目子类型（指向project_type_child)  （项目有类型和子类型，子类关联父类型）',
  `rank_id` int(11) NOT NULL COMMENT '项目所属级别id（指向project_rank表）',
  `college_id` int(11) NOT NULL COMMENT '所属学院id,指向college表的id',
  `begin_year_month` bigint(20) DEFAULT NULL COMMENT '项目立项时间',
  `mid_check_year_month` bigint(20) DEFAULT NULL COMMENT '中期检查时间',
  `end_year_month` bigint(20) DEFAULT NULL COMMENT '项目结项时间\r\n',
  `mid_check_rank` varchar(20) DEFAULT NULL COMMENT '中期检查等级： 1优 2良 3中 4合格 5不合格',
  `end_check_rank` varchar(20) DEFAULT NULL COMMENT '结项等级：  1优 2良 3中 4合格 5不合格',
  `subject` varchar(80) DEFAULT NULL COMMENT '所属一级学科：1工学 2管理学 3农学 4经济学 5教育学 6其他',
  `status` varchar(20) DEFAULT NULL COMMENT '状态：1本地编辑 2待审批 3立项 4中期检查通过 5结题 6存档',
  `host_student` varchar(255) DEFAULT NULL COMMENT '项目主持学生',
  `participate_student` varchar(255) DEFAULT NULL COMMENT '参与学生',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注信息',
  `grade` varchar(255) DEFAULT NULL COMMENT '项目最终成绩',
  `funds` varchar(100) DEFAULT NULL COMMENT '最终审批经费',
  `submit_time` bigint(20) NOT NULL COMMENT '信息提交时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `project_rank_id` (`rank_id`),
  KEY `college_id_pro` (`college_id`),
  KEY `project_type_child_id` (`type_child_id`),
  CONSTRAINT `college_id_pro` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`),
  CONSTRAINT `project_rank_id` FOREIGN KEY (`rank_id`) REFERENCES `project_rank` (`id`),
  CONSTRAINT `project_type_child_id` FOREIGN KEY (`type_child_id`) REFERENCES `project_child_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of teach_reform_project
-- ----------------------------
INSERT INTO `teach_reform_project` VALUES ('1', '测试教改项目', '10000001', '1', '1', '10', '1546272000000', '1553097600000', '1558540800000', 'good', 'good', 'test', '3', '15008023', '1500802,1500803,1500804', '备注备注备注', '100', '0', '20190502002143');

-- ----------------------------
-- Table structure for title_record
-- ----------------------------
DROP TABLE IF EXISTS `title_record`;
CREATE TABLE `title_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` datetime NOT NULL COMMENT '职称授予时间',
  `teacher_number` varchar(60) NOT NULL COMMENT '授予教师工号',
  `teacher_title_id` int(11) DEFAULT NULL COMMENT '授予的教学职称id',
  `manager_title_id` int(11) DEFAULT NULL COMMENT '授予的教学职称id',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `teacher_title_id` (`teacher_title_id`),
  KEY `manage_teacher_title_id` (`manager_title_id`),
  KEY `record_teacher_number` (`teacher_number`),
  CONSTRAINT `manage_teacher_title_id` FOREIGN KEY (`manager_title_id`) REFERENCES `teacher_title` (`id`),
  CONSTRAINT `record_teacher_number` FOREIGN KEY (`teacher_number`) REFERENCES `teacher` (`number`),
  CONSTRAINT `teacher_title_id` FOREIGN KEY (`teacher_title_id`) REFERENCES `teacher_title` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Records of title_record
-- ----------------------------
INSERT INTO `title_record` VALUES ('1', '2019-03-15 20:01:15', '7180278', '1', '2');
INSERT INTO `title_record` VALUES ('2', '2019-03-15 20:01:57', '7180278', '2', '1');
INSERT INTO `title_record` VALUES ('3', '2019-04-29 16:05:03', '7180288', '1', null);
INSERT INTO `title_record` VALUES ('4', '2019-04-29 16:05:20', '7180288', null, '4');
INSERT INTO `title_record` VALUES ('5', '2019-04-24 00:00:00', '5002', null, '2');
