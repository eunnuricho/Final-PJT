<template>
  <div>
    <comment-item
      v-for="(comment, idx) in article_comments"
      :key="idx"
      :comment="comment"
      :article="article"
    >
    </comment-item>
  </div>
</template>

<script>
import CommentItem from '@/components/community/CommentItem'
import { mapGetters } from 'vuex'
export default {
  name: 'CommentList',
  props: {
    article: {
      type: Object,
      required: true,
    }
  },
  data () {
    return {
      articledetail: this.article.id
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
      'article_comments'
    ])
  },
  created() {
    const commentListSet = {
      article_id: this.article.id,
      token: this.setToken()
    }
    console.log(commentListSet)
    this.$store.dispatch('getArticleComments', commentListSet)
  },
}
</script>

<style>

</style>