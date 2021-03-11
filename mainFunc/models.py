# _*_ coding: utf-8 _*_

# Create your models here.
from django.db import models


# 这个文件里面放的是数据库原型

class IMG(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'IMG'


# 用来存储书籍的基本信息
class bookInfo(models.Model):
    # 书籍编号，这里使用自增,从0000,0000开始
    BookID = models.AutoField(primary_key=True)
    # 书名
    Title = models.CharField(max_length=50, default='暂未确定')
    # 作者
    Author = models.CharField(max_length=20, default='未知')
    # 适合年级上限，第一位表示几年级，幼儿园为0，小学一年级为1，以此类推。小数点后0表示上学期，1表示下学期
    GradeUp = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    # 适合年级下限，第一位表示几年级，幼儿园为0，小学一年级为1，以此类推。小数点后0表示上学期，1表示下学期
    GradeDown = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    # 图片,默认上传到images/book_images文件夹下，默认图片是1.jpg
    image = models.ImageField(upload_to='book_images', max_length=100, default='1.jpg')
    # 书籍定价,为XXX.XX
    Price = models.DecimalField(max_digits=5, decimal_places=2, default=999.99)
    # 折扣,最高精确到小数点后三位，默认是八折(因为实际情况里大多数书是八折出售)
    Discount = models.DecimalField(max_digits=4, decimal_places=3, default=0.800)

    class Meta:
        db_table = 'bookInfo'


# 用来记录书籍的每条打分信息，用来计算书籍得分
class bookscore(models.Model):
    # 书籍编号，这里和上面的boofinfo的编号相同,非空
    BookID = models.IntegerField(blank=False)
    # userID,为学生ID或者老师ID,非空
    UserID = models.IntegerField(blank=False)
    # 用户打的分,需要是一个整数值，非空
    score = models.IntegerField(blank=False)

    class Meta:
        db_table = 'bookscore'


# 书籍标签
class bookTag(models.Model):
    # 书籍编号，这里和上面的bookinfo的编号相同,非空
    BookID = models.IntegerField(blank=False)
    # userID,为学生ID或者老师ID,非空
    UserID = models.IntegerField(blank=False)
    # 用户添加的标签，需要十个字以内
    tag = models.CharField(max_length=10, blank=False)

    class Meta:
        db_table = 'bookTag'


# 这个用来保存用户提交的二手书籍信息
# 这里不存储bookID的原因是，不是所有的书我们都有上架
class bookSell(models.Model):
    # 销售ID，这里采用自增，从5000,0000开始
    sellID = models.AutoField(primary_key=True)
    # 用户ID，也是UserID,为学生ID或者老师ID,非空
    UserID = models.IntegerField(blank=False)
    # 书名
    Title = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = 'bookSell'


# 下面两个是问答系统的数据库
# 这个是问题的数据库
class Question(models.Model):
    # 问题编号，自增生成，从0100,0000开始
    QuestionID = models.AutoField(primary_key=True)
    # 提出者ID，也是UserID,为学生ID或者老师ID,非空
    UserID = models.IntegerField(blank=False)
    # 问题主体
    content = models.CharField(max_length=10000, blank=False)
    # 创建时间，随着用户修改自动更新
    creditTime = models.DateTimeField(auto_now_add=True)
    # 是否解决,0表示未解决，1表示已解决。默认未解决
    isFin = models.IntegerField(default=0)

    class Meta:
        db_table = 'Question'


# 这个是答案的数据库
class Answer(models.Model):
    # 答案编号，自增生成，从0110,0000开始
    AnswerID = models.AutoField(primary_key=True)
    # 问题编号，和上面的问题对应
    QuestionID = models.IntegerField(blank=False)
    # 回答主体
    content = models.CharField(max_length=10000, blank=False)
    # 回答者ID，也是UserID,为学生ID或者老师ID,非空
    UserID = models.IntegerField(blank=False)
    # 创建时间，随着用户修改自动更新
    creditTime = models.DateTimeField(auto_now_add=True)
    # 是否是最佳答案,0表示不是，1表示是。默认不是
    isBest = models.IntegerField(default=0)

    class Meta:
        db_table = 'Answer'


# 这个用来保存举报信息
class informLetter(models.Model):
    # 举报编号，自增生成，从0120,0000开始
    informID = models.AutoField(primary_key=True)
    # 举报人的用户名
    UserID = models.IntegerField(blank=False)
    # 被举报用户的userid
    toUserID = models.IntegerField(blank=False)
    # 内容/举报原因
    content = models.CharField(max_length=500, blank=False)

    class Meta:
        db_table = 'informLetter'


# 用来保存用户发表的文章
class userArtical(models.Model):
    # 文章编号，非空,从0200,0000开始
    ArticalID = models.AutoField(primary_key=True)
    # 文章标题，限制长度在30字符以内，非空
    Title = models.CharField(max_length=50, blank=False)
    # 文章内容，不限制长度
    content = models.CharField(max_length=20000, blank=False)
    # 文章作者，就是相应的UserID，非空
    Author = models.IntegerField(blank=False)

    class Meta:
        db_table = 'userArtical'


class StudentInfo(models.Model):
    # openID,用来存储微信官方ID
    openid = models.CharField(max_length=30)
    # 用户ID，这里使用自增，自增从1000,0000开始
    StudentID = models.AutoField(primary_key=True)
    # 用户名
    name = models.CharField(max_length=20, default='用户名未设置')
    # 手机号,不能为空
    Phone = models.IntegerField(blank=False)
    # 年级，不能为空。小数点前表示年级，0表示幼儿园，1表示小学一年级，以此类推。小数点后0表示上学期，1表示下学期
    Grade = models.DecimalField(max_digits=3, decimal_places=1, blank=False)
    # 学校,不能为空
    School = models.CharField(max_length=20, blank=False)
    # 班级，这里只用填写第几班，因为前面已经有年级了
    classroom = models.IntegerField()
    # 积分
    Credit = models.IntegerField(default=0)
    # 友善度，默认为100,60以下将会被封禁3天，期间无法登陆系统
    FriendCredit = models.IntegerField(default=100)
    # 钱包金额
    Money = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        db_table = 'StudentInfo'


class TeacherInfo(models.Model):
    # openID,用来存储微信官方ID
    openid = models.CharField(max_length=30)
    # 用户ID,这里使用自增，自增从2000,0000开始
    TeacherID = models.AutoField(primary_key=True)
    # 用户名
    name = models.CharField(max_length=20, default='用户名未设置')
    # 手机号
    Phone = models.IntegerField()
    # 学校,或者补习班
    School = models.CharField(max_length=20, default='请填写学校名称')
    # 积分
    Credit = models.IntegerField(default=0)

    class Meta:
        db_table = 'TeacherInfo'


# 这里用来保存老师属于哪个年级，一个老师可以保存多条
class TeacherGradeInfo(models.Model):
    # 用户ID,这里使用自增，自增从2000,0000开始
    TeacherID = models.AutoField(primary_key=True)
    # 年级,这里可以有多个年级,通过逗号隔开,比如说123年级就表示为1,2,3    同样的,0表示幼儿园，1表示小学一年级，以此类推。
    Grade = models.IntegerField()

    class Meta:
        db_table = 'TeacherGradeInfo'


# 这里仅仅是单条进货记录，最后显示时可以根据进货方名称等等进行分组显示
class CatalogInData(models.Model):
    # 订单号，从3000,0000开始
    InID = models.AutoField(primary_key=True)
    # 进货方名称
    Name = models.CharField(max_length=50)
    # 联系方式
    Phone = models.IntegerField()
    # 单个种类名称
    Variety = models.CharField(max_length=50)
    # 单个种类的数量
    Number = models.IntegerField()
    # 折扣,最高精确到小数点后三位
    Discount = models.DecimalField(max_digits=3, decimal_places=3)
    # 总货款，等于单个种类*单独数量*折扣
    Payment = models.DecimalField(max_digits=10, decimal_places=3)
    # 是否结账,0表示未结账，1表示已结账。默认未结账
    Isclear = models.IntegerField(default=0)

    class Meta:
        db_table = 'CatalogInData'


# 这里仅仅是单条出货记录，最后显示时可以根据进货方名称等等进行分组显示
class CatalogOutData(models.Model):
    # 订单号，从3100,0000开始
    OutID = models.AutoField(primary_key=True)
    # 出货方名称
    Name = models.CharField(max_length=50)
    # 联系方式
    Phone = models.IntegerField()
    # 单个种类名称
    Variety = models.CharField(max_length=50)
    # 单个种类的数量
    Number = models.IntegerField()
    # 折扣,最高精确到小数点后三位
    Discount = models.DecimalField(max_digits=3, decimal_places=3)
    # 总货款
    Payment = models.DecimalField(max_digits=10, decimal_places=3)
    # 是否结账,0表示未结账，1表示已结账。默认未结账
    Isclear = models.IntegerField(default=0)

    class Meta:
        db_table = 'CatalogOutData'


# 这里是用来保存单条的订货记录，是为个人设计的
class SPbookpreorder(models.Model):
    # 订单号，从4000,0000开始
    PrerderID = models.AutoField(primary_key=True)
    # 名称
    Name = models.CharField(max_length=50)
    # 联系方式
    Phone = models.IntegerField()
    # 单个种类名称
    Variety = models.CharField(max_length=50)
    # 单个种类的数量
    Number = models.IntegerField()
    # 总价。
    Payment = models.DecimalField(max_digits=10, decimal_places=3)
    # 是否结账,0表示未结账，1表示已结账。默认未结账
    Isclear = models.IntegerField(default=0)
    # 创建时间，随着用户修改自动更新
    creditTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'SPbookpreorder'


# 这个用来保存消息通知
class letter(models.Model):
    # 站内信编号，自增生成，从5000,0000开始
    letterID = models.AutoField(primary_key=True)
    # 收到的用户名
    UserID = models.IntegerField(blank=False)
    # 发件人用户的userid
    From = models.IntegerField(blank=False)
    # 标题
    Title = models.CharField(max_length=50, blank=False)
    # 内容
    content = models.CharField(max_length=500, blank=False)

    class Meta:
        db_table = 'letter'


# 这个用来保存奖品信息
class scoreToPresent(models.Model):
    # 奖品编号，自增生成，从6000,0000开始
    presentID = models.AutoField(primary_key=True)
    # 所需要的积分数量
    score = models.IntegerField()
    # 剩余数量
    count = models.IntegerField()
    # 标题
    Title = models.CharField(max_length=50)
    # 内容
    content = models.CharField(max_length=2000)

    class Meta:
        db_table = 'scoreToPresent'


# 这个用来保存奖品获奖人信息
class Usergift(models.Model):
    # 奖品编号
    presentID = models.AutoField(primary_key=True)
    # 收到的用户名
    UserID = models.IntegerField(blank=False)

    class Meta:
        db_table = 'Usergift'


class bookscore(models.Model):
    # 书籍编号，这里和上面的boofinfo的编号相同,非空
    BookID = models.IntegerField(blank=False)
    # userID,为学生ID或者老师ID,非空
    UserID = models.IntegerField(blank=False)
    # 用户打的分,需要是一个整数值，非空
    score = models.IntegerField(blank=False)

    class Meta:
        db_table = 'bookscore'


class userOrder(models.Model):
    # 订单编号，自增生成，从7000,0000开始
    orderID = models.AutoField(primary_key=True)
    # userID,为学生ID或者老师ID,非空
    UserID = models.IntegerField(blank=False)
    # 商品ID
    commodityID = models.IntegerField(blank=False)
    # 商品数量
    commodityCount = models.IntegerField(blank=False)

    class Meta:
        db_table = 'userOrder'
