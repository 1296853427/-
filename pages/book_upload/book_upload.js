const ajax = require('../../utils/ajax.js');
const utils = require('../../utils/util.js');
Page({


  data: {
    content: '',
    contact: '',
    formData: ''
  },


  commit(e) {
    console.log(e.detail.value);
    ajax.request('BookReSysCreat/',e.detail.value,this.postSuccess,this.fail)
  },
  postSuccess:function(data){
    wx.showToast({
      title: '上架请求成功',
             })
  },
  fail:function(data){
    console.log(1)

  }
})