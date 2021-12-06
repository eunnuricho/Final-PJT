<template>
  <v-app id="app">
      <div class="app">
        <div class="logo" ><img :src="require(`./assets/multiplus5.png`)" alt="logo" @click="gohome"></div>      
        <div class="nav">          
          <span v-if="isLogin">
            <!-- <router-link :to="{ name: 'Profile' }">Profile</router-link>| -->
            <!-- <router-link :to="{ name: 'Community' }">Community</router-link>| -->
            <router-link @click.native="getCurrentUser" to="#">MyPage</router-link>|
            <router-link @click.native="logout" to="#">Logout</router-link>|
            <router-link :to="{ name: 'Recommend' }">Recommend</router-link>|
            <router-link :to="{ name: 'MovieList' }">MovieList</router-link>|
            <router-link :to="{ name: 'Reviews' }">Reviews</router-link>|
            <router-link :to="{ name: 'Community' }">Community</router-link>
          </span>
          <span v-else>
            <router-link :to="{ name: 'Signup' }">Signup</router-link>|
            <router-link :to="{ name: 'Login' }">Login</router-link>|
            <router-link :to="{ name: 'MovieList' }">MovieList</router-link>|
            <router-link :to="{ name: 'Login' }">Reviews</router-link>|
            <router-link :to="{ name: 'Login' }">Community</router-link>
          </span>
        </div>
      </div>
    <router-view :key="$route.fullPath" 
      @login="isLogin = true"/>
    
  </v-app>
</template>

<script>
const SERVER_URL = 'http://127.0.0.1:8000/'
import axios from 'axios'
export default {
  name: "App",
  data: function () {
    return {
      isLogin: false,
      currentUser: {},
    }
  },
  methods: {
    logout: function() {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.currentUser = {}
      this.$router.push({name:'Home'})
      
    },
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getCurrentUser() {
      axios({
        method: 'GET',
        url: `${SERVER_URL}accounts/`, 
        headers: this.setToken()
      }) 
      .then(res => {
        console.log(res)
        this.currentUser = res.data
        this.$router.push({ name: 'MyPage', params: { id: this.currentUser.id, currentUser: this.currentUser } })
      })
      .catch(err => console.log(err))
    },
    gohome() {
      this.$router.push({name:'Home'})
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
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Noto+Sans+KR&display=swap');
@import 'assets/styles/appstyle.css';
#app {
  min-height: 100vh;
  background-image:url("./assets/background.jpg");
  background-size: cover;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;  
  /* 기본 서체 */
  font-family: 'Noto Sans KR', sans-serif;     
}
.v-application--wrap {
  flex: 1 1 auto;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    display: flex;
    align-items: center;
    min-height: 100vh;
    max-width: 100%;
    position: relative;
}

.app {
  margin: 0;
  padding: 0;
  box-sizing: border-box;  
  width: 100%;
  min-height:  80px;
  overflow:  hidden;
  display: flex;   
  align-items: center;
  position: relative;    
}

.app .logo {
  display: flex;
  width: 150px;
  height: 150px;
}

.app .nav { 
  display: flex;
  padding-left: 150px;
  justify-content: space-between; 
  /* 넷플릭스 서체 */
  font-family: 'Bebas Neue', cursive;
}

.app .nav a {
  padding: 20px 20px;
  text-decoration: none;
  font-size: 1.5rem;
  /* font-weight: bold; */
  color: whitesmoke;
}

.app .nav a:hover {
  color: lightskyblue;
}
.app .nav a.router-link-exact-active {
  color: lightskyblue;
}
</style>
