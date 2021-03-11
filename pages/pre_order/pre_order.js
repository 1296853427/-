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
    ajax.request('SPBookPreorderCreat/',e.detail.value,this.postSuccess,this.fail)
  },
  postSuccess:function(data){
    wx.showToast({
      title: '预订提交成功',
             })
  },
  fail:function(data){

  }
})