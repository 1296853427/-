const ajax = require('../../utils/ajax.js');
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    currtab: 0,
    swipertab: [{ name: '待付款', index: 0 }, { name: '待取货', index: 1 }, { name: '已取消', index: 2 }],
    alreadyOrder: [],
    waitPayOrder: [],
    lostOrder: [],
    order: [],
    UserID: '',
  },

  /**
   * 生命周期函数--监听页面加载
   */
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
    this.getOrder();
  },
  onReady: function () {
    // 页面渲染完成
    var that = this;
    this.getDeviceInfo()
    this.orderShow()
  },

  getDeviceInfo: function () {
    let that = this
    wx.getSystemInfo({
      success: function (res) {
        that.setData({
          deviceW: res.windowWidth,
          deviceH: res.windowHeight
        })
      }
    })
  },

  /**
  * @Explain：选项卡点击切换
  */
  tabSwitch: function (e) {
    var that = this
    if (this.data.currtab === e.target.dataset.current) {
      return false
    } else {
      that.setData({
        currtab: e.target.dataset.current
      })
    }
  },

  tabChange: function (e) {
    this.setData({ currtab: e.detail.current })
    this.orderShow()
  },

  orderShow: function () {
    let that = this
    switch (this.data.currtab) {
      case 0:
        that.alreadyShow()
        break
      case 1:
        that.waitPayShow()
        break
      case 2:
        that.lostShow()
        break
    }
  },
  alreadyShow: function () {
    this.setData({
      alreadyOrder: [{ name: "a", state: "成功交易", time: "2020/7/25", status: "完成交易", url: "../../images/icon1.jpeg", money: "30.0" }],
    })
  },

  waitPayShow: function () {
    this.setData({
      waitPayOrder: [{ name: "b", state: "待付款", time: "2020/7/6", status: "待付款", url: "../../images/icon1.jpeg", money: "55.6" }],
    })
  },

  lostShow: function () {
    this.setData({
      lostOrder: [{ name: "c", state: "已取消", time: "2020/8/6", status: "从已取消", url: "../../images/icon1.jpeg", money: "6.3" }],
    })
  },
  getOrder: function () {
    var that = this;
    setTimeout(function () {
      //要延时执行的代码
      console.log('user:' + that.data.UserID)
      ajax.request('getOrderByUserID/', { userID: that.data.UserID }, this.DoSuccess, this.DoFail)
    }, 2000) //延迟时间 这里是2秒 

  },
  DoSuccess: function (data) {
    var that = this;
    that.setData({
      order: data
    })
    console.log(data)
  },
  DoFail: function () {
    console.log("fail")
  }
})