<template>
  <div class="reviews_container">
    <div class="reviews">
      <h2>REVIEWS</h2>
      <span v-if="isLogin">           
        <review-list>        
        </review-list>
        <review-create>
        </review-create>
      </span>    
      <router-view @login="isLogin = true"/>      
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/reviews/ReviewList'
import ReviewCreate from '@/components/reviews/ReviewCreate'
export default {
  name: "Reviews",
  components: {
    ReviewList,
    ReviewCreate
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
.reviews > h2{
  font-family: 'Bebas Neue', cursive;
  color: lightskyblue
}

.reviews_container {
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