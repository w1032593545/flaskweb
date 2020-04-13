<template>
  <div class="container" id="app">
    <h2>我的购物车清单</h2>
    <div class="input-group">
      <input type="text" placeholder="请输入你想购买的物品" class="js-new-item form-control" />
      <span class="input-group-btn">
        <button type="button" class="js-add btn btn-default">添加到购物车</button>
      </span>
    </div>

    <!-- 购物车列表 -->
    <ul>
      <li>
        <div class="checkbox">
          <label for>
            <input type="checkbox" class="js-item" />苹果
          </label>
        </div>
      </li>
      <li>
        <div class="checkbox">
          <label for>
            <input type="checkbox" class="js-item" />香蕉
          </label>
        </div>
      </li>
      <li>
        <div class="checkbox">
          <label for>
            <input type="checkbox" class="js-item" />电脑
          </label>
        </div>
      </li>
    </ul>

    <!-- 修改标题 -->
    <div class="footer">
      <hr />
      <span>改变你的标题</span>
      <input type="text" class="js-change-title" value="我的购物车清单" />
    </div>
  </div>
</template>

<script>
</script>

<style>
.container {
  width: 40%;
  margin: 100px auto;
}
.removed {
  color: gray;
}
.removed label {
  text-decoration: line-through;
}
ul {
  border: 1px solid black;
  margin-top: 10px;
}
ul li {
  list-style: none;
}
</style>
