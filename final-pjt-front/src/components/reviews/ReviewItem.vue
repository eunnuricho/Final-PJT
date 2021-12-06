<template>
  <div>
    <div class="review_name">
      <span>    
        <router-link :to="{ name: 'ReviewDetail', params: { id : reviewItem.id }}">{{ reviewItem.title }}</router-link>
      </span>
    </div>  
  </div>
</template>

<script>
export default {
  name: 'ReviewItem', 
  props: {
    review: {
      type: Object,
      required: true
    },
  },  
  data: function () {
    return {
      reviewItem: {
        movie_title: this.review.movie_title,      
        movie_pk: this.review.pk,
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank,
        id: this.review.id
      },
    }
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteReview() {
      const deleteItem = {
        review_id: this.review.id,
        token: this.setToken()
      }      
      console.log(deleteItem)
      this.$store.dispatch('deleteReview', deleteItem)
    },
    updateReview() {
      const updateItem = {
        reviewItem: this.reviewItem,
        review_id: this.review.id,
        token: this.setToken()
      }
      console.log(updateItem)  
      this.$store.dispatch("updateReview", updateItem)    
    }

  },
  created() {
    console.log(this.review)
  }
}
</script>

<style >
.review_name a{
  text-decoration: none;   
}
.review_name a:link{
  color: white;   
}
.review_name a:visited{
  color: white;   
}
.review_name a:hover{
  color: lightskyblue;   
}
</style>