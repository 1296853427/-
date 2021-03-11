//answer.js

const ajax = require('../../utils/ajax.js');

var app = getApp()
Page({
  data: {
    //comment:[],
    ques: {},
    query: '',
    answer:{
      AnswerID: "1",
      image: "../../images/1444983318907-_DSC1826.jpg",
      UserID: "1",
      creditTime: "2020",
      content: "adada"
    },
    // msg: {
    //   userID: '',
    //   questionID: that.data.ques.QuestionID,
    //   content: that.data.query
    // },
    msg: {
      userID: '1',
      questionID:'1',
      content: '12'
    },
  },
  onLoad: function () {
    console.log('onLoad')
    var that = this
    wx.getStorage({
      key: 'ques',
      success: function (res) {
        that.setData({
          ques: res.data
        })
        console.log(that.data.test)
      }
    })
    this.getComment();
  },
  bindKeyInput: function (e) {
    this.setData({
      query: e.detail.value
    })
    console.log(e)
  },
  getComment: function () {
    var that = this;
    wx.request({
      url: '',
      method: 'post',
      data: {

      },
      header: {
        'content-type': 'application/x-www-form-urlencoded'
      },
      success: function (res) {
        that.setData({
          comments: res.data
        })
      },
      fail: function (res) {
        console.log("fail")
      }
    })
  },
  sendComment: function () {
    var that = this;
    ajax.request('Answer/', this.data.msg, this.DoSuccess, this.DoFail)
    // wx.request({
    //   url: app.globalData+'Answer/',
    //   method: 'post',
    //   data: {
    //     userID:'',
    //     questionID:that.data.ques.QuestionID,
    //     content:that.data.query
    //   },
    //   header: {
    //     'content-type': 'application/x-www-form-urlencoded'
    //   },
    //   success: function (res) {
    //     that.setData({
    //       answer: res.data
    //     })
    //   },
    //   fail: function (res) {
    //     console.log("fail")
    //   }
    // })
  },
  DoSuccess: function (e) {
    console.log(e)
  },
  DoFail: function (e) {

  },
  tipoff:function(){
    var that = this
    wx.navigateTo({
      url: '../tipOff/tipOff?toUserID='+that.data.answer.UserID
    })
  }
})
