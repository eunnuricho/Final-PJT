<template>
  <div class="movieform">
    <h2>MOVIE LIST</h2>
    <div class="row row-cols-1 row-cols-md-3 g-4">
    <div v-for="movie in movies" 
    :key="movie.pk">
    <movie-item     
    :movie="movie">   
    </movie-item>    
    </div>
    </div>
  </div>  
</template>

<script>
import MovieItem from '@/components/movies/MovieItem'
import { mapGetters } from 'vuex'
export default {
  name: 'MovieList',  
  components: {
    MovieItem
  },
  methods: {      
  },
  computed: {
    ...mapGetters(['movies'])
  },
  created() {
    this.$store.dispatch('getMovies')
  },

}
</script>

<style>
.movieform h2{
  font-family: 'Bebas Neue', cursive;
  color: lightskyblue
}
</style>