<template>
  <div class="login_container">
    <div class="login">
      <h1>Login</h1>
      <div>
        <label for="username"></label>
        <input type="text"
        id="username"
        v-model="credentials.username"
        placeholder="username">
      </div>
      <div>
        <label for="password"></label>
        <input type="password" 
        id="password"
        v-model="credentials.password"
        placeholder="passowrd">
      </div>       
      <button @click="login">LOGIN</button>
      <span>Don't have an ID?</span>
      <router-link :to="{ name: 'Signup' }"
      class="gosignup">Create one now.</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null
      },
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url:'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then(res=>{
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login') 
          this.$router.push({name:'MovieList'})
        })
        .catch(err=> {
          console.log(err)
          alert("로그인에 실패했습니다. 아이디/비밀번호를 확인하세요")
        })
      this.$emit('submit-login-data', this.loginData)
    }
  }
}
</script>

<style>
.login_container {
  display: flex;
  flex-direction: column;
  justify-content:center;
  align-items: center;
  min-height: 660px;
  background-color: #0009;
  border-radius: 5px;
  box-sizing: border-box;
  width: 100%;
  margin: auto;
  max-width: 450px;
  padding: 60px 68px 40px;
  margin-bottom: 100px;
}

.login_container .login{
  display: flex;
  flex-direction: column;
  max-width: 450px;
  width: 100%;
  align-items: center;
}

.login_container .login h1{
  font-family: 'Bebas Neue', cursive;
  color: lightskyblue;
  font-size: 32px;
  margin-bottom: 28px;
}

.login_container .login input{
  background: #333;
border-radius: 4px;
border: 0;
color: white;  
height: 50px;
line-height: 40px;
padding: 5px 20px;
margin-bottom: 20px;
}
/* .signup input:last-child{
  margin-bottom: 30px;
} */

.login_container .login button{
  background: lightskyblue;
  border-radius: 4px;
  font-size: 16px;
  font-weight: bold;
  margin: 24px 0 12px;
  padding: 16px;
  border: 0;
  color: white;
  cursor: pointer;
  width: 255px;   
}

.login_container .login span{
  color: lig;
}
.login_container .login .gosignup {
  text-decoration: none;
  color: white;
}
</style>