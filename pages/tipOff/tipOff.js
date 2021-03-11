const ajax = require('../../utils/ajax.js');
var app = getApp();
Page({

  data: {
    UserID: '',
    content: '',
    toUserID: '',
  },
  onLoad: function (e) {
    var id = parseInt(e.toUserID);
    var that = this;
    this.setData({
      toUserID: id
    })
    wx.getStorage({
      key: 'userInfo',
      success: function (res) {
        that.setData({
          UserID: res.data.UserID
        })
      }
    })
  },
  bindKeyContent: function (e) {
    this.setData({
      content: e.detail.value
    })
  },
  tipoff: function () {
    var that = this;
    setTimeout(function () {
      ajax.request('informSend/', { UserID: that.data.UserID, toUserID: that.data.toUserID, content: that.data.content }, this.DoSuccess, this.DoFail)
    }, 1000)
  },
  DoSuccess: function (e) {
    wx.showToast({
      title: '举报信息已提交',
    })
  },
  DoFail: function (e) {
    console.log("fail")
  }
})