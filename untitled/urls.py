"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from mainFunc import views
from mainFunc.views import *
from untitled import settings

from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orderCreat/', orderCreat),
    # 处理请求： 获取订单信息，创建订单记录
    # 需要参数：
    #           'userID'：产生订单的用户的的userID，int
    #           'CommodityID'：货物的CommodityID，int
    #           'CommodityCount'：货物的数量，int
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('orderDel/', orderDel),
    # 处理请求： 删除一条订单记录
    # 需要参数：
    #           'orderID'：单条订单的orderID，int
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('bookSearch/', bookSearch),
    # 处理请求： 模糊查询书籍名称，并且返回前端
    # 需要参数：
    #           'name'：需要查询的关键词，string
    # 返回参数及含义：
    #           '若干json数据'：前端会获得书籍的所有信息
    #           '0'：代表操作失败


    path('randomBook/', randomBook),
    # 处理请求： 随机返回数据库里面几条书籍记录给前端
    # 需要参数：
    #            无
    # 返回参数及含义：
    #           '若干json数据'：前端会获得几条书籍的所有信息
    #           '0'：代表操作失败


    path('getOrderByUserID/', getOrderByUserID),
    # 处理请求： 通过userid获取该用户所有的订单信息
    # 需要参数：
    #           'userID'：用户的的userID，int
    # 返回参数及含义：
    #           '若干json数据'：前端会获得该用户的所有订单信息
    #           '0'：代表操作失败


    path('getCreditByUserID/', getCreditByUserID),
    # 处理请求： 通过userid获取用户的积分数量
    # 需要参数：
    #           'userID'：用户的的userID，int
    # 返回参数及含义：
    #           'json数据'：代表用户的积分大小
    #           '0'：代表操作失败


    path('questionSearch/', questionSearch),
    # 处理请求： 模糊查询问题名称，并且返回前端
    # 需要参数：
    #           'name'：需要查询的关键词，string
    # 返回参数及含义：
    #           '若干json数据'：前端会获得问题的的所有信息
    #           '0'：代表操作失败


    path('getQuestionByUserID/', getQuestionByUserID),
    # 处理请求： 通过userid获取该用户创建的所有question
    # 需要参数：
    #           'userID'：用户的的userID，int
    # 返回参数及含义：
    #           '若干json数据'：前端会获得问题的的所有信息
    #           '0'：代表操作失败


    path('getOpenid/', getOpenid),
    # 处理请求： 通过前端发送的code，去服务器换取openid病返回
    # 需要参数：
    #           'code'：自动产生的code，string
    # 返回参数及含义：
    #           'openid'：返回的用户的openid
    #           '0'：代表操作失败


    path('studentCreat/', studentCreat),
    # 处理请求： 创建一条学生数据
    # 需要参数：
    #           'openid'：用户的openid，string
    #           'name'：用户的昵称，string
    #           'phone'：用户的联系方式，int
    #           'school'：用户所属的学校，string
    #           'grade'：用户的年级，int 特别备注：小数点前表示年级，0表示幼儿园，1表示小学一年级，以此类推。小数点后0表示上学期，1表示下学期
    #           'classroom'：用户的具体班级号，int
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('teacherCreat/', teacherCreat),
    # 处理请求： 创建一条老师数据
    # 需要参数：
    #           'openid'：用户的openid，string
    #           'name'：用户的昵称，string
    #           'phone'：用户的联系方式，int
    #           'school'：用户所属的学校，string
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败



    path('read_img/', read_img),
    # 处理请求： 返回对应ID的图片地址
    # 需要参数：
    #           'id'：需要取得图片的ID，int
    # 返回参数及含义：
    #           'file_name'：文件的地址
    #           '0'：代表操作失败


    path('uploadImg/', uploadImg),
    # 处理请求： 保存前端发送过来的图片
    # 需要参数：
    #           'img'：发送的图片，文件类型
    #           'id'：图片对应的ID，比如说用户头像就对应userid，书籍图片就对应bookid
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败

    path('informSend/', informSend),
    # 处理请求： 处理用户的举报请求
    # 需要参数：
    #           'UserID'：举报者的ID，int
    #           'toUserID'：被举报者的ID，int
    #           'content'：举报理由，string
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('FriCreditsGet/', FriCreditsGet),
    # 处理请求： 返回给前端对应用户ID的友好度
    # 需要参数：
    #           'userID'：用户的ID，int
    # 返回参数及含义：
    #           'student.FriendCredit'：int类型
    #           '0'：代表操作失败


    path('FriCreditsChange/', FriCreditsChange),
    # 处理请求： 修改对应用户ID的友好度
    # 需要参数：
    #           'userID'：用户的ID
    #           'change'：代表需要修改的积分值(正数代表增加积分，负数代表减少积分)
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('SPBookPreorderCreat/', SPBookPreorderCreat),
    # 处理请求： 添加用户订书记录
    # 需要参数：
    #           'name'：用户姓名，string（注意这里不是用户ID，不要搞错了）
    #           'phone'：联系方式，int
    #           'variety'：需要的物品的名称，string
    #           'number'：数量，int
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('SPBookPreorderMod/', SPBookPreorderMod),
    # 处理请求： 修改用户订书记录
    # 需要参数：
    #           'name'：用户姓名，string（注意这里不是用户ID，不要搞错了）
    #           'phone'：联系方式，int
    #           'variety'：需要的物品的名称，string
    #           'number'：数量，int
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('SPBookPreorderDel/', SPBookPreorderDel),
    # 处理请求： 删除用户订书记录
    # 需要参数：
    #           'preorderID'：订书记录的ID，int
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('BookReSysCreat/', BookReSysCreat),
    # 处理请求： 创建一条二手书籍出售记录,并返回销售ID
    # 需要参数：
    #           'userID'：用户的ID，int
    #           'phone'：联系方式，int
    #           'content'：书写内容，string
    # 返回参数及含义：
    #           'tmp.sellID'：返回自动生成的销售ID
    #           '0'：代表操作失败


    path('BookReSysDel/', BookReSysDel),
    # 处理请求： 删除一条二手书籍出售记录
    # 需要参数：
    #           'sellID'：需要删除的记录的ID，int
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('bannedWord/', bannedWord),
    # 处理请求： 获取发送的信息，将关键词过滤之后返回
    # 需要参数：
    #           'content'：发送的文本内容，string
    # 返回参数及含义：
    #           'result'：修改过的字符串，string
    #           '0'：代表操作失败


    path('TagCreat/', TagCreat),
    # 处理请求： 添加一个书籍标签
    # 需要参数：
    #           'userID'：用户的ID，int
    #           'bookId'：对应添加的书籍的bookId，int
    #           'tag'：标签名称，string
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('ArticleRele/', ArticleRele),
    # 处理请求： 添加用户文章
    # 需要参数：
    #           'Title'：文章标题，string
    #           'Author'：作者的id，int
    #           'content'：文章内容，string
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败

    path('ArticleDel/', ArticleDel),
    # 处理请求： 删除用户文章
    # 需要参数：
    #           'Author'：作者的id，int
    #           'ArticalID'：需要删除的文章的ID，int
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败

    path('CreditsMod/', CreditsMod),
    # 处理请求：修改用户积分，通过此函数可以修改用户的积分
    # 需要参数：
    #           'userID'：int型，用户的ID
    #           'change'：int型，代表需要修改的积分值(正数代表增加积分，负数代表减少积分)
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('BookJudge/', BookJudge),
    # 处理请求：书籍打分，用户可以通过此函数给书籍打分
    # 需要参数：
    #           'userID'：int型，用户的ID
    #           'bookID'：int型，进行打分的目标书籍ID
    #           'score' ：int型，用户给出的评分
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败


    path('BookReco/', BookReco),
    # 处理请求：书籍推荐，老师可以通过此功能给目标学生推荐书籍
    # 需要参数：
    #           'teacherID'：int型，用户的ID
    #           'studentID'：int型，用户给出的评分
    #           'bookID'   ：int型，进行打分的目标书籍ID
    #           'title'    :string型，老师进行推荐时所编辑信息的标题，如"czy同学你好，这是tr老师给你推荐的书籍"
    #           'content'  :string型，老师进行推荐时所编辑信息的内容，如"这本书...,请你在三天内看完并上交2000字读书笔记"
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败(主要由于studentID不存在或bookID不存在)


    path('Letter/', Letter),
    # 处理请求：站内信，管理员可以通过此功能向目标用户进行消息推送
    # 需要参数：
    #           'userID'   ：int型，接受推送的用户的ID(可以是老师也可以是同学)
    #           'title'    :string型，通知的标题，如"积分变动"
    #           'content'  :string型，通知的主要内容，如"XXX你好，由于...您的积分减少XXX，目前您的剩余积分为XXX"
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败(主要由于目标用户不存在)


    # path('CheckBookInfo/', CheckBookInfo),
    # 处理请求：书籍搜索，用户可以通过此功能搜索该书店的目标书籍
    # 需要参数：
    #           'bookName'   ：string型，书籍名字，支持模糊查询，如搜索"三"得到数据库中所有书名中包含"三"的书籍：《三体》、《三体2》...
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败(主要由于数据库中没有所搜的书籍)


    path('saveQuestion/', saveQuestion),
    # 处理请求：提问，用户可以通过此功能发布一个问题
    # 需要参数：
    #           'userID'   ：int型，发出提问的用户ID
    #           'content'  :string型，问题的主要内容
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败(主要由于数据库中没有所搜的书籍)


    path('Answer/', Answer),
    # 处理请求：回答问题，用户可以通过此功能回答问题库中的任何一个问题
    # 需要参数：
    #           'userID'    ：int型，回答问题的用户的ID
    #           'questionID'：int型，所回答的问题的编号(每个问题都有一个编号)
    #           'content'    :string型，回答的主要内容
    # 返回参数及含义：
    #           '1'：代表操作成功
    #           '0'：代表操作失败(主要由于问题ID不存在，及数据中没有该问题)


    path('CreditsEx/', CreditsEx),
    # 处理请求：积分兑换，用户可以通过此功能消耗自己的积分进行礼品兑换
    # 需要参数：
    #           'userID'     ：int型，用户的ID
    #           'presentID'  ：int型，奖品的ID
    #           'exchangeNum' :int型，兑换的数量
    # 返回参数及含义：
    #           '1' ：代表操作成功
    #           '0' ：代表操作失败，原因是该奖品不存在
    #           '-1' :代表操作失败，原因是该奖品剩余数量不足
    #           '-2' :代表操作失败，原因是该用户剩余积分不足

    url(r'^ims/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),

]
