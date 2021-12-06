<template>
  <div class="homebutton">     
    <div>
    <img :src="require(`../assets/homelogo1.gif`)" alt="logo">      
    </div>
    <router-link :to="{ name: 'MovieList' }"><img :src="require(`../assets/Get Started.gif`)" alt="logo"></router-link>
  </div>
</template>

<script>
  

  export default {
    name: 'Home',    
  }
</script>
<style scoped>
.homebutton{   
  width: 100%;
  height: 700px;
  background-color: #000;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;  
}
.homebutton img{
  border-radius: 10%;
  width: 400px;
}
.homebutton a img{
  border-radius: 10%;
  width: 240px;
}
</style>