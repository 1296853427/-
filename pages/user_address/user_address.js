// pages/user_address/user_address.js
Page({
  data: {
    addressList: []
  },
  onLoad: function (options) {
    
  },
  editAddr(index, addressType) {
    wx.navigateTo({
      url: "../editAddress/editAddress"
    })
  }
})