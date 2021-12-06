<template>
  <div>    
    <comment-item
      v-for="(comment, idx) in comments"
      :key="idx"
      :comment="comment"
      :review="review"
      >
    </comment-item>             
  </div>
</template>

<script>
import CommentItem from '@/components/reviews/CommentItem'
import { mapGetters } from 'vuex'
export default {
  name: 'CommentList',
  props: {
    review: { //모든 정보
      type: Object,
      required: true,  
    }
  },  
  components: {
    CommentItem
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
  computed: {
    ...mapGetters([
      'comments'
    ])
  },
  created() {
    const commentListSet = {
      review_id: this.review.id,
      token: this.setToken()
    }
    this.$store.dispatch('getComments', commentListSet)
  },
  
}
</script>

<style>

</style>