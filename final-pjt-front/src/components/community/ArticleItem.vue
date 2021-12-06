<template>  
  <div>
    <div class="article_name">
      <span>
        <router-link :to="{ name: 'ArticleDetail', params: { id : articleItem.id }}">{{ articleItem.title }}</router-link>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: {
      type: Object,
      required: true
    },
  },  
  data: function () {
    return {
      articleItem: {  
        title: this.article.title,
        content: this.article.content,
        id: this.article.id
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
    deleteArticle() {
      const deleteItem = {
        article_id: this.article.id,
        token: this.setToken()
      }      
      console.log(deleteItem)
      this.$store.dispatch('deleteArticle', deleteItem)
    },
    updateReview() {
      const updateItem = {
        articleItem: this.articleItem,
        article_id: this.article.id,
        token: this.setToken()
      }
      console.log(updateItem)  
      this.$store.dispatch("updateArticle", updateItem)    
    }

  },
  created() {
    console.log(this.article)
  }
}
</script>

<style >
.article_name a{
  text-decoration: none;   
}
.article_name a:link{
  color: white;   
}
.article_name a:visited{
  color: white;   
}
.article_name a:hover{
  color: lightskyblue;   
}
</style>