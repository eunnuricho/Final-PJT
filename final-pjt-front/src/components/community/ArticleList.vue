<template>
  <div class="articlelist">   
    <v-simple-table dark>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            글 번호
          </th>
          <th class="text-center">
            ARTICLE TITLE
          </th>
          <th class="text-center">
            USERNAME
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(article, id) in articles" 
    :key="id" 
        >
          <td>{{ article.id }}</td>        
          <td><article-item :article="article">
        </article-item></td>
        <td>{{article.user.username}}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
  </div>    
</template>

<script>
import {mapGetters} from 'vuex'
import ArticleItem from '@/components/community/ArticleItem'
export default {
  name: 'ArticleList',  
  components: {
    ArticleItem,
  },    
  computed: {
    ...mapGetters(['articles'])
  },
  created() {
    this.$store.dispatch('getArticles')
  },
}
</script>

<style>
.articlelist {
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
.article_items{
  margin: 10px;
}
.artivle_item{
  display: flex;
  flex-direction: column;
  justify-content: left;
  align-items:flex-start;  
  margin: 30px;
}
</style>