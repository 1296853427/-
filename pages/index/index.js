//index.js
//获取应用实例
const ajax = require('../../utils/ajax.js');
const utils = require('../../utils/util.js');
var app = getApp()
Page({
  data: {
    navbar: ['全新书籍', '闲置书籍'],
    currentTab: 0,
    // banner
    imgUrls: [
      'http://127.0.0.1:8000/ims/img/1.jpg',
      'http://127.0.0.1:8000/ims/img/2.jpg',
      'http://127.0.0.1:8000/ims/img/3.jpg'
           //服务器图片的url
    ],
    indicatorDots: true, //是否显示面板指示点
    autoplay: true, //是否自动切换
    thisinterval: 3000, //图片自动切换时间间隔,3s
    duration: 1000, //  滑动动画时长1s
    /*顶部小按钮*/
    navItems: [
      {
        typeId: 0,
        name: '书籍搜索',
        url: 'bill',
        imageurl: '../../static/icon/search.png',
      },
      {
        typeId: 1,
        name: '新书预订',
        url: 'bill',
        imageurl: '../../static/icon/dingdan.png',
      },
      {
        typeId: 2,
        name: '积分兑换',
        url: 'bill',
        imageurl: '../../static/icon/lihe.png'
      },
      {
        typeId: 3,
        name: '有奖推荐',
        url: 'bill',
        imageurl: '../../static/icon/fenxiang.png'
      }
    ],

    navItems_old: [
      {
        typeId: 0,
        name: '书籍搜索',
        url: 'bill',
        imageurl: '../../static/icon/search.png',
      },
      {
        typeId: 1,
        name: '上架书籍',
        url: 'bill',
        imageurl: '../../static/icon/yulebao.png',
      },
      {
        typeId: 2,
        name: '书籍讨论',
        url: 'bill',
        imageurl: '../../static/icon/tishi.png'
      },
      {
        typeId: 3,
        name: '有奖推荐',
        url: 'bill',
        imageurl: '../../static/icon/fenxiang.png'
      }
    ],

    recommendItems: [
      {
        goodId: null,
        name: null,
        url:null,
        imageurl: null,
        price: null,
      },
      {
        goodId: null,
        name: null,
        url:null,
        imageurl: null,
        price: null,
      },
      {
        goodId: null,
        name: null,
        url:null,
        imageurl: null,
        price: null,
      },
      {
        goodId: null,
        name: null,
        url:null,
        imageurl: null,
        price: null,
      },
      {
        goodId: null,
        name: null,
        url:null,
        imageurl: null,
        price: null,
      },
      {
        goodId: null,
        name: null,
        url:null,
        imageurl: null,
        price: null,
      }
    ],
    book:[],
    /*中奖小广告*/
    text: '恭喜小王同学获得pilot钢笔一支',
    marqueePace: 2.5,//滚动速度
    marqueeDistance: 0,//初始滚动距离
    size: 14,
    orientation: 'left',//滚动方向
    interval: 20, // 时间间隔
    adUrl: '../../static/icon/badge.png',
  },
 onShow: function (success) {
   // 页面显示
   var that = this;
   var length = that.data.text.length * that.data.size;//文字长度
   var windowWidth = wx.getSystemInfoSync().windowWidth;// 屏幕宽度
  //  ajax.getData('read_img/',this.imgsuccess,this.fail);
   ajax.getData('randomBook/',this.bookSuccess,this.fail);
   that.setData({
     length: length,
     windowWidth: windowWidth,
   });
   that.runMarquee();// 水平一行字滚动完了再按照原来的方向滚动
  
 },
// imgsuccess:function(data){
//   var that = this
//   that.setData({
//     'recommendItems[0].imageurl' : data
//     })
//     console.log(data)
// },
fail:function(data){
  wx.showToast({
    title: 'bug',
  })
},
bookSuccess:function(data){

  console.log(data)
  console.log(data[0].fields.Title)
  var that = this
  for (var i=0;i<data.length;i++){
    if(i<6){
      that.data.recommendItems[i].name = data[i].fields.Title 
      that.data.recommendItems[i].price = "￥"+data[i].fields.Price
      that.data.recommendItems[i].imageurl = "http://127.0.0.1:8000/ims/img/"+data[i].fields.image
    } 
  }
   that.setData({
   'recommendItems':that.data.recommendItems,
   'book':data
  })
  
},

runMarquee: function () {
   var that = this;
   var interval = setInterval(function () {
     //文字一直移动到末端
     if (-that.data.marqueeDistance < that.data.length) {
       that.setData({
         marqueeDistance: that.data.marqueeDistance - that.data.marqueePace,
       });
     } else {
       clearInterval(interval);
       that.setData({
         marqueeDistance: that.data.windowWidth
       });
       that.runMarquee();
     }
   }, that.data.interval);
 },

  // 导航切换监听
  navbarTap: function (e) {
    this.setData({
      currentTab: e.currentTarget.dataset.idx
    })
  },
  //四个功能页面跳转 
  catchTapSelect:function (e){
    var flag = this.data.navItems[e.currentTarget.dataset.typeid].typeId;
     if(flag == 0){
       wx.navigateTo({
       url: '../Search/search',
     });
     } else if(flag == 1){
       wx.navigateTo({
         url: '../pre_order/pre_order',
       });
     } else if(flag == 2){
       wx.navigateTo({
         url: '../points/points',
       })
     } else if(flag == 3){
       wx.navigateTo({
         url: "../share/share",
       })
     }                    
     
  },
  //闲置书籍功能
  catchTapSelect_old:function (e){
    var flag = this.data.navItems_old[e.currentTarget.dataset.typeid].typeId;
     if(flag == 0){
       wx.navigateTo({
       url: '../Search/search',
     });
     } else if(flag == 1){
       wx.navigateTo({
         url: '../book_upload/book_upload',
       });
     } else if(flag == 2){
       wx.switchTab({
         url: '../Question/ques',
       })
     } else if(flag == 3){
       wx.navigateTo({
         url: "../share/share",
       })
     }                    
     
  },
//推荐书籍页面
  catchTapCategory:function (e){
    var goodsname = this.data.recommendItems[e.currentTarget.dataset.typeid].name;
    console.log("asdas")
    console.log(e.currentTarget.dataset.typeid)
    console.log(this.data.book[e.currentTarget.dataset.typeid])
    wx.setStorage({
      data: this.data.book[e.currentTarget.dataset.typeid],
      key: 'product',
    })
    wx.navigateTo({
      url: '../product_info/product_info',
    })
 }
})
