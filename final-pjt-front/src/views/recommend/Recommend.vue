<template>
  <div class="recommend_container">    
    <v-btn color="light-blue lighten-3" @click="recommendmovie">CLICK!!</v-btn>
    <div >
      <div v-for="(movie, idx) in movies_list" 
        :key="idx">
        <div class="recommendlist">    
          <img :src="`https://www.themoviedb.org/t/p/original/${movie.backdrop_path}`" alt="movie_poster">         
          <div class="content">
            <h1>{{ movie.title }}</h1>        
            <p>{{ movie.overview }}</p>
            <a>
            <router-link :to="{ name: 'RecommendDetail', params: { id : movie.id }}">MOVIE DETAIL</router-link>
            </a>  
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'Recommend',   
  data: function () {
    return {
      movies_list : null,
      items: {
        title: null,
        poster: null,
        overview: null,

      }
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
    recommendmovie() {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/recommend/`,
        headers : this.setToken()
      })
      .then(res => {
        console.log(res)
        const recommendmovie_id = res.data.pk
        axios({
        method: 'GET',
        url: `https://api.themoviedb.org/3/movie/${recommendmovie_id}/recommendations?api_key=16d1729d729f6d8c5d36bfaba0aee1a6&language=ko-KR&page=1`,
        })
        .then(res=> {
          console.log(res)
          this.movies_list = res.data.results
        })
      })      
      .catch(err => { 
        console.log(err)         
        axios({
        method: 'GET',
        url: `https://api.themoviedb.org/3/movie/popular?api_key=16d1729d729f6d8c5d36bfaba0aee1a6&language=ko-KR&page=1`,
        })
        .then(res=> {
          console.log(res)
          this.movies_list = res.data.results
        })       
      })
    },    
  },
  created() {
      this.recommendmovie()
    } 
}
</script>

<style>
.recommend_container {
  width: 1200px;
  height: 800px;
  position: relative;
}
.recommend_container > button{ 
  color: black;
  size: 20px;
  padding: 10px;
  margin-bottom: 10px;
  
}
.recommend_container > button:hover{ 
  color: lightskyblue;
  padding: 10px;
  
}

.recommendlist {
  width: 30%;
  height: 30%;
  position: relative;
  animation: fade 1s ease-in-out;
}
@keyframes fade{
  to{
    opacity: 1;
  }
  from{
    opacity: 0;
  }
}

.recommendlist img{
  max-width: 1200px;
  height: 50%;
  display: block;
  object-fit: cover;
  filter: brightness(80%);
}

.recommendlist .content {
  position: absolute;
  left: 50px;
  bottom: 100px;
  color: white;
  max-width: 500px;
  text-shadow: 0 0 1px #000;  
  text-align: left;
}

.recommendlist .content > h1{
  font-size: 2em;  
}

.recommendlist .content > p{
  /* 한 줄 자르기 */ 
  display: inline-block;
  width: 500px; 
  white-space: nowrap; 
  overflow: hidden; 
  text-overflow: ellipsis;
  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal; 
  line-height: 1.2; 
  height: 3.6em; 
  text-align: left; 
  word-wrap: break-word; 
  display: -webkit-box; 
  -webkit-line-clamp: 3; 
  -webkit-box-orient: vertical;
}

.recommendlist .content a{
  display: inline-block;
  text-decoration: none;
  color: white;
  background: #0009;
  padding: 10px 15px;
}

.recommendlist .content a a:hover{
  background: lightskyblue;
}
/* .recommendlist .content > a:hover{
  background: lightskyblue;
} */
</style>