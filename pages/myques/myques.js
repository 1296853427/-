const ajax = require('../../utils/ajax.js');
var app = getApp();
Page({

  data: {
    question: [
      {
        "QuestionID": 1,
        "answer_id": 3,
        "feed_source_id": 23,
        "feed_source_name": "Rebecca",
        "feed_source_txt": "赞了回答1",
        "feed_source_img": "../../images/icon1.jpeg",
        "content": "选择 Kindle 而不是纸质书的原因是什么？",
        "answer_ctnt": "难道不明白纸质书更贵啊！！！ 若觉得kindle更贵，我觉得要么阅读量太少，那确实没有买kindle的必要。要么买的都是盗版的纸质书？我不清楚不加以评论。。。 另外，用kindle看小说的怎么真心不懂了...",
        "good_num": "112",
        "comment_num": "18"
      }
    ],
    UserID:'',
  },

  onLoad: function (options) {
    var that = this;
    wx.getStorage({
      key: 'userInfo',
      success: function (res) {
        that.setData({
          UserID: res.data.UserID
        })
        console.log(res)
      }
    });
    setTimeout(function () {
    that.getData();
    },2000)
  },
  getData: function () {
    var that = this;
    ajax.request('getQuestionByUserID/',{userID:that.data.UserID},this.DoSuccess,this.DoFail)
  },
  DoSuccess:function(e){
    var that = this;
    that.setData({
      question:e
    })
  },
  DoFail:function(){
    console.log('fail')
  },
  bindItemTap: function (e) {
    var ques = this.data.question[e.currentTarget.dataset.typeid];
    wx.setStorage({
      key: 'ques',
      data: ques,
      success: function (res) {
        wx.navigateTo({
          url: '../answer/answer'
        })
      }
    })
  },
})