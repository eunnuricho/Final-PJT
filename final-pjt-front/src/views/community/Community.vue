<template>
<div class="community_container">
  <div class="community">
    <h2>Community</h2>
    <span v-if="isLogin">
      <article-list>        
      </article-list>
      <article-create>
      </article-create>    
    </span>    
    <router-view @login="isLogin = true"/>      
  </div>
  </div>
</template>

<script>
import ArticleList from '@/components/community/ArticleList'
import ArticleCreate from '@/components/community/ArticleCreate'

export default {
  name: "Community",
  components: {
    ArticleList,
    ArticleCreate,
  },
  data: function () {
    return {
      isLogin: false
    }
  },  
  created: function () {
    const token = localStorage.getItem('jwt')

    if(token) {
      this.isLogin = true
    }
  }
}
</script>

<style>
.community > h2{
  font-family: 'Bebas Neue', cursive;
  color: lightskyblue
}

.community_container {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 900px;
  background-color: #0009;
  border-radius: 5px;
  box-sizing: border-box;
  width: 900px;
  margin: 0;
  max-width: 1000px;
  padding: 10px 30px 20px;
  margin-bottom: 100px;
}
</style>