const ajax = require('../../utils/ajax.js');
var app = getApp();
Page({
  data: {
    query: '',
    hiddenmodalput: true,
    question: [
      {
        "QuestionID": 1,
        "answer_id": 3,
        "feed_source_id": 23,
        "feed_source_name": "Rebecca",
        "feed_source_txt": "赞了回答1",
        "feed_source_img": "../../static/icon/icon1.jpeg",
        "content": "选择 Kindle 而不是纸质书的原因是什么？",
        "answer_ctnt": "难道不明白纸质书更贵啊！！！ 若觉得kindle更贵，我觉得要么阅读量太少，那确实没有买kindle的必要。要么买的都是盗版的纸质书？我不清楚不加以评论。。。 另外，用kindle看小说的怎么真心不懂了...",
        "good_num": "112",
        "comment_num": "18"
      }
    ],
    msg: {
      query: '',
    },

  },
  //事件处理函数

  onLoad: function () {
    console.log('onLoad')
  },
  bindKeyInput: function (e) {
    this.setData({
      query: e.detail.value
    })
    console.log(e)
  },

  getData: function () {
    var that = this;
    that.setData({
      msg: { query: that.data.query }
    })
    ajax.request('questionSearch/', that.data.msg, this.DoSuccess, this.DoFail)
    // wx.request({
    //   url: '',
    //   method: 'post',
    //   data: that.data.msg,
    //   header: {
    //     'content-type': 'application/x-www-form-urlencoded'
    //   },
    //   success: function (res) {
    //     that.setData({
    //       question: res.data
    //     })
    //   },
    //   fail: function (res) {
    //     console.log("fail")
    //   }
    // })
  },
  DoSuccess: function (e) {
    var that = this;
    console.log(e)
    that.setData({
      question: e
    })
  },
  DoFail: function (e) {
    console.log("fail")
  },
  postques: function () {
    wx.navigateTo({
      url: '../postques/postques'
    })
  },
  myQues: function () {
    wx.navigateTo({
      url: '../myques/myques'
    })
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
