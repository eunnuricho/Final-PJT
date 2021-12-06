<template>
  <div class="detailbtn">
    <div>   
      <div>
        <v-row>
          <v-card dark>
            <v-toolbar dark>   
              <v-spacer></v-spacer>          
              <v-spacer></v-spacer>
              <v-toolbar-title>                                   MOVIE DETAIL</v-toolbar-title>
              <v-spacer></v-spacer>         
              <v-spacer></v-spacer>
              <v-btn icon dark @click="golist"            
              ><v-icon>mdi-close</v-icon>
              </v-btn>          
            </v-toolbar>
            <v-container class="detail_container"><v-row>
              <v-col cols="5">
              <img class="detailimg"
              max-height="700"
              max-width="350"
              :src="`https://www.themoviedb.org/t/p/w500/${movie.poster_path}`" alt="movie_poster">
              </v-col>
                <v-col cols="7">
                  <v-list>
                    <v-list-item-content>
                    <v-list-item-subtitle>Movie Title</v-list-item-subtitle>
                    <v-list-item-title> <h3>{{ movie.title}}</h3></v-list-item-title>                   
                    </v-list-item-content>
                    <v-list-item-subtitle>Genres</v-list-item-subtitle>
                    <v-list-item class="genre_list">                      
                      <v-span v-for="genre in movie.genre_ids"
                      :key="genre.id">
                      <span>{{genre.name}}</span>
                      </v-span>                   
                    </v-list-item>
                    <v-list-item-subtitle>Rank</v-list-item-subtitle>
                    <v-rating
                      v-model="rank"                  
                      color="light-blue accent-"
                      background-color="grey darken-1"
                      empty-icon="$ratingFull"
                      half-increments
                      hover
                      large
                      readonly
                    ></v-rating>
                    <v-list-item-content>
                    <p>{{movie.release_date}}</p>
                    </v-list-item-content>
                  <v-list-item-content><p>{{movie.overview}}</p></v-list-item-content>
                </v-list>
              </v-col>
            </v-row></v-container>        
          </v-card>
        </v-row>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'RecommendDetail',
  data () {
      return {
        movie_id : this.$route.params.id,
        rank : null,
        movie : null
      }
    },
  methods : {
    golist() {
      this.$router.push({name: 'Recommend'})
    },
    getMoviesDetail() {
        axios({
          method: 'GET',
          url: `${SERVER_URL}movies/${this.$route.params.id}/`,
        })
        .then(res => {
          this.movie = res.data
          this. rank = (Math.round(this.movie.vote_average))/2
          console.log(this.movie)
        })
        .catch(err => console.log(err))
      },
  },
  created() {
    this.getMoviesDetail()
  },
}
</script>

<style >
.detailbtn {
  font-family: 'Noto Sans KR', sans-serif;    
  background-color: #0009;
  display: flex;
  flex-direction: column; 
  border-radius: 5px;
  box-sizing: border-box;
  width:1100px;
  margin: 0;
  max-width: 1100px;
  padding: 10px 30px 20px; 
  align-items: center;
  text-decoration: none;
  color: white;

}

.detailimg {
  max-width: 100%;
  height: 90%;
  display: block;
  object-fit: cover;
}
p {    
  white-space: normal;
}
.genre_list {
  display: flex;
  justify-content: space-around;
}
</style>