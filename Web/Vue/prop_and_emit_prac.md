# prop and emit practice

- App.vue

```vue
<template>
  <div id="app">
    <h1>APP</h1>
    <input type="text" v-model="appData">
    <p>appData : {{ appData }}</p>
    <p>parentData : {{ parentData }}</p>
    <p>childData : {{ childData }}</p>
    
    <app-parent
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
      @input-parent="inputParent"
      @input-child="inputChild"
    ></app-parent>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data(){
    return {
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  methods:{
    inputParent(data){
      this.parentData = data
    },
    inputChild(data){
      this.childData = data
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```



- AppParent.vue

```vue
<template>
  <div class="parent">
    <h1>AppParent</h1>
    <input type="text" @input="inputParent">
    <p>appData : {{ appData }}</p>
    <p>parentData : {{ parentData }}</p>
    <p>childData : {{ childData }}</p>
    <app-child
      :app-data="appData"
      :parent-data="parentData"
      :child-data="childData"
      @input-child="inputChild"
    ></app-child>
  </div>
</template>

<script>
import AppChild from '@/components/AppChild.vue'
// import AppChild from './AppChild.vue'

export default {
  name: 'AppParent',
  components:{
    AppChild,
  },
  props:{
    appData: String,
    parentData: String,
    childData: String,
  }, 
  methods:{
    inputParent(event){
      this.$emit('input-parent', event.target.value)
    },
    inputChild(data){
      this.$emit('input-child', data)

    }

  }

}
</script>

<style>
</style>
```



- AppChild.vue

```vue
<template>
  <div class="child">
    <h1>AppChild</h1>
    <input type="text" @input="inputChild">
    <p>appData : {{ appData }}</p>
    <p>parentData : {{ parentData }}</p>
    <p>childData : {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props:{
    appData: String,
    parentData: String,
    childData: String,
  },
  methods:{
    inputChild(event){
      this.$emit('input-child',event.target.value)
    }
  }
}
</script>

<style>

</style>
```

