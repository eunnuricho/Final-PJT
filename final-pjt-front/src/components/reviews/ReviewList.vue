<template>
  <div class="reviewlist">   
    <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            글 번호
          </th>
          <th class="text-center">
            REVIEW TITLE
          </th>
          <th class="text-center">
            USERNAME
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(review, id) in reviews" 
    :key="id" 
        >
          <td>{{ review.id }}</td>        
          <td><review-item :review="review">
        </review-item></td>
        <td>{{review.user.username}}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
  </div>  
</template>

<script>
import {mapGetters} from 'vuex'
import ReviewItem from '@/components/reviews/ReviewItem'
export default {
  name: 'ReviewList',  
  components: {
    ReviewItem
  },    
  computed: {
    ...mapGetters(['reviews'])
  },
  created() {
    this.$store.dispatch('getReviews')
  },
}
</script>

<style>
.reviewlist {
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
.review_items{
  margin: 10px;
}
.review_item{
  display: flex;
  flex-direction: column;
  justify-content: left;
  align-items:flex-start;  
  margin: 30px;
}

</style>