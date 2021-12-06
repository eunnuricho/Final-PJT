<template>
  <div class="createform">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="light-blue lighten-3" v-bind="attrs" v-on="on">
          Create
        </v-btn>
      </template>
      <v-card dark>
        <v-card-title>
          <span class="headline">Review Create</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-autocomplete
                :items="movieTitles"
                item-text="name"
                item-value="value"
                v-model="movie_data"
                label="영화 선택"
                required
              ></v-autocomplete>              
              <v-text-field
                label="제목"
                v-model.trim="reviewItem.title"
                required
              ></v-text-field>              
              <v-col cols="6">
                <v-rating
                  v-model="reviewItem.rank"
                  color="light-blue accent-"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  half-increments
                  hover
                  large
                ></v-rating>
              </v-col>
              <v-col cols="6" class="rank_text">
                <h5>
                  {{ reviewItem.rank }}
                </h5>
              </v-col>
              <v-col cols="12">
                <v-textarea
                  solo
                  label="내용"
                  v-model.trim="reviewItem.content"
                  required
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
          <large>평점에 따라 추천영화가 달라질 수 있습니다.</large>
        </v-card-text>
        <v-card-actions>          
          <v-btn          
          color="light-blue accent-"
          @click="dialog = false"
          >
            취소
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
          
          color="light-blue accent-"         
          @click="createReview"
          >
            작성
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'ReviewCreate',  
  data() {
    return {
      movie_data: null ,
      reviewItem: {
        movie_title: null,            
        title: null,
        content: null,
        rank: 2.5,  
        movie_pk: null
      },
      dialog: false,
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
    
    createReview() {     
      this.reviewItem.movie_title = this.movie_data.title
      this.reviewItem.movie_pk = this.movie_data.pk
      const reviewcreate = {
      reviewItem: this.reviewItem,      
      token: this.setToken()
    }
    console.log(reviewcreate)
    this.$store.dispatch('createReview', reviewcreate)
    this.movie_title = null,
    this.movie_pk = null,
    this.title = null,
    this.content = null,
    this.dialog = false    
    }
  },
  computed: {
    ...mapGetters([
      'movieTitles'
    ])
  },
  created() {
    this.$store.dispatch('getMovies')    
  },  
}
</script>

<style>
.createform{
  margin-top: 20px;
  display: flex;
  justify-content: right;
  font-family: 'Noto Sans KR', sans-serif;     
}

.rank_text {    
  display: flex;
  justify-content: center;
  align-items: center;
}  
</style>