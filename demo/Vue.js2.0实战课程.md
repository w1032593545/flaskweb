## 一、什么是前端？前端都包括哪些内容

#### 1. 前端历史

2014之前：HTML，CSS，JavaScript，jQuery（2006，JavaScript函数库），Bootstrap(UI)

2014年—2016年：NodeJS，Angular（谷歌），React（Facebook），Vue（华人，尤雨溪）

2017年之后：小程序等等

#### 2.前端代码体验

使用HTMl构建页面结构

使用CSS修饰页面的效果

使用JavaScript实现动态效果：

2.1 获取HTML元素

2.2 添加事件改变元素内容或样式

#### 3. VSCode前端环境配置

3.1 安装Beautify，它用来格式化代码

3.2 安装open in browser  右键选中可以直接在浏览器中查看页面效果

3.3 HTML Snippets 代码自动填充

3.4 Vetur  支持Vue 

3.5 Live server 浏览器实时更新

## 二、动手写一个购物车效果

#### 1. HTML，CSS，JavaScript，jQuery，Bootstrap

引入库：https://www.bootcdn.cn/

#### 2. 非工程化方式的Vue

v-model 双向数据绑定，指令用来在 input、select、textarea、checkbox、radio 等表单控件元素上创建双向数据绑定，根据表单上的值，自动更新绑定的元素的值。 

v-for 循环遍历，渲染列表项

v-bind 绑定数据和元素属性，div v-bind:class="{'class1': use}" 判断 use 的值，如果为 true 使用 class1 类的样式，否则不使用该类： 

v-on  事件绑定

## 三、动手写一个TODOList应用

设置一个倒计时，比如说初始时间是25分钟，进入work（工作）状态，25分钟到点后就是一个5分钟的rest（休息）状态，如此反复



## 四、Vue2.X工程化环境搭建

1. 下载nodejs：https://nodejs.org/en/，npm包管理工具

   检查是否已经安装，cmd中输入node -v检查node ，npm -v 检查npm

2. 用管理员身份打开cmd或者cmder或者gitbash：运行npm install -g vue-cli，vue-cli是vue的脚手架工具  ，Mac Terminal中增强权限sudo

   如果之前安装过，可以先卸载 vue-cli：npm uninstall -g vue-cli

   输入vue --version检查是否安装成功

3. 初始化项目  vue init webpack practise

   进入到项目中  cd practise

   运行项目  npm run dev

   

4. 启动单元测试：npm run unit

5. 启动端对端测试e2e：npm run e2e，因为selenium需要Java的环境，所以先要安装Java的JDK（关注右侧公众号或微信中搜索“即学即会IT课”，点击java即可获取安装视频），安装好之后，先把谷歌浏览器升级到最新版本，然后把node_modules中的chrome-driver文件夹删掉，把package.json中的chrome-driver依赖删掉，执行以下npm install；最后执行 npm install chromedriver –chromedriver_cdnurl=<https://npm.taobao.org/mirrors/chromedriver> 从淘宝的镜像安装chrome-driver即可。（关键点：chrome一定要是最新，chrome-driver也是最新，这两个版本一定一定要对应，否则会报错）

6. 安装vue-devtools，打开 <https://github.com/vuejs/vue-devtools> ，将Branch切换到master分支，再点击clone or download按钮下载；下载完成后，将压缩包解压，进入到vue-devtools文件夹中，执npm install (安装依赖)，运行完成后，再执行npm run build (编译文件)。打开谷歌浏览器的设置—> 扩展程序—>加载已解压的扩展程序（确保右上角开发者模式已经打开），选中vue-devtools文件夹中的shells中的chrome文件夹即可，重启浏览器生效

## 五、MVVM架构

MTV，MVC

1. 名词解释 View（div #app） Model（var data） ViewModel

   Model-View-ViewModel MVVM

2. 数据传入Vue实例后发生了什么？

   ```
   var obj = {}
   undefined
   var text = ''
   undefined
   var oH2 = document.getElementsByTagName('h2')[0]
   undefined
   Object.defineProperty(obj,'text',{
     get:function(){ return text; },
     set:function(newVal){text=newVal;oH2.innerHTMl=text;}
   });
   {}text: (...)get text: ƒ ()set text: ƒ (newVal)__proto__: Object
   obj.text = "nidedingdan"
   "nidedingdan
   ```

   通过setters，getters方法实现的双向数据绑定，数据驱动