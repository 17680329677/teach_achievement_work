from flask import jsonify, request, current_app, json
from app.api_1_0 import api

import platform,os,uuid
from werkzeug.utils import secure_filename

'''
    公共函数 
    1.文件上传
'''


# 允许上传的图片格式
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png', 'gif'])
# 静态上传文件夹
UPLOAD_FOLDER = 'app/static/uploads'

'''
    判断文件后缀是否在列表中
'''
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


'''
    上传文件
    params ：参数file是文件对象，用file = request.files['file']获得的
    return ：file_name 例：'ffdc8d83-1c96-4154-9ef8-91e039a7869b.jpg'
'''
def fileUpload(file):
    if platform.system() == "Windows":
        slash = '\\'
    else:
        platform.system() == "Linux"
        slash = '/'
    # 判断文件夹是否存在，如果不存在则创建
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    else:
        pass

    # 获取post过来的文件名称，从name=file参数中获取
    file = file
    if file and allowed_file(file.filename):
        # secure_filename方法会去掉文件名中的中文
        filename = secure_filename(file.filename)
        # 因为上次的文件可能有重名，因此使用uuid保存文件
        file_name = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[1]
        #保存文件
        file.save(os.path.join(UPLOAD_FOLDER, file_name))
        #获得基础路径 base_path = os.getcwd() 输出：'D:\\pyWeb\\graduation_design\\Shopping-Cart'
        #获得文件路径 file_path = base_path + slash + app.config['UPLOAD_FOLDER'] + slash + file_name
        #输出 ：'D:\\pyWeb\\graduation_design\\Shopping-Cart\\shop/static/uploads\\445156465.jpg'
        return file_name

'''
    文件上传
'''
@api.route('/common/upload_file', methods=['GET', 'POST'])
def uploadFile():
    file = request.files['file']
    file_name = fileUpload(file)

    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': file_name,
        'reason': '上传成功，文件名：' + file_name
    })

'''
    文件删除
'''
@api.route('/common/delete_file', methods=['GET', 'POST'])
def deleteFile():
    if platform.system() == "Windows":
        slash = '\\'
    else:
        platform.system() == "Linux"
        slash = '/'
    fileName = request.json['file_name']
    fileAddress = UPLOAD_FOLDER + slash +fileName

    if os.path.exists(fileAddress):
        os.remove(fileAddress)
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '删除成功'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '此文件不存在:'+fileAddress
        })