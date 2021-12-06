<template>
  <div class="movie_container">
    <div class="movielist">    
      <div class="img">
        <img :src="`https://www.themoviedb.org/t/p/original/${movie.poster_path}`" alt="movie_poster">               </div>
        <div class="content">
          <h1>{{ movie.title }}</h1>        
          <p>{{ movie.overview }}</p>    
          <!-- <p>{{ movie.genre_ids }}</p> -->
          <a>
            <router-link :to="{ name: 'MovieDetail', params: { id : movie_pk }}">MOVIE DETAIL</router-link>
          </a>          
        </div>
    </div>
  </div>
</template>

<script>
// import MovieDetail from '@/components/movies/MovieDetail'
export default {
  name: 'MovieItem',
  props: {
    movie: {
      type: Object,
      required: true
    },
  },
  // components: {
  //   MovieDetail
  // },
  data () {
      return {
        movie_pk: this.movie.pk
      }
    },
}
</script>

<style >
.movie_container {
  width: 100%;
  height: 800px;
  position: relative;
  display: flex;
}

.movielist {
  display:flex;
  justify-content: space-between;
  width: 100%;
  height: 100%;
  justify-content: center;
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
.movielist .img{
  display: flex;
  object-fit: contain;   
}
.movielist img{  

  max-width: 100%;
  height: 90%;
  display: block;
  object-fit: cover;
  filter: brightness(80%);  
}

.movielist .content {
  display: flex;
  flex-direction: column;
  background-color: #0009;
  justify-content: center;
  position: absolute;  
  bottom: 100px;
  color: white;
  max-width: 80%;
  text-shadow: 0 0 1px #000;  
  text-align: left;
}

.movielist .content h1{  
  font-size: 2em;  
}

.movielist .content > p{
  
  display: inline-flex;
  width: 100%; 
  white-space: nowrap; 
  overflow: hidden; 
  text-overflow: ellipsis;

  white-space: normal; 
  line-height: 1.2; 
  height: 3.6em; 
  text-align: left; 
  word-wrap: break-word; 
  display: -webkit-box; 
  -webkit-line-clamp: 3; 
  -webkit-box-orient: vertical;
}
.movielist .content a a{
  display: inline-block;
  text-decoration: none;
  color: white;
  background: #0009;
  padding: 10px 15px;
}

.movielist .content a a:hover{
  background: lightskyblue;
}
</style>