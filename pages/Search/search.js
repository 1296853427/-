const ajax = require('../../utils/ajax.js');
var app = getApp();
Page({
  data: {
    query: '',
    book: {},
    books: [],
    hidden: false,
  },
  onLoad: function () {
  },
  bindKeyInput: function (e) {
    this.setData({
      query: e.detail.value
    })
  },
  redirectToDetail: function (e) {
    var Book = this.data.books[e.currentTarget.dataset.typeid];
    console.log(Book)
    wx.setStorage({
      key: 'product',
      data: Book,
      success: function (res) {
        console.log(res.fields)
        wx.navigateTo({
          url: '../product_info/product_info'
        })
      },
      fail: function () {
        console.log("fail")
      }
    })
  },
  fetchBookData: function () {
    var that = this;
    ajax.request('bookSearch/', { name: that.data.query}, this.DoSuccess, this.DoFail)
    // wx.request({
    //   url: app.globalData.host + 'bookSearch/',
    //   method: 'post',
    //   data: {
    //     name: that.data.query
    //   },
    //   header: {
    //     'content-type': 'application/x-www-form-urlencoded'
    //   },

    //   success: function (res) {
    //     that.setData({
    //       books: res.data
    //     })
    //     console.log(that.data.books)
    //   },
    //   fail: function (res) {
    //     console.log("fail")
    //   }
    // })
  },

  DoSuccess:function(e){
    console.log(e)
    var that = this;
    that.setData({
      books:e
    })
  },
  DoFail:function(e){
    console.log("fail")
  }
})