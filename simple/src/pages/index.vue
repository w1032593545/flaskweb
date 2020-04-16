<template>
  <div class="index-wrapper">
    <div class="index-left">
      <!-- 全部产品 -->
      <div class="index-left-block">
        <h2>全部产品</h2>
        <template v-for="product in productList">
          <h3>{{ product.title }}</h3>
          <ul>
            <li v-for="item in product.list">
                <a v-bind:href="item.url">{{ item.title }}</a>
                <span v-if="item.hot" class="hot-tag">HOT</span>
            </li>
          </ul>
          <div v-if="product.last" class="hr"></div>
        </template>
      </div>
      <!-- 最新消息 -->
      <div class="index-left-block lastest-news">
        <h2>最新消息</h2>
        <ul>
          <li v-for="item in newslist">
            <a v-bind:href="item.url">{{ item.title }}</a>
            <span v-if="item.hot" class="hot-tag">HOT</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="index-right">
      <div style="margin:0 auto;width:900px;height:300px;background:red;">使用组件代替</div>
      <div class="index-boader-list">
        <div class="index-boader-item">
          <div class="index-boader-inner">
            <h2>戴尔电脑</h2>
            <p>戴尔电脑就是好哇</p>
            <div class="index-boader-button">立即购买</div>
          </div>
        </div>
        <div class="index-boader-item">
          <div class="index-boader-inner">
            <h2>戴尔电脑</h2>
            <p>戴尔电脑就是好哇</p>
            <div class="index-boader-button">立即购买</div>
          </div>
        </div>
        <div class="index-boader-item">
          <div class="index-boader-inner">
            <h2>戴尔电脑</h2>
            <p>戴尔电脑就是好哇</p>
            <div class="index-boader-button">立即购买</div>
          </div>
        </div>
        <div class="index-boader-item">
          <div class="index-boader-inner">
            <h2>戴尔电脑</h2>
            <p>戴尔电脑就是好哇</p>
            <div class="index-boader-button">立即购买</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  mounted() {
    axios.get('api/getnewslist')
    .then((res) => {
      console.log(res);
      this.newslist = res.data.list
    })
    .catch((error) => {
      console.log(error);
      
    });
  },
  data() {
    return {
              newslist: [
          {
            title: "数据统计",
            url: "http://starcraft.com"
          },
          {
            title: "数据预测",
            url: "http://warcraft.com"
          },
          {
            title: "流量分析",
            url: "http://overwatch.com",
            hot: true
          },
          {
            title: "广告发布",
            url: "http://hearstone.com"
          }
        ],
      productList: {
        pc: {
          last:true,
          title: "PC产品",
          list: [
            {
              title: "数据统计",
              url: "http://starcraft.com"
            },
            {
              title: "数据预测",
              url: "http://warcraft.com"
            },
            {
              title: "流量分析",
              url: "http://overwatch.com",
              hot: true
            },
            {
              title: "广告发布",
              url: "http://hearstone.com"
            }
          ]
        },
        app: {
          title: "手机应用类",
          list: [
            {
              title: "91助手",
              url: "http://weixin.com"
            },
            {
              title: "产品助手",
              url: "http://weixin.com",
              hot: true
            },
            {
              title: "智能地图",
              url: "http://maps.com"
            },
            {
              title: "语音助手",
              url: "http://phone.com",
              hot: true
            }
          ]
        }
      }
    };
  }
};
</script>

<style scoped>
.index-wrapper {
  width: 1200px;
  display: flex;
}
.index-left {
  width: 300px;
}
.index-right {
  width: 900px;
  margin-top:15px;
}
.index-left-block {
  margin: 15px;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0 0 1px #dddddd;
}
.index-left-block .hr {
  border: 1px solid black;
  margin: 20px 0;
}
.index-left-block h2 {
  background: #4fc08d;
  color: #ffffff;
  padding: 10px 15px;
  margin-bottom: 20px;
}
.index-left-block h3 {
  color: #222;
  font-weight: bolder;
  padding: 0 15px 5px 15px;
}
.index-left-block ul {
  padding: 10px 15px;
}
.index-left-block li {
  padding: 5px;
}
.index-boader-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top:15px;
}
.index-boader-item {
  width: 400px;
  height: 125px;
  background: #ffffff;
  box-shadow: 0 0 1px #dddddd;
  border-radius: 0 0 10px 10px;
  margin-bottom:20px;
  padding: 20px;
}
.index-boader-inner{
  height: 125px;
  padding-left: 160px;
  background-image:url(../assets/logo.png);
  background-repeat: no-repeat;
  background-size:30%;
}
.index-boader-inner h2{
  font-size: 18px;
  font-weight: bolder;
  color:#000;
  margin-bottom:15px;
}
.index-boader-inner p{
  margin-bottom: 15px;
}
.index-boader-button{
  width: 80px;
  height: 40px;
  background:#4fc08d;
  color:#ffffff;
  text-align: center;
  line-height: 40px;
  border-radius: 5px;
}
.hot-tag{
  color: #ffffff;
  background: purple;
  font-size: 13px;
}
</style>