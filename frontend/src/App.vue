<template>
  <header>
    <div class="header_left">
      <router-link to="/"><img src="../img/Главная.svg" alt="" class="img_width"></router-link>
      <router-link to="/categories"><img src="../img/Каталог.svg" alt="" class="img_width"></router-link>
      <img src="../img/Поиск.svg" alt="" class="img_width">
    </div>
    <div class="header_logo">
      <img src="../img/Лого.svg" alt="">
    </div>
    <div class="header_right">
      <img src="../img/enter.svg" alt="" class="img_width">
      <img src="../img/Избранное.svg" alt="" class="img_width">
      <img src="../img/Корзина.svg" alt="" class="img_width">
    </div>
  </header>

  <div class="fake"></div>
  <router-view/>

  <footer id="footer" class="footer">
    <div class="container">
      <div class="footer_phone">
        <img src="../img/Logo_white.svg" width="200" style="color: white" alt="IT UNIVERSITY" class="logo">
        <p class="p_phone">
          +7 (123) 345-67-55
        </p>
      </div>
      <div class="footer_year">
        <p class="credits">
          © LAGRACI, 2022‐2023
        </p>
      </div>
    </div>
  </footer>
</template>

<style>

header{
  display: flex;
  padding-top: 20px;
  position: fixed;
  background-color: white;
  height: 100px;
  z-index: 10;
  width: 100%;
  box-shadow: 0 0 .4em #787878;
}

.img_width{
  width: 30%;
}
.header_left{
  margin-left: 21%;
}


.header_logo img{
  width: 80%;
}

.fake{
  padding-top: 100px;
}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}



.footer {
  padding: 33px 0;
  background: black;
  color: white;
}

.footer_phone {
  display: flex;
  justify-content: space-between;
}

.footer_year {
  text-align: center;
}

.container {
  width: 1170px;
  margin: 0 auto; /* Контейнер автоматически всегда будет находиться по середине */
}
</style>
