- v-model을 v-model 없이 구현하기

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <input @input="inputMessage" :value="message">
    <div>no v-model : {{ message }}</div>
    <br>
    <br>
    <input type="text" v-model="message2">
    <div>v-model : {{ message2 }}</div>
  </div>
</body>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script> 
  const app = new Vue({
    el: '#app',
    data: {
      message: "",
      message2: ""
    },
    methods: {
      inputMessage(event){
        this.message = event.target.value
      }
    }
  })
</script>
</html>
```

- v-model을 methods 안의 함수를 이용해서 실시간으로 data에 있는 message를 바꿔주는 방식으로 v-model을 구현해보았다. v-bind를 통해서 input 안의 value를 data의 message와 연결시켜주었다.
