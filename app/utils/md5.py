import hashlib


def get_md5(raw):
    """
    获取raw的md5
    :param raw:
    :return:
    """
    m2 = hashlib.md5()
    m2.update(raw)
    return m2.hexdigest()
