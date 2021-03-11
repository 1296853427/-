const ajax = require('../../utils/ajax.js');
var app = getApp();
Page({
  data: {
    height: 64,
    top: 0,
    scrollH: 0,
    opcity: 0,
    iconOpcity: 0.5,
    pageIndex: 1,
    loadding: false,
    pullUpOn: true,
    point: "",
    UserID: '',
  },
  onLoad: function (options) {
    var that = this;
    let obj = wx.getMenuButtonBoundingClientRect();
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
      that.getPoint();
    }, 2000)
    wx.getSystemInfo({
      success: (res) => {
        this.setData({
          width: obj.left || res.windowWidth,
          height: obj.top ? (obj.top + obj.height + 8) : (res.statusBarHeight + 44),
          top: obj.top ? (obj.top + (obj.height - 32) / 2) : (res.statusBarHeight + 6),
          scrollH: res.windowWidth * 0.6
        })
      }
    })
  },
  href(e) {
    let page = Number(e.currentTarget.dataset.type)
    let url = "";
    switch (page) {
      case 1:
        url = "../Transaction/tran"
        break;
      case 2:
        url = "../points/points"
        break;
      case 3:
        url = "../tipOff/tipOff"
        break;
      case 4:
        url = "../logs/logs"
        break;
      default:
        break;
    }
    if (url) {
      wx.navigateTo({
        url: url
      })
    } else {
      wx.showToast({
        title: "功能尚未完善~",
        icon: "none"
      })
    }
  },
  getPoint: function () {
    var that = this;
    console.log('getPint')
    ajax.request('getCreditByUserID/', { userID: that.data.UserID }, this.DoSuccess, this.DoFail)
  },
  DoSuccess: function (e) {
    var that = this;
    console.log(e)
    that.setData({
      // question:e
    })
  },
  DoFail: function () {
    console.log('fail')
  },
})