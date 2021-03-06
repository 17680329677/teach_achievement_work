from . import db
from werkzeug.security import check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, primary_key=False, nullable=False)
    password = db.Column(db.String, primary_key=False, nullable=False)
    type = db.Column(db.String, primary_key=False, nullable=False)

    def __init__(self, id, number, password, type):
        self.id = id
        self.number = number
        self.password = password
        self.type = type

    def __repr__(self):
        return '<Teacher %r>' % self.number

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class College(db.Model):
    __tablename__ = 'college'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, primary_key=False, nullable=False)
    college_id = db.Column(db.String, primary_key=False, nullable=False)
    department_num = db.Column(db.Integer, primary_key=False, nullable=True)
    teacher_num = db.Column(db.Integer, primary_key=False, nullable=True)

    def __repr__(self):
        return '<College %r>' % self.name

    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class TeacherInfo(db.Model):
    __tablename__ = 'teacher_info'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, primary_key=False, nullable=False)
    name = db.Column(db.String, primary_key=False, nullable=False)
    gender = db.Column(db.String, primary_key=False, nullable=True)
    nationality = db.Column(db.String, primary_key=False, nullable=True)
    birth_year_month = db.Column(db.String, primary_key=False, nullable=True)
    department_id = db.Column(db.Integer, primary_key=False, nullable=True)
    college_id = db.Column(db.Integer, primary_key=False, nullable=False)
    teachertitle_id = db.Column(db.Integer, primary_key=False, nullable=True)
    managertitle_id = db.Column(db.Integer, primary_key=False, nullable=True)
    type = db.Column(db.String, primary_key=False, nullable=True)
    type_id = db.Column(db.Integer, primary_key=False, nullable=False)
    status = db.Column(db.String, primary_key=False, nullable=True)
    work_begin_year_month = db.Column(db.String, primary_key=False, nullable=True)
    bjfu_join_year_month = db.Column(db.String, primary_key=False, nullable=True)
    highest_education = db.Column(db.String, primary_key=False, nullable=True)
    highest_education_accord_year_month = db.Column(db.String, primary_key=False, nullable=True)
    graduate_paper_title = db.Column(db.String, primary_key=False, nullable=True)
    graduate_school = db.Column(db.String, primary_key=False, nullable=True)
    research_direction = db.Column(db.String, primary_key=False, nullable=True)
    telephone = db.Column(db.String, primary_key=False, nullable=True)
    email = db.Column(db.String, primary_key=False, nullable=True)


class Teacher_Type(db.Model):
    __tablename__ = 'teacher_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String, primary_key=False)
    role = db.Column(db.String, primary_key=False)


class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, primary_key=False, nullable=False)
    number = db.Column(db.String, primary_key=False, nullable=True)
    director = db.Column(db.String, primary_key=False, nullable=True)
    college_id = db.Column(db.Integer, primary_key=False, nullable=False)

    def __init__(self, id, name, number, director, college_id):
        self.id = id
        self.name = name
        self.number = number
        self.director = director
        self.college_id = college_id

    def __repr__(self):
        return '<Department %r>' % self.name


class BookRank(db.Model):
    __tablename__ = 'book_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rank_name = db.Column(db.String, primary_key=False, nullable=False)

    def __repr__(self):
        return '<BookRank %r>' % self.rank_name

    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String, primary_key=False, nullable=False)
    book_number = db.Column(db.String, primary_key=False, nullable=False)
    publish_year_month = db.Column(db.String, primary_key=False, nullable=False)
    pages = db.Column(db.Integer, primary_key=False, nullable=True)
    words = db.Column(db.Integer, primary_key=False, nullable=True)
    isbn = db.Column(db.String, primary_key=False, nullable=False)
    press = db.Column(db.String, primary_key=False, nullable=False)
    version = db.Column(db.String, primary_key=False, nullable=False)
    style = db.Column(db.String, primary_key=False, nullable=False)
    rank_id = db.Column(db.Integer, primary_key=False, nullable=False)
    college_id = db.Column(db.Integer, primary_key=False, nullable=False)
    source_project = db.Column(db.String, primary_key=False, nullable=True)
    status = db.Column(db.String, primary_key=False, nullable=False)
    cover_path = db.Column(db.String, primary_key=False, nullable=True)
    copyright_path = db.Column(db.String, primary_key=False, nullable=True)
    content_path = db.Column(db.String, primary_key=False, nullable=True)
    participate_teacher = db.Column(db.String, primary_key=False, nullable=True)
    submit_teacher = db.Column(db.String, primary_key=False, nullable=False)
    submit_time = db.Column(db.DateTime, primary_key=False, nullable=True)

    def __repr__(self):
        return '<Book %r>' % self.book_name

    # def single_to_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    #
    # def dobule_to_dict(self):
    #     result = {}
    #     for key in self.__mapper__.c.keys():
    #         if getattr(self, key) is not None:
    #             result[key] = str(getattr(self, key))
    #         else:
    #             result[key] = getattr(self, key)
    #     return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v





