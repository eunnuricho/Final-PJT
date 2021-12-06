import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import vueMoment from 'vue-moment'
// import createPersistedState from "vuex-persistedstate"; 

const SERVER_URL = 'http://127.0.0.1:8000/'
Vue.use(Vuex)
Vue.use(vueMoment)

export default new Vuex.Store({
  plugins: [],
  state: {
    movies: [],
    reviews: [],
    movieTitles: [],
    comments: [],
    comment: null,

    articles: [],
    article_comments: [],
    article_comment: null,
  },
  mutations: {

    // 영화
    GET_MOVIES(state, res) {
      state.movies = res
    },

    GET_MOVIE_TITLES(state, res) {
      const tmp_list = []
      for (var value of res) {
        const tmp = {
          name: value.title, value: value, id: value.pk
        }
        tmp_list.push(tmp)
      }
      state.movieTitles = tmp_list
    },

    // 리뷰
    GET_REVIEWS(state, res) {
      state.reviews = res
    },
    CREATE_REVIEW(state, res) {
      state.reviews = res      
    },
    UPDATE_REVIEW(state, reviewItem) {
      state.reviews = state.reviews.map((review) => {
        if (review === reviewItem) {
          return { ...review,
            title: reviewItem.title,
            content: reviewItem.content,
            rank: reviewItem.rank,
          }
        }  
        return review
      })    
    },
    DELETE_REVIEW(state, reviewItem) {
      const index = state.reviews.indexOf(reviewItem)
      state.reviews.splice(index, 1)
    },
    
    // 댓글
    GET_COMMENTS(state, res) {
      state.comments = res
    },
    CREATE_COMMENT(state, res) {
      state.comments.push(res)
    },
    UPDATE_COMMENT(state, commentItem) {
      state.comments = state.comments.map((comment) => {
        if (comment === commentItem) {
          return { ...comment, content: commentItem.content }
        }
        return comment
      })
    },
    DELETE_COMMENT(state, commentItem) {
      const index = state.comments.indexOf(commentItem)
      state.comments.splice(index, 1)
    },

    // 게시글
    GET_ARTICLES(state, res) {
      state.articles = res
    },
    CREATE_ARTICLE(state, res) {
      state.articles.push(res)
    },
    UPDATE_ARTICLE(state, articleItem) {
      state.articles = state.articles.map((article) => {
        if (article === articleItem) {
          return { ...article,
            title: articleItem.title,
            content: articleItem.content,
          }
        }  
        return article
      })    
    },
    DELETE_ARTICLE(state, articleItem) {
      const index = state.articles.indexOf(articleItem)
      state.articles.splice(index, 1)
    },
    
     // 게시글 댓글
     GET_ARTICLE_COMMENTS(state, res) {
      state.article_comments = res
    },
    CREATE_ARTICLE_COMMENT(state, res) {
      state.article_comments.push(res)
    },

    UPDATE_ARTICLE_COMMENT(state, commentItem) {
      state.article_comments = state.article_comments.map((comment) => {
        if (comment === commentItem) {
          return { ...comment, content: commentItem.content }
        }
        return comment
      })
    },
    DELETE_ARTICLE_COMMENT(state, commentItem) {
      const index = state.article_comments.indexOf(commentItem)
      state.article_comments.splice(index, 1)
    },
  },

  actions: {
    //영화 전체, 제목 가져오기
    getMovies({commit}) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/`,
      })
      .then(res => {
        commit('GET_MOVIES', res.data)
        commit('GET_MOVIE_TITLES', res.data)
      })
      .catch(err => console.log(err))
    },   


    //리뷰 조회 생성
    getReviews({commit}) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/community/`,
      })
      .then(res => {
        commit('GET_REVIEWS', res.data)   
      })
      .catch(err => {
        console.log(err)        
      })
    },    
    createReview({commit}, reviewcreate) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}movies/community/create/`,
        data: reviewcreate.reviewItem,
        headers: reviewcreate.token
      })
      .then(res => {       
        console.log(res)
        commit('CREATE_REVIEW', res.data) 
        router.push({name:'Reviews'})
        router.go()       
      })
      .catch( err => {
        console.log(err)        
      })
    },


    //리뷰 수정 삭제
    updateReview({commit}, updateItem) {
      axios({
        method: 'PUT',
        url: `${SERVER_URL}movies/community/${updateItem.review_id}/`,    
        data: updateItem.reviewItem,
        headers: updateItem.token
      }) 
      .then(res => {       
        console.log(res)
        commit('UPDATE_REVIEW')               
      })
    },
    deleteReview({commit}, deleteItem) {
      axios({
        method: 'DELETE',
        url: `${SERVER_URL}movies/community/${deleteItem.review_id}/`,
        headers: deleteItem.token
      }) 
      .then(res => {       
        console.log(res)
        commit('DELETE_REVIEW') 
        router.push({name:'Reviews'})
      })
    },

    // 댓글 조회 생성
    getComments({commit}, objs) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/community/${objs.review_id}/comment_create/`,
        headers: objs.token
      })
      .then((res) => {
        console.log(res)
        commit('GET_COMMENTS', res.data)
        // router.push({name:'ReviewDetail', params:{id: res.id}})
      })
      .catch(err => console.log(err))
    },
    createComment({commit}, objs) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}movies/community/${objs.review_id}/comment_create/`,
        data: objs.commentItem,
        headers: objs.token
      })
      .then((res) => {
        console.log(res)
        commit('CREATE_COMMENT', res.data)
      })
      .catch(err => console.log(err))
    },


    //댓글 수정 삭제
    updateComment({commit}, objs) {
      axios({
        method: 'PUT',
        url: `${SERVER_URL}movies/community/${objs.review_id}/${objs.comment_id}/`,
        data: objs.commentItem,
        headers: objs.token
      })
      .then((res) => {
        commit('UPDATE_COMMENT', res.data)
        router.push({name:'ReviewDetail', params:{id: objs.review_id }})
      })
      .catch(err => console.log(err))
    },
    deleteComment({commit}, objs) {
      axios({
        method: 'DELETE',
        url: `${SERVER_URL}movies/community/${objs.review_id}/${objs.comment_id}/`,
        headers: objs.token
      })
      .then((res) => {        
        commit('DELETE_COMMENT', res.data)
        router.push({name:'ReviewDetail', params:{id: objs.review_id }})
      })
      .catch(err => console.log(err))
    },

     //게시글 조회 생성
     getArticles({commit}) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}articles/`,
      })
      .then(res => {
        commit('GET_ARTICLES', res.data)   
      })
      .catch(err => {
        console.log(err)        
      })
    },    
    createArticle({commit}, articlecreate) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}articles/create/`,
        data: articlecreate.articleItem,
        headers: articlecreate.token
      })
      .then(res => {       
        console.log(res)
        commit('CREATE_ARTICLE', res.data) 
        router.push({name:'Community'})
        router.go()       
      })
      .catch( err => {
        console.log(err)        
      })
    },

    // 게시글 수정 삭제
    updateArticle({commit}, updateItem) {
      axios({
        method: 'PUT',
        url: `${SERVER_URL}articles/${updateItem.article_id}/`,    
        data: updateItem.articleItem,
        headers: updateItem.token
      }) 
      .then(res => {       
        console.log(res)
        commit('UPDATE_ARTICLE')     
              
      })
    },
    deleteArticle({commit}, deleteItem) {
      axios({
        method: 'DELETE',
        url: `${SERVER_URL}articles/${deleteItem.article_id}/`, 
        headers: deleteItem.token
      }) 
      .then(res => {       
        console.log(res)
        commit('DELETE_ARTICLE')                                
      })
    },

    
    // 게시글 댓글 조회 생성
    getArticleComments({commit}, objs) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}articles/${objs.article_id}/comment_create/`,
        headers: objs.token
      })
      .then((res) => {
        commit('GET_ARTICLE_COMMENTS', res.data)
      })
      .catch(err => console.log(err))
    },
    createArticleComment({commit}, objs) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}articles/${objs.article_id}/comment_create/`,
        data: objs.commentItem,
        headers: objs.token
      })
      .then((res) => {
        commit('CREATE_ARTICLE_COMMENT', res.data)
      })
      .catch(err => console.log(err))
    },


    // 게시글 댓글 수정 삭제
    updateArticleComment({commit}, objs) {
      axios({
        method: 'PUT',
        url: `${SERVER_URL}articles/${objs.article_id}/${objs.comment_id}/`,
        data: objs.commentItem,
        headers: objs.token
      })
      .then((res) => {
        commit('UPDATE_ARTICLE_COMMENT', res.data)
        router.push({name:'ArticleDetail', params:{id: objs.article_id }})    
      })
      .catch(err => console.log(err))
    },
    deleteArticleComment({commit}, objs) {
      axios({
        method: 'DELETE',
        url: `${SERVER_URL}articles/${objs.article_id}/${objs.comment_id}/`,
        headers: objs.token
      })
      .then((res) => {
        commit('DELETE_ARTICLE_COMMENT', res.data)
        router.push({name:'ArticleDetail', params:{id: objs.article_id }}) 
      })
      .catch(err => console.log(err))
    },
  },
  getters: {
    movies(state) {
      return state.movies
    },
    reviews(state) {
      return state.reviews
    },
    movieTitles(state) {
      return state.movieTitles
    },
    comments(state) {
      return state.comments
    },
    articles(state) {
      return state.articles
    },
    article_comments(state) {
      return state.article_comments
    }
  },
  modules: {
  }
})
