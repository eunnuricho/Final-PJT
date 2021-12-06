import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'

// accounts
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MyPage from '@/views/accounts/MyPage'
import Profile from '@/views/accounts/Profile'

// movies
import MovieList from '@/views/movies/MovieList'
import MovieItem from '@/components/movies/MovieItem'
import MovieDetail from '@/components/movies/MovieDetail'
import Recommend from '@/views/recommend/Recommend'
import RecommendDetail from '@/views/recommend/RecommendDetail'

// reviews
import Reviews from '@/views/reviews/Reviews'
import ReviewItem from '@/components/reviews/ReviewItem'
import ReviewDetail from '@/components/reviews/ReviewDetail'

// community
import Community from '@/views/community/Community'
import ArticleList from '@/components/community/ArticleList'
import ArticleDetail from '@/components/community/ArticleDetail'


const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(() => {
        return window.location.reload()
    })
};
 

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'Home',
    component: Home,
  },

  // accounts
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/MyPage',
    name: 'MyPage',
    component: MyPage,
    props: true,
  },
  {
    path: '/accounts/:id',
    name: 'Profile',
    component: Profile,
    props: true,
  },

  // movies
  {
    path: '/movies/movielist',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/movies/movieitem',
    name: 'MovieItem',
    component: MovieItem,
  },
  {
    path: '/movies/:id',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true,
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend,
  },
  {
    path: '/recommend/:id',
    name: 'RecommendDetail',
    component: RecommendDetail,
  },

  // reviews
  {
    path: '/reviews',
    name: 'Reviews',
    component: Reviews,
    props: true
  },  
  {
    path: '/reviews/item',
    name: 'ReviewItem',
    component: ReviewItem,
  },
  {
    path: '/reviews/:id',
    name: 'ReviewDetail',
    component: ReviewDetail,
    props:true
  },

  // community
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/community/articles',
    name: 'ArticleList',
    component: ArticleList,
    props: true
  },
  {
    path: '/community/:id',
    name: 'ArticleDetail',
    component: ArticleDetail,
    props: true
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
