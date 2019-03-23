# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class BookRank(Base):
    __tablename__ = 'book_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(255), nullable=False)


class CertificateRank(Base):
    __tablename__ = 'certificate_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(80), nullable=False)


class ClassInfo(Base):
    __tablename__ = 'class_info'

    id = Column(INTEGER(11), primary_key=True)
    class_name = Column(String(255), nullable=False)
    college_id = Column(INTEGER(11), nullable=False)
    grade = Column(String(60), nullable=False)
    status = Column(String(20), nullable=False)


class College(Base):
    __tablename__ = 'college'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    college_id = Column(String(255), index=True)
    department_num = Column(INTEGER(11))
    teacher_num = Column(INTEGER(11))


class DistributionDesire(Base):
    __tablename__ = 'distribution_desire'

    id = Column(INTEGER(11), primary_key=True)
    college_id = Column(INTEGER(11), nullable=False)
    student_id = Column(INTEGER(11), nullable=False)
    distribution_id = Column(INTEGER(11), nullable=False)
    desire_rank = Column(INTEGER(11), nullable=False)
    submit_time = Column(DateTime, nullable=False)
    status = Column(String(20), nullable=False)


class DistributionInfo(Base):
    __tablename__ = 'distribution_info'

    id = Column(INTEGER(11), primary_key=True)
    college_id = Column(INTEGER(11), nullable=False)
    orientation_ids = Column(String(255), nullable=False)
    num_limit = Column(String(255), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)


class DistributionResult(Base):
    __tablename__ = 'distribution_result'

    id = Column(INTEGER(11), primary_key=True)
    college_id = Column(INTEGER(11), nullable=False)
    student_id = Column(String(80), nullable=False)
    distribution_id = Column(INTEGER(11), nullable=False)
    status = Column(String(255), nullable=False)


class InnovationRank(Base):
    __tablename__ = 'innovation_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(80), nullable=False)


class InvigilateInfo(Base):
    __tablename__ = 'invigilate_info'

    id = Column(INTEGER(11), primary_key=True)
    subject = Column(String(255), nullable=False)
    semester_id = Column(INTEGER(11))
    _class = Column('class', String(255), nullable=False)
    college_id = Column(INTEGER(11), nullable=False)
    exam_time = Column(DateTime)
    location = Column(String(255), nullable=False)
    participate_teacher = Column(String(255), nullable=False)
    submit_time = Column(DateTime, nullable=False)
    status = Column(String(80))


class MajorInfo(Base):
    __tablename__ = 'major_info'

    id = Column(INTEGER(11), primary_key=True)
    major_name = Column(String(255), nullable=False)
    college_id = Column(INTEGER(11), nullable=False)
    department_id = Column(INTEGER(11), nullable=False)


class ProjectRank(Base):
    __tablename__ = 'project_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(255), nullable=False)


class ProjectType(Base):
    __tablename__ = 'project_type'

    id = Column(INTEGER(11), primary_key=True)
    type_name = Column(String(255), nullable=False)
    student_attend = Column(String(20), nullable=False)


class SemesterInfo(Base):
    __tablename__ = 'semester_info'

    id = Column(INTEGER(11), primary_key=True)
    semester_name = Column(String(80), nullable=False)
    status = Column(String(20), nullable=False)


class Student(Base):
    __tablename__ = 'students'

    id = Column(INTEGER(11), primary_key=True)
    student_id = Column(String(255), nullable=False)
    gender = Column(String(20), nullable=False)
    class_id = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    college_id = Column(INTEGER(11), nullable=False)
    gpa = Column(Float(255, True), nullable=False)


class TeachReformPaper(Base):
    __tablename__ = 'teach_reform_paper'

    id = Column(INTEGER(11), primary_key=True)
    paper_name = Column(String(255))
    paper_number = Column(INTEGER(11))
    journal_name = Column(String(255))
    publish_year_month = Column(String(255))
    journal_year = Column(String(255))
    journal_number = Column(String(255))
    college_id = Column(INTEGER(11))
    journal_volum = Column(String(255))
    status = Column(String(40))
    source_project = Column(String(255))
    cover_path = Column(String(255))
    content_path = Column(String(255))
    text_path = Column(String(255))
    cnki_url = Column(String(255))
    participate_teacher = Column(String(255))


class TeacherType(Base):
    __tablename__ = 'teacher_type'

    id = Column(INTEGER(11), primary_key=True)
    type_name = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)


class Book(Base):
    __tablename__ = 'book'

    id = Column(INTEGER(11), primary_key=True)
    book_name = Column(String(255), nullable=False)
    book_number = Column(String(255), nullable=False)
    publish_year_month = Column(String(255), nullable=False)
    pages = Column(INTEGER(11))
    words = Column(INTEGER(11))
    isbn = Column(String(255))
    press = Column(String(100))
    version = Column(String(60), nullable=False)
    style = Column(String(60))
    rank_id = Column(ForeignKey('book_rank.id'), nullable=False, index=True)
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)
    source_project = Column(String(255))
    status = Column(String(255))
    cover_path = Column(String(255))
    copyright_path = Column(String(255))
    content_path = Column(String(255))
    participate_teacher = Column(String(255))
    submit_teacher = Column(String(255), nullable=False)
    submit_time = Column(DateTime)

    college = relationship('College')
    rank = relationship('BookRank')


class Department(Base):
    __tablename__ = 'department'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    number = Column(INTEGER(10))
    director = Column(String(255))
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)

    college = relationship('College')


class InnovationProject(Base):
    __tablename__ = 'innovation_project'

    id = Column(INTEGER(11), primary_key=True)
    project_name = Column(String(255), nullable=False)
    project_number = Column(String(80), nullable=False)
    rank_id = Column(ForeignKey('innovation_rank.id'), nullable=False, index=True)
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)
    begin_year_month = Column(String(255))
    mid_check_year__month = Column('mid_check_year_ month', String(255))
    end_year_month = Column(String(255))
    mid_check_rank = Column(String(50))
    end_check_rank = Column(String(50))
    subject = Column(String(60))
    status = Column(String(60), nullable=False)
    host_student = Column(String(255), nullable=False)
    participant_student = Column(String(255))
    remark = Column(String(255))
    submit_time = Column(DateTime, nullable=False)

    college = relationship('College')
    rank = relationship('InnovationRank')


class ProjectChildType(Base):
    __tablename__ = 'project_child_type'

    id = Column(INTEGER(11), primary_key=True)
    child_type_name = Column(String(255), nullable=False)
    parent_type_id = Column(ForeignKey('project_type.id'), nullable=False, index=True)

    parent_type = relationship('ProjectType')


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(INTEGER(11), primary_key=True)
    number = Column(String(60), nullable=False, index=True)
    password = Column(String(255), nullable=False)
    type = Column(ForeignKey('teacher_type.id'), nullable=False, index=True)

    teacher_type = relationship('TeacherType')


class TeacherTitle(Base):
    __tablename__ = 'teacher_title'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    type_id = Column(ForeignKey('teacher_type.id'), index=True)

    type = relationship('TeacherType')


class InnovationTeacher(Base):
    __tablename__ = 'innovation_teacher'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    project_id = Column(ForeignKey('innovation_project.id'), nullable=False, index=True)

    project = relationship('InnovationProject')
    teacher = relationship('Teacher')


class TeachReformProject(Base):
    __tablename__ = 'teach_reform_project'

    id = Column(INTEGER(11), primary_key=True)
    project_name = Column(String(255), nullable=False)
    project_number = Column(String(255), nullable=False)
    type_child_id = Column(ForeignKey('project_child_type.id'), nullable=False, index=True)
    rank_id = Column(ForeignKey('project_rank.id'), nullable=False, index=True)
    college_id = Column(ForeignKey('college.id'), nullable=False, index=True)
    begin_year__month = Column('begin_year_ month', String(80))
    mid_check_year__month = Column('mid_check_year_ month', String(80))
    end_year_month = Column(String(80))
    mid_check_rank = Column(String(20))
    end_check_rank = Column(String(20))
    subject = Column(String(80))
    status = Column(String(20))
    host_student = Column(String(255))
    participate_student = Column(String(255))
    remark = Column(String(255))
    grade = Column(String(255))
    funds = Column(String(100))
    submit_time = Column(DateTime, nullable=False)

    college = relationship('College')
    rank = relationship('ProjectRank')
    type_child = relationship('ProjectChildType')


class TeacherBook(Base):
    __tablename__ = 'teacher_book'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    book_id = Column(ForeignKey('book.id'), nullable=False, index=True)
    order = Column(String(60))

    book = relationship('Book')
    teacher = relationship('Teacher')


class TeacherInfo(Base):
    __tablename__ = 'teacher_info'

    id = Column(INTEGER(11), primary_key=True)
    number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(20), nullable=False)
    nationality = Column(String(20))
    birth_year_month = Column(String(255))
    department_id = Column(INTEGER(11), nullable=False)
    college_id = Column(INTEGER(11))
    teachertitle_id = Column(ForeignKey('teacher_title.id'), index=True)
    managertitle_id = Column(ForeignKey('teacher_title.id'), index=True)
    type = Column(String(20))
    type_id = Column(ForeignKey('teacher_type.id'), nullable=False, index=True)
    status = Column(String(60))
    work_begin_year_month = Column(String(255))
    bjfu_join_year_month = Column(String(255))
    highest_education = Column(String(255))
    highest_education_accord_year_month = Column(String(255))
    graduate_paper_title = Column(String(255))
    graduate_school = Column(String(255))
    research_direction = Column(String(255))
    telephone = Column(String(60))
    email = Column(String(255))

    managertitle = relationship('TeacherTitle', primaryjoin='TeacherInfo.managertitle_id == TeacherTitle.id')
    teacher = relationship('Teacher')
    teachertitle = relationship('TeacherTitle', primaryjoin='TeacherInfo.teachertitle_id == TeacherTitle.id')
    type1 = relationship('TeacherType')


class TeacherPaper(Base):
    __tablename__ = 'teacher_paper'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    paper_id = Column(ForeignKey('teach_reform_paper.id'), nullable=False, index=True)
    order = Column(String(255), nullable=False)

    paper = relationship('TeachReformPaper')
    teacher = relationship('Teacher')


class TitleRecord(Base):
    __tablename__ = 'title_record'

    id = Column(INTEGER(11), primary_key=True)
    datetime = Column(DateTime, nullable=False)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    teacher_title_id = Column(ForeignKey('teacher_title.id'), nullable=False, index=True)
    manager_title_id = Column(ForeignKey('teacher_title.id'), index=True)

    manager_title = relationship('TeacherTitle', primaryjoin='TitleRecord.manager_title_id == TeacherTitle.id')
    teacher = relationship('Teacher')
    teacher_title = relationship('TeacherTitle', primaryjoin='TitleRecord.teacher_title_id == TeacherTitle.id')


class CertificateInfo(Base):
    __tablename__ = 'certificate_info'

    id = Column(INTEGER(11), primary_key=True)
    certificate_name = Column(String(255), nullable=False)
    ranking = Column(String(50), nullable=False)
    rank_id = Column(ForeignKey('certificate_rank.id'), nullable=False, index=True)
    organize_unit = Column(String(255), nullable=False)
    teacher_number = Column(String(80), nullable=False)
    grant_time = Column(DateTime, nullable=False)
    project_id = Column(ForeignKey('teach_reform_project.id'), index=True)
    type = Column(String(60))
    certificate_pic_path = Column(String(255))
    status = Column(String(255), nullable=False)
    college_id = Column(ForeignKey('college.id'), index=True)
    participate_student = Column(String(255))
    submit_time = Column(DateTime, nullable=False)

    college = relationship('College')
    project = relationship('TeachReformProject')
    rank = relationship('CertificateRank')


class ProjectChangeRecord(Base):
    __tablename__ = 'project_change_record'

    id = Column(INTEGER(11), primary_key=True)
    project_id = Column(ForeignKey('teach_reform_project.id'), nullable=False, index=True)
    reason = Column(String(255), nullable=False)
    change_time = Column(DateTime, nullable=False)
    describe = Column(String(255), nullable=False)

    project = relationship('TeachReformProject')


class TeacherProject(Base):
    __tablename__ = 'teacher_project'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    project_id = Column(ForeignKey('teach_reform_project.id'), nullable=False, index=True)
    participate_type = Column(String(20), nullable=False)

    project = relationship('TeachReformProject')
    teacher = relationship('Teacher')


class TeacherCertificate(Base):
    __tablename__ = 'teacher_certificate'

    id = Column(INTEGER(11), primary_key=True)
    teacher_number = Column(ForeignKey('teacher.number'), nullable=False, index=True)
    certificate_id = Column(ForeignKey('certificate_info.id'), nullable=False, index=True)

    certificate = relationship('CertificateInfo')
    teacher = relationship('Teacher')
