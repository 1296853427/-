const ajax = require('../../utils/ajax.js');
const utils = require('../../utils/util.js');
Page({
  data: {
    cart: [{
      goods_small_logo:null,
      goods_name:null,
      goods_price:null,
      goods_id:null,
      count:null, 
    },
    {
      goods_small_logo:null,
      goods_name:null,
      goods_price:null,
      goods_id:null,
      count:null, 
    },
    {
      goods_small_logo:null,
      goods_name:null,
      goods_price:null,
      goods_id:null,
      count:null, 
    },
    {
      goods_small_logo:null,
      goods_name:null,
      goods_price:null,
      goods_id:null,
      count:null, 
    },
    {
      goods_small_logo:null,
      goods_name:null,
      goods_price:null,
      goods_id:null,
      count:null, 
    },
    {
      goods_small_logo:null,
      goods_name:null,
      goods_price:null,
      goods_id:null,
      count:null, 
    },
  ], //购物车数组
  tmpPost:[
    {
      CommodityID:null,
      CommodityCount:null,
    }

  ],
    totalPrice: 0, //总价
    totalcount: 0, //总数量
    length: 0,
  },
  onLoad: function () {
    var that = this
    wx.getStorage({
      key: 'product',
      success: function (res) {
        console.log("2")
        console.log(res.data)
        console.log(res.data.length)
        for (var i = 0; i < res.data.length; i++) {
            console.log(res.data[i].imgUrl)
            console.log(i)
            that.data.cart[i].goods_small_logo=res.data[i].imgUrl,
            that.data.cart[i].goods_name= res.data[i].title,
            that.data.cart[i].goods_price=res.data[i].price,
            that.data.cart[i].count=res.data[i].count,
            that.data.cart[i].goods_id=res.data[i].goodsId,
            that.data.totalPrice=res.data[i].price        
        }
        console.log(that.data.cart)
        that.setData({
          'cart':that.data.cart,
          'totalPrice':that.data.totalPrice,
          'length': res.data.length
        })
      }
    })
    wx.setStorage({
      data: null,
      key: 'product',
    })

  },
  handleQuantityChange(e) {
    var componentId = e.componentId;
    var quantity = e.quantity;
    this.data.cart[index].count = quantity;
    this.setData({
      cart: this.data.cart,
    });
  },
  delCount: function (e) {
    var index = e.target.dataset.index;
    console.log("刚刚您点击了减1");
    var count = this.data.cart[index].count;
    // 商品总数量-1
    if (count > 1) {
      this.data.cart[index].count--;
    }
    // 将数值与状态写回  
    this.setData({
      cart: this.data.cart
    });
    this.priceCount()
  },
  /* 加数 */
  addCount: function (e) {
    var index = e.target.dataset.index;
    console.log("刚刚您点击了加1");
    var count = this.data.cart[index].count;
    // 商品总数量-1  
    if (count < 10) {
      this.data.cart[index].count++;
    }
    // 将数值与状态写回  
    this.setData({
      cart: this.data.cart
    });
    this.priceCount()
  },
  priceCount: function (e) {
    this.data.totalPrice = 0;
    for (var i = 0; i < this.data.cart.length; i++) {
        this.data.totalPrice = parseFloat(this.data.totalPrice + (this.data.cart[i].goods_price * this.data.cart[i].count)).toFixed(2);     
    }
    this.setData({
      totalPrice: this.data.totalPrice,
    })
  },


  handleOrderPay() {
    for(var i =0;i<this.data.length;i++){
      this.data.tmpPost[0].CommodityID =this.data.cart[i].goods_id
      this.data.tmpPost[0].CommodityCount =this.data.cart[i].count
      console.log(this.data.tmpPost[0])
      ajax.request('orderCreat/',this.data.tmpPost[0],this.postSuccess,this.fail)
    }
  },
  postSuccess:function(data){
    wx.navigateTo({
      url: '../order_confirm/order_confirm',
    })
  },
  fail:function(data){

  }
});