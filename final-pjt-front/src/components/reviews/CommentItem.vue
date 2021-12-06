<template>
  <div>
    <template>
      <v-list class="plzmin">
        <v-list-item class="marginminus">
        <v-container class="likespace">            
        <v-row>
          <v-col cols="11">
        <v-list-item-content class="marginminus2">        
        <v-text-field v-model="commentItem.content"></v-text-field>        
        </v-list-item-content>     
          </v-col>
            <v-col cols="1">    
        <v-list-item-subtitle v-if="commentLiked" class="comment-detail-like">
          <i @click="toggleLike" style="color: crimson" class="fas fa-heart comment-detail-like-button"></i> {{ likeUser }}
        </v-list-item-subtitle>
        <v-list-item-subtitle v-else class="comment-detail-like">
          <i @click="toggleLike" class="fas fa-heart comment-detail-like-button"></i> {{ likeUser}}
        </v-list-item-subtitle>    
 </v-col>
          </v-row>
          </v-container>
              



        </v-list-item>
        <v-list-item class="marginminus">
        <v-list-item-subtitle>username: {{currentUser.username}} ----- 작성일 : {{ comment.created_at | moment('YYYY-MM-DD HH:mm') }} ----- 수정일 : {{ comment.updated_at | moment('YYYY-MM-DD HH:mm') }}</v-list-item-subtitle>
      

      
        <v-btn x-small class="btn btn-primary" @click="updateComment">UPDATE</v-btn>
        <v-btn x-small class="btn btn-danger" @click="deleteComment">DELETE</v-btn>
        </v-list-item>
        <v-divider></v-divider>
      </v-list>
      </template>
    
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'CommentItem',
  props: {
    review: {
      type: Object,
      required: true,
    },
    comment: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      commentItem: {
        content: this.comment.content,      
      }, 
      currentUser: null,
      likeUser: [],
      commentLiked: null,
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
    updateComment() {
      const commentItemSet = {
        commentItem: this.commentItem,
        comment_id: this.comment.id,
        review_id: this.review.id,
        token: this.setToken()
      }      
      this.$store.dispatch('updateComment', commentItemSet)
    },
    deleteComment() {
      const commentItemSet = {
        comment_id: this.comment.id,
        review_id: this.review.id,
        token: this.setToken()
      }
      this.$store.dispatch('deleteComment', commentItemSet)
    },
    getCurrentUser() {
      axios({
        method: 'GET',
        url: `${SERVER_URL}accounts/`, 
        headers: this.setToken()
      }) 
      .then(res => {
        console.log(res)
        console.log("12312412421412421421")
        this.currentUser = res.data
        console.log(this.likeUser)
        console.log("213")
        console.log(this.currentUser)
        if (this.currentUser in this.likeUser) {
          this.commentLiked = true
        }
        else {
          this.commentLiked = false
        }
        // this.commentLiked = !!this.likeUser.some(user => user === this.currentUser.username)
      })
      .catch(err => console.log(err))
    },

    toggleLike() {
      const likeBtn = document.querySelector(".comment-detail-like-button")
      axios({
      method: 'POST',
      url: `${SERVER_URL}movies/community/${this.review.id}/${this.comment.id}/like/`,
      headers: this.setToken()})
      .then(res => {
        console.log(res)
        if (res.data.liked) {
          likeBtn.style.color = "crimson"
          this.likeUser.push(this.currentUser)
          }
      else {
          likeBtn.style.color = "black"
          this.likeUser = this.likeUser.filter(user => {
          return this.currentUser.username !== user.username
            })
        }
      })
      .catch(err=>console.log(err))
    },
    likedColor() {
      const likeBtn = document.querySelector(".comment-detail-like-button")
      console.log(this.commentLiked)
      if (this.commentLiked) {
          likeBtn.style.color = 'crimson'
      } else {likeBtn.style.color = 'black'}
    },
    getReviewComment(){
      axios({
      method: 'GET',
      url: `${SERVER_URL}movies/community/${this.review.id}/${this.comment.id}/`,
      headers: this.setToken()})
      .then(res => {
        console.log(res)

        this.likeUser = this.comment.like_users
      })
    },
  },
  created() {
    this.getCurrentUser()
    this.getReviewComment()
  }
}
</script>

<style>
.marginminus {
  height: 30px;  
  box-sizing:border-box;
  padding: 0;
  margin-left: 12px;
}
.marginminus2 {
  height: 50px;
  box-sizing: border-box;
  padding: 0;
  margin-left: 5px;
}
.plzmin {
  min-height: 50px;
}
.plzmin .v-list-item {
  min-height: 45px;
}
.likespace{
  
  margin: 0;
  padding: 0;
}
.likespace .row .col{
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  padding: 0;
}
</style>