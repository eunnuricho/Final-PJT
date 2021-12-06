# Final Project

> Django 와 Vue 를 이용한 영화 추천 사이트



# MULTIPLUS

> 박준영  : front 
>
> 조은누리 : back



# 개발 기간

>2021.11.17 ~ 2021.11.25



# 개발 환경

### 1. 개발 환경

- Python, Django
- HTML, CSS
- JavaScript, Vue.js



### 2. 설치

- python

```
python -m venv venv
source venv/Scripts/activate
python manage.py migrate
python manage.py loaddata genredata.json
python manage.py loaddata moviedata.json
python manage.py runserver
```

- vue 

```
npm i
npm run serve
```



## 목표

- Django 와 vue 의 연결을 이해하면서 프로젝트 이어나가기
- 한학기 동안 배운 기능 모두 적용해보기 
- 협업툴 적극적으로 사용
- API 활용방법과 데이터의 변환 적용하기





# ERD

![ERD](readme.assets/ERD-16378476781841.jpg)



* 모델 : 영화, 유저, 리뷰, 장르, 댓글
* 추가 사항
  * 게시판을 만들기위해서 이후에 article 모델을 추가하였다.
  * my page에 연결하기위해 user 와 review와 article에  like user 가 M:N 관계설정



# Content

> Home & 로그인 & 회원가입

![preview1](readme.assets/preview1.gif)



>영화 페이지 & 영화 상세 페이지

![preview2](readme.assets/preview2.gif)



>리뷰 페이지 & 리뷰 작성 및 상세 페이지 & 추천 페이지

![preview3](readme.assets/preview3.gif)



> 게시판 페이지 & 게시판 작성 및 상세 페에지 & 마이페이지

![preview4](readme.assets/preview4.gif)





### 사용자 인증

* JWT 사용
  * 필요한 데이터 마다 Token 으로 인증



### 추천 알고리즘

* 로그인한 유저의 리뷰에서 평점을  저장할때 3점 이상일 경우 : movieid 를 출력해 추천 API 실행
  * 3점이상인 리뷰가 2개 이상일 경우 : random 으로 movieid 를 출력해 추천 API 실행
* 로그인한 유저의 리뷰의 모든 평점이 3점 미만일 경우: popular API 실행



### 완료 내용

```
Home & signup & login & logout
영화 페이지
리뷰와 게시판 페이지 & 댓글 기능
추천 알고리즘
마이페이지
```



### 미완성 내용

```
profile 과 comment의 좋아요 기능을 구현했지만
front 에는 data 다루는 법이 익숙하지 않아서 구현하지 못함
css 부분도 전체적으로 부족한 느낌
```



# 느낀점

```
박준영 : 처음에는 어떻게 만들지 하면서 시작했는데 하다보니 코드는 점점길어지고 파일들이 늘어나는 것을 보니 힘들기는 했지만 재미있었다. 
오류도 많이 발생하고 오류를 해결하기 위해서 시간도 많이 들었지만 알아가면서 많이 배운것 같다.
ERD를 확실하게 하고 가야 중간에 실수를 하더라도 쉽게 오류를 해결할 수 있다는 것을 알게 되었음.
추가하고 싶은 기능과 css 를 고급스럽게 하지 못한 것과 마지막까지 오류를 해결하지 못한것이 아쉬운 부분.
하지만 페어와 팀워크가 좋아서 편하게 프로젝트를 진행한 것 같다. 
나와 비슷한 실력을 가진 사람과 진행하면서 서로 부족한 부분을 채워주고 모르는게 있으면 같이 공부하고 오류를 해결해 나가는게 좋았던 것 같다.
```

```
조은누리 : 마지막 프로젝트를 앞두고 그동안 공부를 충분히 잘 따라가지 못했던 것 같아 걱정이 많았는데, 페어를 잘 섭외해서 그래도 많은 걸 배우고 잘 끝난 것 같다. 
그동안 수업에서 내용을 배우고 실습을 했던 것도 물론 도움이 많이 됐지만 실제로 지금까지 중에서는 가장 긴 기간동안 프로젝트 하나를 진행하면서는 다르게 느끼는 점이 많았다. 
생각보다는 잘할 수 있었던 부분도 있었고, 코드가 점점 길어지면서는 내 역량의 부족함을 느끼는 부분도 많았다. 
기능을 하나씩 추가할 때마다 1 + 1 + 1 이렇게 늘어나는 게 아니라 1 + 2 + 6 + 1000000 ..... 이런 식으로 보기가 힘들고 어려워지는 것 같았다. 
vue는 배운지가 얼마되지 않아서 django와 vue 사이에서 데이터를 주고받는 부분에서 가장 에러가 많았던 것 같다. 
그래도 막 배우기 시작한만큼 프로젝트의 결과만 놓고 보기보다는 협업이나 코딩에 있어서 좋은 연습이었다고 생각하고 싶다.
```

