const ajax = require('../../utils/ajax.js');
var app = getApp();
Page({

  data: {
    content: '',
    imgID: '',
    imgs: [],
    a: {
      userID: '1',
      // content:that.data.content
      content: 'abc'
    },
    mytempFilePaths: '',
  },


  onLoad: function (options) {

  },
  bindKeyContent: function (e) {
    this.setData({
      content: e.detail.value
    })
  },
  uploader: function () {
    var that = this;
    let imagesList = [];
    let maxSize = 1024 * 1024;
    let maxLength = 1;
    let flag = true;
    wx.chooseImage({
      count: 3, //最多可以选择的图片总数
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        wx.showToast({
          title: '正在上传...',
          icon: 'loading',
          mask: true,
          duration: 500
        })
        for (let i = 0; i < res.tempFiles.length; i++) {
          if (res.tempFiles[i].size > maxSize) {
            flag = false;
            console.log(111)
            wx.showModal({
              content: '图片太大，不允许上传',
              showCancel: false,
              success: function (res) {
                if (res.confirm) {
                  console.log('用户点击确定')
                }
              }
            });
          }
        }
        if (res.tempFiles.length > maxLength) {
          console.log('222');
          wx.showModal({
            content: '最多能上传' + maxLength + '张图片',
            showCancel: false,
            success: function (res) {
              if (res.confirm) {
                console.log('确定');
              }
            }
          })
        }
        if (flag == true && res.tempFiles.length <= maxLength) {
          that.setData({
            imagesList: res.tempFilePaths
          })
        }
        that.setData({
          mytempFilePaths: res.tempFilePaths[0]
        })
        console.log(that.data.mytempFilePaths)
      },
      fail: function (res) {
      }
    })
  },
  tipoff: function () {
    var that = this;
    ajax.request('saveQuestion/', that.data.a, this.conSuccess, this.DoFail)
  },
  conSuccess: function (res) {
    console.log(this.data.a)
    var that = this;
    console.log('imgid')
    setTimeout(function () {
      console.log(res)
    that.setData({
      imgID: res//改称对应id
    });
    console.log(that.data.imgID)
    
    wx.uploadFile({
      url: app.globalData.host + 'uploadImg/',
      filePath: that.data.mytempFilePaths,
      name: that.data.imgID,
      formData: {
        id: that.data.imgID,
      },
      header: {
        "Content-Type": "multipart/form-data",
      },
      success: function (data) {
        wx.switchTab({
          url: '../Question/ques',
        })
        console.log(data);
      },
      fail: function (data) {
        console.log(data);
      }
    })
  }, 2000)
  },
  DoFail: function () {
    console.log("fail")
  }
})