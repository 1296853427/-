// pages/share/share.js
Page({

  onShareAppMessage (e) {
    return {
        title: '书籍交易系统',
        path: '/pages/index/index', // 好友点击分享之后跳转到的小程序的页面
        desc: '划时代的书籍购买、中小学题目查询平台',  // 描述
        imageUrl: '../../static/icon/hhh.png'
      }
    },
})