<template>
  <div class="commentform1">    
        <v-text-field class="inputcomments"
        v-model="commentItem.content"
        :rules="rules"
        counter
        maxlength="100"
        hint="This field uses maxlength attribute"
        label="Comments"
        ></v-text-field> 
      <v-btn  class="btn btn-primary" @click="makeCreate">댓글 작성</v-btn>
    </div> 
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'CommentCreate',
  props: {
    article: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      commentItem: {
        content: null,
        currentUser: null,
      },
      rules: [v => v.length <= 100 || 'Max 100 characters']
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
    getCurrentUser() {
      axios({
        method: 'GET',
        url: `${SERVER_URL}accounts/`, 
        headers: this.setToken()
      }) 
      .then(res => {        
        this.commentItem.currentUser = res.data.username    
        console.log(this.commentItem.currentUser)
      })
      .catch(err => console.log(err))
    },   
    createComment() {
      const commentItemSet = {
        commentItem: this.commentItem,
        article_id: this.article.id,
        token: this.setToken()
      }
      console.log(commentItemSet)
      this.$store.dispatch('createArticleComment', commentItemSet)
      this.commentItem.content = null
      this.commentItem.currentUser = null
    },
    makeCreate () {
    this.getCurrentUser()
    this.createComment()    
    }
  }
}
</script>

<style>
.commentform1{
  display: flex;
  justify-content: center;
  align-items: center;  
}
.inputcomments{
  margin-right: 5px;
}
</style>