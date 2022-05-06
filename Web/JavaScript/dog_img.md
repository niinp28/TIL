```html
<script>
    function getDog() {
      const URL = 'https://dog.ceo/api/breeds/list/all'
      axios.get(URL)
        .then(res => {
          const breeds = Object.keys(res.data.message)
          const breed = _.sample(breeds)
          const indiURL = `https://dog.ceo/api/breed/${breed}/images/random`

          const h1 = document.querySelector('h1')
          h1.innerText = `Dog API - ${breed}`
          return axios.get(indiURL)
        })
        .then(res => {
          console.log(res)
          const img = document.querySelector('img')
          img.setAttribute('src', res.data.message)
        })
    }
    const button = document.querySelector('button')
    button.addEventListener('click', getDog)
  </script>
```

