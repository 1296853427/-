// pages/product_info/product_info.js
const ajax = require('../../utils/ajax.js');
const utils = require('../../utils/util.js');
Page({
  data: {
    isLike: false,
    showDialog: false,
    indicatorDots: true, //是否显示面板指示点
    autoplay: true, //是否自动切换
    interval: 3000, //自动切换时间间隔,3s
    duration: 1000, //  滑动动画时长1s
    goods:[
      {
        title:null,
        price:null,
        privilegePrice:null,
        imgUrl:null,
        imgUrls:null,
        detailImg:null,
        goodsId:null,
        count:null,
        totalMoney:null,   
      },
    ],
    tmpgoods:[
      {
        title:null,
        price:null,
        privilegePrice:null,
        imgUrl:null,
        imgUrls:null,
        detailImg:null,
        goodsId:null,
        count:null,
        totalMoney:null,   
      },
    ],
  },
  //预览图片
  // 收藏
  // addLike() {
  //   this.setData({
  //     isLike: !this.data.isLike
  //   });
  //   ajax.request({
  //     method: 'GET',
  //     url: 'collection/addShopCollection?key=' + utils.key + '&goodsId=' + goodsId,
  //     success: data => {
  //       console.log("收藏返回结果：" + data.message)
  //       wx.showToast({
  //         title: data.message,
  //         icon: 'success',
  //         duration: 2000
  //       });
  //     }
  //   })
  // },
  // 跳到购物车
  toCar() {
    wx.switchTab({
      url: '../shopping_cart/shopping_cart'
    })
  },
  // 立即购买
  immeBuy() {
    wx.showToast({
      title: '购买成功',
      icon: 'success',
      duration: 2000
    });
    console.log("1")
    console.log(this.data.tmpgoods)
    wx.setStorage({
      data: this.data.tmpgoods,
      key: 'product',
    })
    wx.navigateTo({
      url: '../order/order',
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    wx.getStorage({
      key: 'product',
      success:function(res){
          that.data.goods[0].title=res.data.fields.Title,
          that.data.goods[0].price=(res.data.fields.Price * (1 - res.data.fields.Discount)).toFixed(2),
          that.data.goods[0].privilegePrice= res.data.fields.Price,
          that.data.goods[0].imgUrl= "http://127.0.0.1:8000/ims/img/" + res.data.fields.image,
          that.data.goods[0].imgUrls= ["http://127.0.0.1:8000/ims/img/" + res.data.fields.image, 
          "http://127.0.0.1:8000/ims/img/" + res.data.fields.image, 
          "http://127.0.0.1:8000/ims/img/" + res.data.fields.image, 
        ],
        that.data.goods[0].detailImg= "http://127.0.0.1:8000/ims/img/" + res.data.fields.image,
        that.data.goods[0].goodsId= 1,
        that.data.goods[0].count= 1,
        that.data.goods[0].totalMoney= res.data.fields.Price * (1 - res.data.fields.Discount)
        console.log(that.data.goods)
        that.setData({
          'goods': that.data.goods[0],
          'tmpgoods':that.data.goods
        })
        }

        
      
    })
    //加载商品详情
  },
 

  /**
   * sku 弹出
   */
  toggleDialog: function () {
    this.setData({
      showDialog: !this.data.showDialog
    });
  },
  /**
   * sku 关闭
   */
  closeDialog: function () {
    console.info("关闭");
    this.setData({
      showDialog: false
    });
  },
  /* 减数 */
  delCount: function (e) {
    console.log("刚刚您点击了减1");
    var count = this.data.goods.count;
    // 商品总数量-1
    if (count > 1) {
      this.data.goods.count--;
    }
    // 将数值与状态写回  
    this.setData({
      goods: this.data.goods
    });
    this.priceCount();
  },
  /* 加数 */
  addCount: function (e) {
    console.log("刚刚您点击了加1");
    var count = this.data.goods.count;
    // 商品总数量-1  
    if (count < 10) {
      this.data.goods.count++;
    }
    // 将数值与状态写回  
    this.setData({
      goods: this.data.goods
    });
    this.priceCount();
  },
  //价格计算
  priceCount: function (e) {
    this.data.goods.totalMoney = (this.data.goods.price * this.data.goods.count).toFixed(2);
    this.setData({
      goods: this.data.goods
    })
  },
  /**
   * 加入购物车
   */
  addCar: function (e) {
    var goods = this.data.goods;
    goods.isSelect = false;
    var count = this.data.goods.count;

    var title = this.data.goods.title;
    if (title.length > 13) {
      goods.title = title.substring(0, 13) + '...';
    }

    // 获取购物车的缓存数组（没有数据，则赋予一个空数组）  
    var arr = wx.getStorageSync('cart') || [];
    console.log("arr,{}", arr);
    if (arr.length > 0) {
      // 遍历购物车数组  
      for (var j in arr) {
        // 判断购物车内的item的id，和事件传递过来的id，是否相等  
        if (arr[j].goodsId == this.data.goods.goodsId) {
          // 相等的话，给count+1（即再次添加入购物车，数量+1）  
          arr[j].count = arr[j].count + 1;
          // 最后，把购物车数据，存放入缓存（此处不用再给购物车数组push元素进去，因为这个是购物车有的，直接更新当前数组即可）  
          try {
            wx.setStorageSync('cart', arr)
          } catch (e) {
            console.log(e)
          }
          //关闭窗口
          wx.showToast({
            title: '加入购物车成功！',
            icon: 'success',
            duration: 2000
          });
          this.closeDialog();
          // 返回（在if内使用return，跳出循环节约运算，节约性能） 
          return;
        }
      }
      // 遍历完购物车后，没有对应的item项，把goodslist的当前项放入购物车数组  
      arr.push(goods);
    } else {
      arr.push(goods);
    }
    // 最后，把购物车数据，存放入缓存  
    try {
      wx.setStorageSync('cart', arr)
      // 返回（在if内使用return，跳出循环节约运算，节约性能） 
      //关闭窗口
      wx.showToast({
        title: '加入购物车成功！',
        icon: 'success',
        duration: 2000
      });
      this.closeDialog();
      return;
    } catch (e) {
      console.log(e)
    }


  }
})