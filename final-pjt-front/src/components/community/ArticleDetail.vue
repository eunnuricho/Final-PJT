<template>
  <div class="articleitems">   
    <v-card>
      <v-toolbar dark>
        <v-spacer></v-spacer>       
        <v-toolbar-title>{{article.id}}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer> 
        <v-spacer></v-spacer>  
        <v-toolbar-title>{{article.user.username}}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn icon dark @click="goback">
          <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <v-list three-line>         
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>Title </v-list-item-title>
            <v-list-item-title>{{ article.title }}</v-list-item-title>
          </v-list-item-content>    
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list subheader>          
        <v-list-item>            
          <v-list-item-content>
            <v-list-item-title>Content</v-list-item-title>            
            <v-list-item-title>
              <div class="marginplz">
              <v-textarea outlined name="articleContent" cols="80" rows="5" v-model="article.content" placeholder="내용"></v-textarea>
              </div>
              </v-list-item-title>
          </v-list-item-content>
        </v-list-item>          
        <v-list-item>     
        <v-subheader>작성 시각: {{ article.created_at | moment('from', 'now') }}</v-subheader>          
        <v-subheader>수정 시각: {{ article.updated_at | moment('from', 'now') }}</v-subheader>
          <v-list-item-content>
            <v-list-item-subtitle>Likes</v-list-item-subtitle>
            <v-list-item-title
             v-for="user in article.like_users" 
            :key="user.id">
            {{ user.username }}</v-list-item-title>
          </v-list-item-content>
        <v-list-item-content v-if="articleLiked" class="article-detail-like">
          <i @click="toggleLike" style="color: crimson" class="fas fa-heart article-detail-like-button"></i> {{ likeUser.length }}
        </v-list-item-content>
        <v-list-item-content v-else class="article-detail-like">
          <i @click="toggleLike" class="fas fa-heart article-detail-like-button"></i> {{ likeUser.length }}
        </v-list-item-content>
        <v-list-item-content >
            <v-row class="btn_x">
              <v-col col="6">                
              </v-col>
              <v-col col="6">
            <v-btn class="btn btn-primary" @click="updateArticle">UPDATE</v-btn>
            <v-btn class="btn btn-danger" @click="deleteArticle">DELETE</v-btn>                
              </v-col>
              </v-row>            
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-card max-width="900">
    <v-toolbar color="light-blue lighten-2">
      <v-spacer></v-spacer> 
      <v-toolbar-title>Comments</v-toolbar-title>
      <v-spacer></v-spacer>      
    </v-toolbar>
    <v-list three-line>
      <v-list-item>
        <v-list-item-content class="marginplz2">          
      <comment-create :article="article"></comment-create>
      </v-list-item-content>
      </v-list-item>
      <v-list-item>
      <v-list-item-content>
      <comment-list :article="article"></comment-list>
        </v-list-item-content>
      </v-list-item>      
    </v-list>
  </v-card>  
      </v-list>
    </v-card>
  </div>
</template>

<script>
import CommentList from '@/components/community/CommentList'
import CommentCreate from '@/components/community/CommentCreate'
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'ArticleDetail',
  components: {
  CommentList,
  CommentCreate
  },
  data: function() {
    return {
      articleItem : {
        title : null,
        content : null,
        id : null
      },       
      article: null,
      currentUser:null,
      likeUser:null,
      articleLiked: null,
    }
  },
  methods : {
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
        this.articleLiked = !!this.likeUser.some(user => user.username === this.currentUser.username)
      })
      .catch(err => console.log(err))
    },
    
    toggleLike() {
      const likeBtn = document.querySelector(".article-detail-like-button")
      axios({
      method: 'POST',
      url: `${SERVER_URL}articles/${this.$route.params.id}/like/`,
      headers: this.setToken()})
      .then(res => {
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
      const likeBtn = document.querySelector(".article-detail-like-button")
      console.log(this.articleLiked)
      if (this.articleLiked) {
          likeBtn.style.color = 'crimson'
      } else {likeBtn.style.color = 'black'}
    },

    getArticle(){
      axios({
      method: 'GET',
      url: `${SERVER_URL}articles/${this.$route.params.id}/`,
      headers: this.setToken()})
      .then(res => {
        console.log(res)
        this.article = res.data
        this.likeUser = this.article.like_users
        console.log(this.likeUser)
        this.likeCount = res.data.count
      })
    },
    deleteArticle() {
      const deleteItem = {
        article_id: this.article.id,
        token: this.setToken()
      }      
      console.log(deleteItem)
      this.$store.dispatch('deleteArticle', deleteItem)
    },
    updateArticle() {          
      this.articleItem.title= this.article.title,
      this.articleItem.content= this.article.content,      
      this.articleItem.id =  this.article.id
      const updateItem = {
        articleItem: this.articleItem,
        article_id: this.article.id,
        token: this.setToken()
      }
      console.log(updateItem)  
      this.$store.dispatch("updateArticle", updateItem)     
    },
    goback() {
      this.$router.push({name:'Community'})
    }
  },
  created(){
    this.getArticle()
    this.getCurrentUser()
  }
}

</script>

<style>
.articleitems {
  font-family: 'Noto Sans KR', sans-serif;    
  background-color: #0009;
  display: flex;
  flex-direction: column;
  align-items: left;   
  border-radius: 5px;
  box-sizing: border-box;
  width:900px;
  margin: 0;
  max-width: 900px;
  padding: 10px 30px 20px;  
}
.articleitems .marginplz {
  margin-top: 10px;
}
.articleitems .marginplz2 {
  margin-top: 10px;
  margin-bottom: 20px;
}
.article-detail-like{
  display: flex;
  justify-content: center;
}
.btn_x{
  display: flex;
  justify-content: left;
}
</style>