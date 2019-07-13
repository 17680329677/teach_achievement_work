init：controller可以理解成多个DAO操作的集合，决定什么数据该流入DAO，决定DAO中什么数据该出来


参数：ctx context 表示上下文，但是没有封装context进去，只表示是否使用事务。因为controller层也有这个ctx，controller之间也有互相调用。
参数：ctx 目前只表示是否进行事务
因为DAO 和 Controller层都有同级之间的调用，也确实会有。


方法：fomatter 决定是否传输某个字段或者即使增加一个表中没有的字段。 
     DAO的formatter负责决定增加减少。