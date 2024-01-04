<script setup>

</script>

<template>
  <header>
    <img
      alt="Vue logo"
      class="logo"
      src="../assets/logo1.svg"
      width="125"
      height="125"
    />
    <div class="wrapper">
      <div class="greetings">
        <h1 class="white">中国地图网</h1>
        <h3 class="white">
          这是一个
          <a href="https://cn.vuejs.org/" target="_blank" rel="noopener">Vue 3</a>+
          <a href="https://www.djangoproject.com/" target="_blank" rel="noopener">Django 5</a>
          的小项目.
        </h3>
      </div>
    </div>
  </header>
</template>

<style scoped>
.white{
  color: hsl(255, 255%, 255%);
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
a,
.green {
  text-decoration: none;
  color: hsla(160, 100%, 37%, 1);
  transition: 0.4s;
  padding: 3px;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}
</style>