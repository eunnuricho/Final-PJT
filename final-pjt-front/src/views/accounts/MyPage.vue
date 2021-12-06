<template>  
  <div class="profile_container">
      <div class="profile_header">{{ profileUser.username }}'s Page</div>
      <v-row>
        <v-col >
          <v-card
        max-width="400"
        class="mx-auto" >
        <v-app-bar>   
          <v-toolbar-title>My Reviews</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-app-bar>
        <v-container v-if="profileUser.reviews">
          <v-rol>            
          <router-link
            v-for="review in profileUser.reviews" 
            :key="review.id"
            :to="{name: 'ReviewDetail', params: { id: review.id }}" >         
            <v-col cols="12"> 
            <v-card  color="#385F73" dark >
              <v-card-title class="text-h5">
                Title : {{ review.title }}</v-card-title>
              <v-card-subtitle>Content : {{ review.content }}</v-card-subtitle>
            </v-card>
            </v-col>
          </router-link>
          </v-rol>   
        </v-container>
        <v-container v-else>
        <v-card>
          <v-card-title class="text-h5">아직 작성한 리뷰가 없습니다</v-card-title> 
        </v-card>
        </v-container>
        </v-card> 
        </v-col>
        <v-col>
           <v-card
        max-width="400"
        class="mx-auto">
        <v-app-bar>   
          <v-toolbar-title>Likes Reviews</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-app-bar>
        <v-container v-if="profileUser.like_reviews">
            <v-rol>
          <router-link
            v-for="review in profileUser.like_reviews" 
            :key="review.id"
            :to="{ name: 'ReviewDetail', params: { id: review.id } }" > 
            <v-col cols="12"> 
            <v-card  color="#385F73" dark >
              <v-card-title class="text-h5">
                Title : {{ review.title }}  </v-card-title>                
              <v-card-subtitle>Content : {{ review.content }}</v-card-subtitle>
            </v-card>
            </v-col>           
          </router-link>
           </v-rol>
        </v-container>
        <v-container v-else>
        <v-card>
          <v-card-title class="text-h5">아직 좋아하는 리뷰가 없습니다</v-card-title> 
        </v-card>
        </v-container>
        </v-card> 
        </v-col>
          
        </v-row>
        <v-row>
        <v-col>
           <v-card
        max-width="400"
        class="mx-auto" >
        <v-app-bar>   
          <v-toolbar-title>My Articles</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-app-bar>
        <v-container v-if="profileUser.articles">
            <v-rol>
            
         
          <router-link
            v-for="article in profileUser.articles" 
            :key="article.id"
            :to="{name: 'ReviewDetail', params: { id: article.id }}" >       
            <v-col cols="12"> 
            <v-card  color="#385F73" dark >
              <v-card-title class="text-h5">
                Title : {{ article.title }}</v-card-title>
              <v-card-subtitle>Content : {{ article.content }}</v-card-subtitle>
            </v-card>
            </v-col>     
          </router-link>
           </v-rol>
        </v-container>
        <v-container v-else>
        <v-card>
          <v-card-title class="text-h5">아직 작성한 게시글이 없습니다</v-card-title> 
        </v-card>
        </v-container>
        </v-card> 
        </v-col>
        <v-col>
           <v-card
        max-width="400"
        class="mx-auto" >
        <v-app-bar>   
          <v-toolbar-title>Likes Articles</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-app-bar>
        <v-container v-if="profileUser.like_articles">
          <v-row>

          <router-link
            v-for="article in profileUser.like_articles" 
            :key="article.id"
            :to="{ name: 'ArticleDetail', params: { id: article.id, article: article, currentUser: currentUser } }">            
            <v-col cols="12">

            <v-card  color="#385F73" dark >
              <v-card-title class="text-h5">
                Title : {{ article.title }}</v-card-title>
              <v-card-subtitle>Content : {{ article.content }}</v-card-subtitle>
            </v-card>
            </v-col>
          </router-link>
          </v-row>
        </v-container>
        <v-container v-else>
        <v-card>
          <v-card-title class="text-h5">아직 좋아하는 게시글이 없습니다</v-card-title> 
        </v-card>
        </v-container>
        </v-card> 
        </v-col>
      </v-row>   
  </div>
</template>

<script>
export default {
  name: 'MyPage',
  data() {
    return {
      profileUser: {}
    }
  },
  props: {
    currentUser: Object,
  },
  methods: {
    getProfileUser() {
      this.profileUser = this.currentUser
    }
  },
  created() {
    this.getProfileUser()
  }
}
</script>

<style>
.profile_container {
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
.profile_header {
  font-family: 'Bebas Neue', cursive;
  color: lightskyblue;
  font-size: 32px;
  margin-bottom: 28px;
}
.profile_container a {
  display: block;
  text-decoration: none;
}


/* media */
@media screen and (min-width: 576px) { 
  .profile {
    font-size: 24px;
    margin: 30px auto 0;
  }
  .profile-header {
    font-family: 'Overpass', sans-serif;;
    font-size: 36px;
    text-align: center;
  }
  .profile-body {
    margin-top: 30px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
  }
  .profile-body-articles-item,
  .profile-body-like-articles-item {
    padding: 10px 15px;
    color: #fcfcfc;
    font-size: 18px;
  }
  .profile-body-like-articles-item {
    background-color: #fcfcfc;
    color: #535c68;
  }
}
@media screen and (min-width: 992px) { 
  .profile {
    font-size: 32px;
    margin: 30px auto 0;
  }
  .profile-header {
    font-size: 44px;
  }
  .profile-body-articles-item,
  .profile-body-like-articles-item {
    padding: 20px 30px;
    color: #fcfcfc;
    font-size: 24px;
  }
  .profile-body-like-articles-item {
    background-color: #fcfcfc;
    color: #535c68;
  }
}
</style>