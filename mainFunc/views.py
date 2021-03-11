import datetime
import json
import os
import re
import random
import requests
import string
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.views.generic.base import View
from rest_framework.decorators import api_view
from mainFunc import models
from mainFunc.models import *


# Create your views here.
def listorders(request):
    return HttpResponse((json.dumps({'res': '1'})))


def imgurl(name):
    return "http://127.0.0.1:8000/ims/img/" + name


@api_view(('GET',))
@csrf_exempt
def read_img(request):
    try:
        # 获取需要展示的图片ID，找到对应的图片
        get_picID = request.data.get('picID')
        tmp = IMG.objects.get(id=get_picID)
        file_name = tmp.name
        return HttpResponse(json.dumps(imgurl(file_name)))
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps(0))


# 保存图片，需要接受保存的图片，保存的图片的文件名，保存的ID（这个是用于区分图片对应数据库那条信息对应的图片的）
@api_view(('POST',))
@csrf_exempt
def uploadImg(request):
    print(1)
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            id=request.data.get('id'),
            name=str(''.join(random.sample(string.ascii_letters + string.digits, 20)))
        )
        print(new_img.id,new_img.name)
        new_img.save()
        with open('../../ims/img', 'wb+') as f:
            f.write(new_img.img.read())
        return HttpResponse((json.dumps({'res': '1'})))


@api_view(('POST',))
@csrf_exempt
def informSend(request):
    if request.method == 'POST':
        # 由上到下依次是获取举报人ID，被举报人ID，举报信息
        get_UserID = request.data.get('UserID'),
        get_toUserID = request.data.get('toUserID'),
        get_content = request.data.get('content'),
        informLetter.objects.create(UserID=int(get_UserID[0]), toUserID=int(get_toUserID[0]),
                                    content=str(get_content[0]))
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


# def CreditsMod(request):


@api_view(('POST',))
@csrf_exempt
def CreditsMod(request):
    # print(request.data)
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        get_change = request.data.get('change'),
        tmp = StudentInfo.objects.get(StudentID=int((get_userID[0])))
        tmp.Credit += int(get_change[0])
        tmp.save(update_fields=['Credit'])
        # print(tmp.Credit)
        print("Success!")
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def BookJudge(request):
    print(request.data)
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        get_bookID = request.data.get('bookID'),
        get_score = request.data.get('score'),
        record = models.bookscore.objects.create(
            BookID=int(get_bookID[0]),
            UserID=int(get_userID[0]),
            score=int(get_score[0]))
        print("Success!")
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


# 书籍推荐功能：传入参数为老师ID、学生ID、书籍ID
# 执行逻辑：首先学生ID正确否(因为老师正常登录故不用验证)，其次验证书籍ID正确否(查询数据库)
#          如果学生ID与书籍ID均正确则向目标学生发送推荐信息(通过写入letter数据库)
# 返回处理结果(成功、失败)
@api_view(('POST',))
@csrf_exempt
def BookReco(request):
    print(request.data)
    if request.method == 'POST':
        get_teacherID = request.data.get('teacherID'),
        get_studentID = request.data.get('studentID'),
        get_bookID = request.data.get('bookID'),
        get_title = request.data.get('title'),
        get_content = request.data.get('content'),
        stu = models.StudentInfo.objects.get(StudentID=int((get_studentID[0])))
        book = models.bookInfo.objects.get(BookID=int((get_bookID[0])))

        if stu and book:
            letter.objects.create(
                From=int(get_teacherID[0]),
                UserID=int(get_studentID[0]),
                Title=get_title[0],
                content=get_content[0])
        else:
            return HttpResponse((json.dumps({'res': '0'})))  # 处理失败，学生或数据不存在
    return HttpResponse((json.dumps({'res': '1'})))


@api_view(('POST',))
@csrf_exempt
def Letter(request):
    stuExist = True
    teaExist = True
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        get_title = request.data.get('title'),
        get_content = request.data.get('content'),
        try:
            stu = StudentInfo.objects.get(StudentID=int((get_userID[0])))
            print('存在学生')
        except:
            print('找不到该学生！')
            stuExist = False

        try:
            tea = TeacherInfo.objects.get(TeacherID=int((get_userID[0])))
            print('存在老师')
        except:
            print('没有该老师！')
            teaExist = False
    if stuExist or teaExist:
        print('Success!')
        record = letter.objects.create(
            UserID=int(get_userID[0]),
            From=0,
            Title=get_title[0],
            content=get_content[0])
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        print('Failed!用户不存在')
        return HttpResponse((json.dumps({'res': '0'})))


# @api_view(('POST',))
# @csrf_exempt
# def CheckBookInfo(request):
#     flag = True
#     if request.method == 'POST':
#         get_bookName = request.data.get('bookName'),
#         try:
#             book = bookInfo.objects.get(Title__contains=get_bookName[0])
#         except:
#             print('没有找到')
#             flag = False
#         if flag:
#             print('Success!')
#             return HttpResponse((json.dumps({'res': '1'})))
#         else:
#             return HttpResponse((json.dumps({'res': '0'})))
#     else:
#         return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def saveQuestion(request):
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        get_content = request.data.get('content'),
        time = datetime.datetime.now(),
        record = Question.objects.create(
            UserID=int(get_userID[0]),
            creditTime=time[0],
            content=get_content[0])
        tmp=Question.objects.get(content=get_content[0])
        return HttpResponse((json.dumps(tmp.QuestionID)))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def Answer(request):
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        get_questionID = request.data.get('questionID'),
        get_content = request.data.get('content'),
        try:
            question = Question.objects.get(QuestionID=int((get_questionID[0])))
        except:
            print('您回答的问题ID不存在')
            return HttpResponse((json.dumps({'res': '0'})))
        record = Answer.objects.create(
            UserID=int(get_userID[0]),
            creditTime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            QuestionID=int(get_questionID[0]),
            content=get_content[0])
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def CreditsEx(request):
    print(request.data)
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        get_presentID = request.data.get('presentID'),
        get_exchangeNum = request.data.get('exchangeNum'),
        user = StudentInfo.objects.get(StudentID=int(get_userID[0]))
        try:
            present = scoreToPresent.objects.get(presentID=int(get_presentID[0]))
        except:
            print('该奖品不存在: 0')
            return HttpResponse((json.dumps({'res': '0'})))

        if int(get_exchangeNum[0]) > present.count:
            print('该奖品剩余数量不足: -1')
            return HttpResponse((json.dumps({'res': '-1'})))
        elif user.Credit < int(get_exchangeNum[0]) * present.score:
            print('该用户剩余积分不足: -2')
            return HttpResponse((json.dumps({'res': '-2'})))
        else:
            # 更新礼物余量和用户剩余积分
            user.Credit -= int(get_exchangeNum[0]) * present.score
            present.count -= int(get_exchangeNum[0])

        # 更新礼物和用户数据库
        user.save(update_fields=['Credit'])
        present.save(update_fields=['count'])

        # 存入数据库
        record = Usergift.objects.create(
            presentID=int(get_presentID[0]),
            UserID=int(get_userID[0]))

        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('GET',))
@csrf_exempt
def FriCreditsGet(request):
    if request.method == 'GET':
        get_userID = request.data.get('userID'),
        student = models.StudentInfo.objects.get(StudentID=int((get_userID[0])))
        # 返回json格式的学生友好度信息
        return HttpResponse(json.dumps(student.FriendCredit))


@api_view(('POST',))
@csrf_exempt
def FriCreditsChange(request):
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        get_change = request.data.get('change'),
        student = StudentInfo.objects.get(StudentID=int((get_userID[0])))
        tmp = student.FriendCredit
        tmp = tmp + int(get_change[0])
        student.FriendCredit = tmp
        student.save(update_fields=['FriendCredit'])
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


# 获取前端信息，创建订单信息，同时向用户发送订单创建成功的信息
@api_view(('POST',))
@csrf_exempt
def SPBookPreorderCreat(request):
    if request.method == 'POST':
        get_name = 1,
        get_phone = request.data.get('phone'),
        get_variety = request.data.get('variety'),
        get_number = 1,
        SPbookpreorder.objects.create(Name=str(get_name[0]), Phone=int(get_phone[0])
                                      , Variety=str(get_variety[0])
                                      , Number=int(get_number[0])
                                      )
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


# 修改一条订货记录
@api_view(('POST',))
@csrf_exempt
def SPBookPreorderMod(request):
    if request.method == 'POST':
        get_preorderID = request.data.get('preorderID'),
        get_name = request.data.get('name'),
        get_phone = request.data.get('phone'),
        get_variety = request.data.get('variety'),
        get_number = request.data.get('number'),
        tmp = SPbookpreorder.objects.get(PrerderID=int((get_preorderID[0])))
        tmp.name = str(get_name[0])
        tmp.phone = int(get_phone[0])
        tmp.variety = str(get_variety[0])
        tmp.number = int(get_number[0])
        tmp.save(update_fields=['name', 'phone', 'variety', 'number'])
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


# 删除某条订货记录
@api_view(('POST',))
@csrf_exempt
def SPBookPreorderDel(request):
    if request.method == 'POST':
        get_preorderID = request.data.get('preorderID'),
        tmp = SPbookpreorder.objects.get(prerderID=int((get_preorderID[0])))
        tmp.delete()
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


# 创建一条书籍出售记录,并返回销售ID
@api_view(('POST',))
@csrf_exempt
def BookReSysCreat(request):
    if request.method == 'POST':
        get_userID = 1,
        get_title = request.data.get('title'),
        bookSell.objects.create(UserID=int(get_userID[0]), Title=str(get_title[0]))
        tmp = bookSell.objects.get(Title=str(get_title[0]))
        return HttpResponse(json.dumps(tmp.sellID))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


# 删除一条销售记录
@api_view(('POST',))
@csrf_exempt
def BookReSysDel(request):
    if request.method == 'POST':
        get_sellID = request.data.get('sellID'),
        tmp = bookSell.objects.get(sellID=int((get_sellID[0])))
        tmp.delete()
        return HttpResponse(json.dumps({'res': '1'}))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


# 下面的算法是用来过滤敏感词汇的
# DFA算法
class DFAFilter():
    def __init__(self):
        self.keyword_chains = {}
        self.delimit = '\x00'

    def add(self, keyword):
        keyword = keyword.lower()
        chars = keyword.strip()
        if not chars:
            return
        level = self.keyword_chains
        for i in range(len(chars)):
            if chars[i] in level:
                level = level[chars[i]]
            else:
                if not isinstance(level, dict):
                    break
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit: 0}
                break
        if i == len(chars) - 1:
            level[self.delimit] = 0

    def parse(self, path):
        with open(path, encoding='utf-8') as f:
            for keyword in f:
                self.add(str(keyword).strip())

    def filter(self, message, repl="*"):
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        ret.append(repl * step_ins)
                        start += step_ins - 1
                        break
                else:
                    ret.append(message[start])
                    break
            else:
                ret.append(message[start])
            start += 1

        return ''.join(ret)


@api_view(('POST',))
@csrf_exempt
def bannedWord(request):
    if request.method == 'POST':
        get_content = request.data.get('content'),
        tmp = DFAFilter()
        path = "mgch.txt"
        tmp.parse(path)
        result = tmp.filter(str(get_content[0]))
        return HttpResponse(json.dumps(result))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def TagCreat(request):
    if request.method == 'POST':
        get_bookId = request.data.get('bookId'),
        get_userId = request.data.get('userId'),
        get_tag = request.data.get('tag'),
        # 如果一本书的标签大于10，那么保存失败
        if (bookTag.objects.count(BookID=int(get_bookId[0])) > 10):
            return HttpResponse((json.dumps({'res': '0'})))
        bookTag.objects.create(BookID=int(get_bookId[0]), UserID=int(get_userId[0]), tag=str(get_tag[0]))
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def ArticleRele(request):
    if request.method == 'POST':
        get_Title = request.data.get('Title'),
        get_Author = request.data.get('Author'),
        get_content = request.data.get('content'),
        userArtical.objects.create(Title=str(get_Title[0]), Author=int(get_Author[0]), content=str(get_content[0]))
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def ArticleDel(request):
    if request.method == 'POST':
        get_Author = request.data.get('Author'),
        get_ArticalID = request.data.get('ArticalID'),
        tmp = userArtical.objects.get(Author=str((get_Author[0])), ArticalID=int(get_ArticalID[0]))
        tmp.delete()
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def orderCreat(request):
    if request.method == 'POST':
        get_userID = 1,
        get_CommodityID = request.data.get('CommodityID'),
        get_CommodityCount = request.data.get('CommodityCount'),
        userOrder.objects.create(UserID=int(get_userID[0]), commodityID=int(get_CommodityID[0]),
                                 commodityCount=int(get_CommodityCount[0]))
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def orderDel(request):
    if request.method == 'POST':
        get_orderID = request.data.get('orderID'),
        tmp = userOrder.objects.get(orderID=int(get_orderID[0]))
        tmp.delete()
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def bookSearch(request):
    if request.method == 'POST':
        user_input = request.data.get('name'),
        tmpCollection = []
        # 循环插入
        for i in range(10000000):
            try:
                tmp = bookInfo.objects.get(BookID=i)
                tmpCollection.append(tmp.Title)
            # 如果找不到bookinfo了话说明书籍已经全部登陆完了
            except:
                break
        pattern = '.*'.join(user_input)
        regex = re.compile(pattern)
        suggestions = []
        for item in tmpCollection:
            match = regex.search(item)  # Checks if the current item matches the regex.
            if match:
                suggestions.append(item)
        res = serializers.serialize("json", bookInfo.objects.filter(Title__in=suggestions))
        return HttpResponse(json.dumps(json.loads(res), ensure_ascii=False),
                            content_type="application/json,charset=utf-8")


@api_view(('GET',))
@csrf_exempt
def randomBook(request):
    if request.method == 'GET':
        res = serializers.serialize("json", bookInfo.objects.order_by('?')[:6])
        return HttpResponse(json.dumps(json.loads(res), ensure_ascii=False),
                            content_type="application/json,charset=utf-8")


@api_view(('POST',))
@csrf_exempt
def getOrderByUserID(request):
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        res = serializers.serialize("json", userOrder.objects.get(UserID=int(get_userID[0])))
        return HttpResponse(json.dumps(json.loads(res), ensure_ascii=False),
                            content_type="application/json,charset=utf-8")


@api_view(('POST',))
@csrf_exempt
def getCreditByUserID(request):
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        res = serializers.serialize("json", StudentInfo.objects.get(UserID=int(get_userID[0])))
        return HttpResponse(json.dumps(json.loads(res), ensure_ascii=False),
                            content_type="application/json,charset=utf-8")


@api_view(('POST',))
@csrf_exempt
def questionSearch(request):
    if request.method == 'POST':
        user_input = request.data.get('name'),
        tmpCollection = []
        # 循环插入
        for i in range(1000000, 1100000):
            try:
                tmp = Question.objects.get(BookID=i)
                tmpCollection.append(tmp.content)
            except:
                break
        pattern = '.*'.join(str(user_input[0]))
        regex = re.compile(pattern)
        suggestions = []
        for item in tmpCollection:
            match = regex.search(item)  # Checks if the current item matches the regex.
            if match:
                suggestions.append(item)
        res = serializers.serialize("json", Question.objects.filter(content__in=suggestions))
        return HttpResponse(json.dumps(json.loads(res), ensure_ascii=False),
                            content_type="application/json,charset=utf-8")


@api_view(('POST',))
@csrf_exempt
def getQuestionByUserID(request):
    if request.method == 'POST':
        get_userID = request.data.get('userID'),
        res = serializers.serialize("json", Question.objects.get(UserID=int(get_userID[0])))
        return HttpResponse(json.dumps(json.loads(res), ensure_ascii=False),
                            content_type="application/json,charset=utf-8")


@api_view(('POST',))
@csrf_exempt
def getOpenid(request):
    if request.method == 'POST':
        code = request.data.get("code")
        url = "https://api.weixin.qq.com/sns/jscode2session"
        url += "?appid=wx96c2b7674bed8855"
        url += "&secret=2d807baaed0d5d5331c75def8c059dc4"
        url += "&js_code=" + code  # 从微信小程序传来的code
        url += "&grant_type=authorization_code"
        r = requests.get(url)
        openid = r.json().get('openid', '')
        return HttpResponse(openid)


@api_view(('POST',))
@csrf_exempt
def studentCreat(request):
    if request.method == 'POST':
        get_openid = request.data.get('openid'),
        get_name = request.data.get('name'),
        get_phone = request.data.get('phone'),
        get_grade = request.data.get('grade'),
        get_school = request.data.get('school'),
        get_classroom = request.data.get('classroom'),
        StudentInfo.objects.create(openid=str(get_openid[0])
                                   , name=str(get_name[0])
                                   , Phone=int(get_phone[0])
                                   , Grade=float(get_grade[0])
                                   , School=str(get_school[0])
                                   , classroom=int(get_classroom[0])
                                   )
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))


@api_view(('POST',))
@csrf_exempt
def teacherCreat(request):
    if request.method == 'POST':
        get_openid = request.data.get('openid'),
        get_name = request.data.get('name'),
        get_phone = request.data.get('phone'),
        get_school = request.data.get('school'),
        TeacherInfo.objects.create(openid=str(get_openid[0])
                                   , name=str(get_name[0])
                                   , Phone=int(get_phone[0])
                                   , School=str(get_school[0]))
        return HttpResponse((json.dumps({'res': '1'})))
    else:
        return HttpResponse((json.dumps({'res': '0'})))

