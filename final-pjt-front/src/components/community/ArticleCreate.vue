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
          <span class="headline">Article Create</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="제목"
                  v-model.trim="articleItem.title"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-textarea
                  solo
                  label="내용"
                  v-model.trim="articleItem.content"
                  required
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
          <large>사전 고지 없이 삭제 될 수 있습니다.</large>
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
            @click="createArticle"
          >
            작성
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    </div>
</template>

<script>
export default {
  name: 'ArticleCreate',  
  data() {
    return {
      articleItem: {
        title: null,
        content: null,
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
    createArticle() {     
      const articlecreate = {
      articleItem: this.articleItem,      
      token: this.setToken()
    }
    this.$store.dispatch('createArticle', articlecreate)
    this.title = null,
    this.content = null,
    this.dialog = false    
    }
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

</style>