<template>
  <div class="signup_container">
    <div class="signup">
      <h1>Signup</h1>
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
      <div>
        <label for="passwordConfirmation"></label>
        <input type="password" id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
        @keyup.enter="signup"
        placeholder="passwordConfirmation">
      </div>
      <button @click="signup"> signup </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null
      }
    }
  },
  methods: {
    signup: function () {
      // console.log(this.credentials)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
      .then( () => {
        // console.log(res)
        this.$router.push({name:'Login'})
      })
      .catch(res => {
        console.log(res)
        alert("아이디, 비밀번호를 다시 확인하세요")
      })
    }
  }
}
</script>

<style>
.signup_container {
  display: flex;
  flex-direction: column;
  justify-content: center;
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

.signup_container .signup{
  display: flex;
  flex-direction: column;
  max-width: 450px;
  width: 100%;
  align-items: center;
}

.signup_container .signup h1{
  font-family: 'Bebas Neue', cursive;
  color: lightskyblue;
  font-size: 32px;
  margin-bottom: 28px;
}

.signup_container .signup input{
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

.signup_container .signup button{
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
</style>
