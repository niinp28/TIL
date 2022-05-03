# 0503 workshop

```html
# base.html
<script src="https://kit.fontawesome.com/cb1774b497.js" crossorigin="anonymous"></script>

# index.html
{% extends 'base.html' %}

{% block content %}
  ...
  {% for article in articles %}
    ...
    <div>
      <form class="like-form" data-article-pk="{{ article.pk }}">  
        {% if user in article.like_users.all %}
          <button id="input-{{ article.pk }}">
            <i class="fa-solid fa-thumbs-down" style="color:brown"></i>
          </button>
          {% else %}
          <button id="input-{{ article.pk }}">
            <i class="fa-solid fa-thumbs-up" style="color:blue;"></i>
          </button>
        {% endif %}
      </form>
      <p id="cnt-{{ article.pk }}">좋아요 수 : {{ article.like_users.all.count }}</p>
    </div>
    ...
  {% endfor %}

  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  
  
  <script>
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const forms = document.querySelectorAll('.like-form')
    forms.forEach(form => {
      form.addEventListener('submit', function(event) {
        event.preventDefault()
        const articlePk = event.target.dataset.articlePk
        axios({
          method: 'post',
          url: `/articles/${articlePk}/likes/`,
          headers: {
            'X-CSRFToken': csrftoken
          }
        })
        .then(res => {
          const liked = res.data.liked
          const likedCnt = res.data.likeCnt
          const p = document.querySelector(`#cnt-${articlePk}`)
          p.innerText = `좋아요 수 : ${likedCnt}`
          const button = document.querySelector(`#input-${articlePk}`)
          if (liked === true) {
            button.innerHTML = '<i class="fa-solid fa-thumbs-down" style="color:brown"></i>'
          } else {
            button.innerHTML = '<i class="fa-solid fa-thumbs-up" style="color:blue;"></i>'
          }
          
        })
      })
    })
    
</script>
{% endblock content %}

# profile.html

...
{% block content %}
...

{% with followers=person.followers.all followings=person.followings.all %}
  <div id="follow-cnt">
    팔로워 : {{ followers|length }} / 팔로우 : {{ followings|length }}
  </div>

  <div>
    {% if user != person %}
      <form data-person-pk="{{ person.pk }}" id="follow-form">
        {% if user in followers %}
        <button><i class="fa-solid fa-heart-crack"></i></button>
        {% else %}
        <button><i class="fa-solid fa-heart" style="color: red;"></i></button>
        {% endif %}
      </form>
    {% endif %}
  </div>
{% endwith %}
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <script>
    const form = document.querySelector('#follow-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const personPk = form.dataset.personPk

    form.addEventListener('submit', function(event){
      event.preventDefault()
      axios({
        method: 'post',
        url: `/accounts/${personPk}/follow/`,
        headers: {
          'X-CSRFToken' : csrftoken
        } 
      })
      // axios.post(`/accounts/${personPk}/follow/`)
        .then(res => {
          const liked = res.data.liked
          const button = document.querySelector('button') // if 문 안의 button 태그이므로 하나만 해도 됨
          if (liked === true) {
            button.innerHTML = '<i class="fa-solid fa-heart-crack"></i>'
          } else {
            button.innerHTML = '<i class="fa-solid fa-heart" style="color: red;"></i>'
          }
          const followCnt = document.querySelector('#follow-cnt')
          const followerCnt = res.data.follower_cnt
          const followingCnt = res.data.following_cnt
          followCnt.innerText = `팔로워 : ${followerCnt} / 팔로우 : ${followingCnt}`
        })
    })
  </script>
{% endblock content %}
```

```python
# views.py(accounts)
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(), pk=user_pk)
        me = request.user

        if me != you:
            if you.followers.filter(pk=me.pk).exists():
            # if me in you.followers.all():
                # 언팔로우
                you.followers.remove(me)
                liked = False
            else:
                # 팔로우
                you.followers.add(me)
                liked = True
            context ={
                'liked' : liked,
                'follower_cnt' : you.followers.count(),
                'following_cnt' : you.followings.count(),
            }

        return JsonResponse(context) # 이제 비동기이므로 페이지를 리다이렉트 할 필요없음
        # return redirect('accounts:profile', you.username)
    return redirect('accounts:login')

# views.py(articles)
@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        # 이 게시글에 좋아요를 누른 유저 목록에 현재 요청하는 유저가 있다면.. 좋아요 취소
        # if request.user in article.like_users.all(): 
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            liked = False
        else:
            article.like_users.add(request.user)
            liked = True
        context = {
            'liked': liked,
            'likeCnt': article.like_users.count(),

        }
        return JsonResponse(context)
    return redirect('accounts:login')
```

- 실습 진행하면서 유의한 점 정리
  - index 페이지는 게시글들이 for문으로 정리되어 여러 게시글이 표시되는데, 각각의 좋아요 기능을 구현하기 위해 태그를 선택하는 과정에서 `querySelectorAll`을 사용했다. 그 이후 `forEach`를 통해 이벤트를 구현했다.
  - 각 게시글 마다 좋아요를 구현해야하기 때문에 pk를 받아오기 위해 form 태그 안에는 `data-article-pk`를 설정한 후 `articlePk` 변수에 `event.target.dataset.articlePK`로 할당해주었다. 할당 방법을 모르겠으면 `console.log`로 event의 내용을 확인하면 어떤 식으로 받아야 할 지 알 수 있다.
  - axios를 post 요청으로 보낼 때의 형식을 새로 배웠다. url은 전에 변수에 저장해둔 것을 이용한 템플릿 리터럴로 저장한다. csrf 토큰은 공식 문서를 참조하여 `csrftoken` 변수에 정해진 형식대로 저장, 이것을 headers에 `'X-CSRFToken' : csrftoken `형태로 저장한다.
  - 비동기식으로 좋아요/팔로우를 구현하는 것이므로 기존 form 태그 안에 있던 action값과 method는 더 이상 필요 없음을 이해했다.
  - views.py 에서 liked라는 플래그와 likeCnt라는 좋아요/팔로우 수를 담아 context로 만들어 JsonResponse로 넘겨준다. axios에서 이 컨텍스트를 `.then`함수의 res 인자로 넘겨주기 때문에
    이후 변수를 할당할 때 `res.data.liked`와 같은 형태로 이루어짐을 이해했다.
  - 아이콘을 사용하기 위해 폰트어썸을 이용하였고 버튼 태그 안에 i 태그가 들어가는 형태이므로
    `innerHTML`을 이용하여 liked 플래그에 따라 변경되도록 해주었다.

