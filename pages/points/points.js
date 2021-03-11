// pages/user/myintegral/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    content: [],
    contents: [],
    ctselect: true,
    point: "0",
    gift: [],
    gifts: [{"ID": 3,
    "image": "../../images/icon1.jpeg",
    "title": "1",
    "price":"a"}],
    giftmsg:{},
    contentmsg:{},
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getPoint();
    this.setData({
      gift: this.data.gifts,
      content: ''
    });
  },
  ctbind: function (e) {
    if (idx == 1) {
      this.setData({
        gift: this.data.gifts,
        content: ''
      })
      
    } else {
      this.setData({
        content: this.data.contents,
        gift: ''
      })
    }
  },
  getPoint: function () {
    var that = this;
    wx.getStorage({
      key: 'points',
      success: function (res) {
        that.setData({
          point: res.data
        })
      },
      fail: function (res) { }
    })
  },
  getGift: function () {
    var that = this;
    wx.request({
      url: '',
      method: 'post',
      data: that.data.giftmsg,
      header: {
        'content-type': 'application/x-www-form-urlencoded'
      },
      success: function (res) {
        that.setData({
          gift: res.data
        })
      },
      fail: function (res) {
        console.log("fail")
      }
    })
  },
  getContent: function () {
    var that = this;
    wx.request({
      url: '',
      method: 'post',
      data: that.data.contentmsg,
      header: {
        'content-type': 'application/x-www-form-urlencoded'
      },
      success: function (res) {
        that.setData({
          content: res.data
        })
      },
      fail: function (res) {
        console.log("fail")
      }
    })
  },
  exchange:function(){
    
  }
})