from . import db
from werkzeug.security import check_password_hash
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#from flask import current_app



from sqlalchemy import Column, DateTime, Float, ForeignKey, String, Boolean
from sqlalchemy.dialects.mysql import INTEGER,BIGINT
from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

from app.utils.url_condition.url_condition_mysql import UrlCondition, process_query, count_query, page_query
from app.utils.Error import CustomError
from datetime import datetime


'''
2019.3.15：新增的库
2019.4.29：新增关联
2019.6.9：新增course表、teacher_category表
2019.7.5：弃用，转为model包里面
'''

class BookRank(db.Model):
    __tablename__ = 'book_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(255), nullable=False)

    def __repr__(self):
        return '<BookRank %r>' % self.rank_name

    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class CertificateRank(db.Model):
    __tablename__ = 'certificate_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(80), nullable=False)

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v



class College(db.Model):
    __tablename__ = 'college'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    department_num = Column(INTEGER(11))
    teacher_num = Column(INTEGER(11))

    def __repr__(self):
        return '<College %r>' % self.name

    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class Course(db.Model):
    __tablename__ = 'course'

    id = Column(INTEGER(11), primary_key=True)
    course_name = Column(String(255))
    category = Column(String(20))
    all_teaching_time = Column(INTEGER(11))
    credit = Column(Float(asdecimal=True))
    classes = Column(String(255))
    choose_number = Column(INTEGER(11))
    teacher = Column(String(255))
    submit_time = Column(BIGINT(20))
    college_id = Column(INTEGER(11))



class InnovationRank(db.Model):
    __tablename__ = 'innovation_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(80), nullable=False)

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class ProjectRank(db.Model):
    __tablename__ = 'project_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(255), nullable=False)

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class ProjectType(db.Model):
    __tablename__ = 'project_type'

    id = Column(INTEGER(11), primary_key=True)
    type_name = Column(String(255), nullable=False)
    student_attend = Column(String(20), nullable=False)

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class SemesterInfo(db.Model):
    __tablename__ = 'semester_info'

    id = Column(INTEGER(11), primary_key=True)
    semester_name = Column(String(80), nullable=False)
    status = Column(String(20), nullable=False)

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v




class TeachReformPaper(db.Model):
    __tablename__ = 'teach_reform_paper'

    id = Column(INTEGER(11), primary_key=True)
    paper_name = Column(String(255))
    paper_number = Column(INTEGER(11))
    journal_name = Column(String(255))
    publish_year_month = Column(BIGINT(20))
    journal_year = Column(String(255))
    journal_number = Column(String(255))
    journal_volum = Column(String(255))
    source_project = Column(String(255))
    cover_path = Column(String(255))
    content_path = Column(String(255))
    text_path = Column(String(255))
    cnki_url = Column(String(255))
    participate_teacher = Column(String(255))
    college_id = Column(INTEGER(11))
    status = Column(String(40))

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TeacherCategory(db.Model):
    __tablename__ = 'teacher_category'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TeacherType(db.Model):
    __tablename__ = 'teacher_type'

    id = Column(INTEGER(11), primary_key=True)
    type_name = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class Book(db.Model):
    __tablename__ = 'book'

    id = Column(INTEGER(11), primary_key=True)
    book_name = Column(String(255), nullable=False)
    book_number = Column(String(255))
    publish_year_month = Column(BIGINT(20))
    pages = Column(INTEGER(11))
    words = Column(INTEGER(11))
    isbn = Column(String(255))
    press = Column(String(100))
    version = Column(String(60))
    style = Column(String(60))
    rank_id = Column(ForeignKey('book_rank.id'), index=True)
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)
    source_project = Column(String(255))
    cover_path = Column(String(255))
    copyright_path = Column(String(255))
    content_path = Column(String(255))
    participate_teacher = Column(String(255))
    submit_teacher = Column(String(255), nullable=False)
    submit_time = Column(BIGINT(20))
    status = Column(String(255))

    college = relationship('College')
    rank = relationship('BookRank')

    def __repr__(self):
        return '<Book %r>' % self.book_name

    # def single_to_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    #
    # def dobule_to_dict(self):
    #     result = {}
    #     for key in self.__mapper__.c.keys():
    #         if getattr(self, key) is not None:
    #             result[key] = getattr(self, key)
    #         else:
    #             result[key] = getattr(self, key)
    #     return result

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class ClassInfo(db.Model):
    __tablename__ = 'class_info'

    id = Column(INTEGER(11), primary_key=True)
    class_name = Column(String(255), nullable=False)
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)
    grade = Column(String(60), nullable=False)
    status = Column(String(20), nullable=False)

    college = relationship('College')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v



class Department(db.Model):
    __tablename__ = 'department'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    number = Column(INTEGER(10))
    director = Column(String(255))
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)

    college = relationship('College')

    def __repr__(self):
        return '<Department %r>' % self.name

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

class DistributionInfo(db.Model):
    __tablename__ = 'distribution_info'

    id = Column(INTEGER(11), primary_key=True)
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)
    orientation_name = Column(String(255), nullable=False)
    num_limit = Column(INTEGER(11), nullable=False)
    start_time = Column(BIGINT(20), nullable=False)
    end_time = Column(BIGINT(20), nullable=False)

    college = relationship('College')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

class InnovationProject(db.Model):
    __tablename__ = 'innovation_project'

    id = Column(INTEGER(11), primary_key=True)
    project_name = Column(String(255), nullable=False)
    project_number = Column(String(80), nullable=False)
    rank_id = Column(ForeignKey('innovation_rank.id'), nullable=False, index=True)
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)
    begin_year_month = Column(BIGINT(20))
    mid_check_year_month = Column(BIGINT(20))
    end_year_month = Column(BIGINT(20))
    mid_check_rank = Column(String(50))
    end_check_rank = Column(String(50))
    subject = Column(String(60))
    status = Column(String(60), nullable=False)
    host_student = Column(String(255), nullable=False)
    participant_student = Column(String(255))
    remark = Column(String(255))
    submit_time = Column(BIGINT(20), nullable=False)

    college = relationship('College')
    rank = relationship('InnovationRank')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class ProjectChildType(db.Model):
    __tablename__ = 'project_child_type'

    id = Column(INTEGER(11), primary_key=True)
    child_type_name = Column(String(255), nullable=False)
    parent_type_id = Column(ForeignKey('project_type.id'), nullable=False, index=True)

    parent_type = relationship('ProjectType')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = Column(INTEGER(11), primary_key=True)
    number = Column(String(60), nullable=False, index=True)
    password = Column(String(255), nullable=False)
    type = Column(ForeignKey('teacher_type.id'), nullable=False, index=True)
    using = Column(Boolean, default=True)

    teacher_type = relationship('TeacherType')

    def __repr__(self):
        return '<Teacher %r>' % self.number

    def verify_password(self, password):
        return check_password_hash(self.password, password)  #如果密码正确return true

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TeacherTitle(db.Model):
    __tablename__ = 'teacher_title'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    teacher_category_id = Column(ForeignKey('teacher_category.id'), nullable=False, index=True)

    teacher_category = relationship('TeacherCategory')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

    def __repr__(self):
        return '<TeacherTitle %r>' % self.name

class InnovationTeacher(db.Model):
    __tablename__ = 'innovation_teacher'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    project_id = Column(ForeignKey('innovation_project.id'), nullable=False, index=True)

    project = relationship('InnovationProject')
    teacher = relationship('Teacher')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

class InvigilateInfo(db.Model):
    __tablename__ = 'invigilate_info'

    id = Column(INTEGER(11), primary_key=True)
    apply_teacher = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    subject = Column(ForeignKey('course.id'), nullable=False, index=True)
    semester_id = Column(ForeignKey('semester_info.id'), index=True)
    _class = Column('class', String(255), nullable=False)
    exam_time = Column(BIGINT(20))
    location = Column(String(255), nullable=False)
    participate_teacher = Column(String(255), nullable=False)
    submit_time = Column(BIGINT(20), nullable=False)
    college_id = Column(INTEGER(11), nullable=False)
    status = Column(String(80))

    teacher = relationship('Teacher')
    semester = relationship('SemesterInfo')
    course = relationship('Course')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

class MajorInfo(db.Model):
    __tablename__ = 'major_info'

    id = Column(INTEGER(11), primary_key=True)
    major_name = Column(String(255), nullable=False)
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)
    department_id = Column(ForeignKey('department.id'), nullable=False, index=True)

    college = relationship('College')
    department = relationship('Department')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

class Student(db.Model):
    __tablename__ = 'students'

    id = Column(INTEGER(11), primary_key=True)
    password = Column(String(255), nullable=False)
    name = Column(String(40))
    gender = Column(String(20))
    class_id = Column(ForeignKey('class_info.id'), nullable=False, index=True)
    college_id = Column(INTEGER(11), nullable=False)
    gpa = Column(Float(asdecimal=True), nullable=False)

    _class = relationship('ClassInfo')

    def verify_password(self, password):
        return check_password_hash(self.password, password)  #如果密码正确return true

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

class TeachReformProject(db.Model):
    __tablename__ = 'teach_reform_project'

    id = Column(INTEGER(11), primary_key=True)
    project_name = Column(String(255), nullable=False)
    project_number = Column(String(255))
    type_child_id = Column(ForeignKey('project_child_type.id'), nullable=False, index=True)
    rank_id = Column(ForeignKey('project_rank.id'), nullable=False, index=True)
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)
    begin_year_month = Column(BIGINT(20))
    mid_check_year_month = Column(BIGINT(20))
    mid_check_rank = Column(String(20))
    end_year_month = Column(BIGINT(20))
    end_check_rank = Column(String(20))
    subject = Column(String(80))
    host_student = Column(String(255))
    participate_student = Column(String(255))
    remark = Column(String(255))
    grade = Column(String(255))
    funds = Column(String(100))
    submit_time = Column(BIGINT(20), nullable=False)
    status = Column(String(20))

    college = relationship('College')
    rank = relationship('ProjectRank')
    type_child = relationship('ProjectChildType')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TeacherBook(db.Model):
    __tablename__ = 'teacher_book'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    book_id = Column(ForeignKey('book.id'), nullable=False, index=True)
    order = Column(String(60))

    book = relationship('Book')
    teacher = relationship('Teacher')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TeacherInfo(db.Model):
    __tablename__ = 'teacher_info'

    id = Column(INTEGER(11), primary_key=True)
    number = Column(ForeignKey('teacher.number'), index=True)
    name = Column(String(100))
    gender = Column(String(20))
    nationality = Column(String(20))
    birth_year_month = Column(BIGINT(20))
    college_id = Column(INTEGER(11))
    department_id = Column(INTEGER(11))
    teachertitle_id = Column(ForeignKey('teacher_title.id'), index=True)
    managertitle_id = Column(ForeignKey('teacher_title.id'), index=True)
    teacher_category_id = Column(ForeignKey('teacher_category.id'), index=True)
    type = Column(String(20))
    type_id = Column(ForeignKey('teacher_type.id'), nullable=False, index=True)
    work_begin_year_month = Column(BIGINT(20))
    bjfu_join_year_month = Column(BIGINT(20))
    highest_education = Column(String(255))
    highest_education_accord_year_month = Column(BIGINT(20))
    graduate_paper_title = Column(String(255))
    graduate_school = Column(String(255))
    research_direction = Column(String(255))
    telephone = Column(String(60))
    email = Column(String(255))
    status = Column(String(60))
    using = Column(Boolean, default = True)

    managertitle = relationship('TeacherTitle', primaryjoin='TeacherInfo.managertitle_id == TeacherTitle.id')
    teacher = relationship('Teacher')
    teacher_category = relationship('TeacherCategory')
    teachertitle = relationship('TeacherTitle', primaryjoin='TeacherInfo.teachertitle_id == TeacherTitle.id')
    type1 = relationship('TeacherType')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TeacherPaper(db.Model):
    __tablename__ = 'teacher_paper'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    paper_id = Column(ForeignKey('teach_reform_paper.id'), nullable=False, index=True)
    order = Column(String(255), nullable=False)

    paper = relationship('TeachReformPaper')
    teacher = relationship('Teacher')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TitleRecord(db.Model):
    __tablename__ = 'title_record'

    id = Column(INTEGER(11), primary_key=True)
    datetime = Column(DateTime, nullable=False)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    teacher_title_id = Column(ForeignKey('teacher_title.id'), index=True)
    manager_title_id = Column(ForeignKey('teacher_title.id'), index=True)

    manager_title = relationship('TeacherTitle', primaryjoin='TitleRecord.manager_title_id == TeacherTitle.id')
    teacher = relationship('Teacher')
    teacher_title = relationship('TeacherTitle', primaryjoin='TitleRecord.teacher_title_id == TeacherTitle.id')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

class CertificateInfo(db.Model):
    __tablename__ = 'certificate_info'

    id = Column(INTEGER(11), primary_key=True)
    certificate_name = Column(String(255), nullable=False)
    ranking = Column(String(50), nullable=False)
    rank_id = Column(ForeignKey('certificate_rank.id'), nullable=False, index=True)
    organize_unit = Column(String(255), nullable=False)
    teacher_number = Column(String(80), nullable=False)
    grant_time = Column(BIGINT(20), nullable=False)
    project_id = Column(ForeignKey('teach_reform_project.id'), index=True)
    type = Column(String(60))
    certificate_pic_path = Column(String(255))
    status = Column(String(255), nullable=False)
    college_id = Column(ForeignKey('college.id'), index=True)
    participate_student = Column(String(255))
    submit_time = Column(BIGINT(20), nullable=False)

    college = relationship('College')
    project = relationship('TeachReformProject')
    rank = relationship('CertificateRank')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v



class DistributionDesire(db.Model):
    __tablename__ = 'distribution_desire'

    id = Column(INTEGER(11), primary_key=True)
    college_id = Column(INTEGER(11), nullable=False)
    student_id = Column(ForeignKey('students.id'), nullable=False, index=True)
    distribution_id = Column(INTEGER(11), nullable=False)
    desire_rank = Column(INTEGER(11), nullable=False)
    submit_time = Column(BIGINT(20), nullable=False)
    status = Column(String(20), nullable=False)

    student = relationship('Student')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class DistributionResult(db.Model):
    __tablename__ = 'distribution_result'

    id = Column(INTEGER(11), primary_key=True)
    college_id = Column(INTEGER(11), nullable=False)
    student_id = Column(ForeignKey('students.id'), nullable=False, index=True)
    distribution_id = Column(INTEGER(11), nullable=False)
    status = Column(String(255), nullable=False)

    student = relationship('Student')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v

class ProjectChangeRecord(db.Model):
    __tablename__ = 'project_change_record'

    id = Column(INTEGER(11), primary_key=True)
    project_id = Column(ForeignKey('teach_reform_project.id'), nullable=False, index=True)
    reason = Column(String(255), nullable=False)
    change_time = Column(BIGINT(20), nullable=False)
    describe = Column(String(255), nullable=False)

    project = relationship('TeachReformProject')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TeacherProject(db.Model):
    __tablename__ = 'teacher_project'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    project_id = Column(ForeignKey('teach_reform_project.id'), nullable=False, index=True)
    participate_type = Column(String(20), nullable=False)

    project = relationship('TeachReformProject')
    teacher = relationship('Teacher')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TeacherCertificate(db.Model):
    __tablename__ = 'teacher_certificate'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    certificate_id = Column(ForeignKey('certificate_info.id'), nullable=False, index=True)

    certificate = relationship('CertificateInfo')
    teacher = relationship('Teacher')

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v
