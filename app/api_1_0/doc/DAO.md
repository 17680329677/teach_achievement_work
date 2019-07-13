init：mysql会自动转化数据类型

参数：ctx context 表示上下文，但是没有封装context进去，只表示是否使用事务。因为controller层也有这个ctx，controller之间也有互相调用。
参数：ctx 目前只表示是否进行事务
''' 因为DAO 和 Controller层都有同级之间的调用，也确实会有 '''

方法：fomatter做DAO的数据类型转换。仅仅针对于本表中数据出来后做数据转关，只能调用别的DAO的方法进行操作，不可以直接查询。
     DAO的formatter负责包你存的转化成你想要的。
''' 比如课程所属的学期名称，根据课程表中的学期id转换成学期名称返回 '''


类：每个DAO中类所拥有的属性和方法
    __tablename__ = 'tabel_name'
    ziduan = db.Column()
    ziduan = db.Column()
    ......
    
    
    @classmethod
    def reformatter_insert(cls, data: dict)
        
    @classmethod
    def reformatter_update(cls, data: dict)
        
    @classmethod
    def formatter(cls, activity)
    
    