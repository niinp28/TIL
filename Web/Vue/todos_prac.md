# Vuex practice

- Index.js

```js
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
      {
        title: '공부',
        is_completed: false,
        data: new Date().getTime()
      },
      {
        title: '휴식',
        is_completed: false,
        data: new Date().getTime() + 1
      },
    ]
  },
  getters: {
    completedTodosCount(state){
      return state.todos.filter(todo => {
        return todo.is_completed
      }).length
    },
    incompletedTodosCount(state){
      return state.todos.filter(todo => {
        return !todo.is_completed
      }).length
    }
  },
  mutations: {
    CREATE_TODO(state, todoItem){
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem){
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO(state, todoItem){
      state.todos = state.todos.map(todo => {
        if (todo === todoItem){
          return {
            ...todo,
            is_completed : !todoItem.is_completed
          }
        }
        else{
          return todo
        }
      })
    }
  },

  actions: {
    createTodo({ commit }, todoItem){
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo({ commit }, todoItem){
      commit('DELETE_TODO', todoItem)
    },
    updateTodo({ commit }, todoItem){
      commit('UPDATE_TODO', todoItem)
    }
  },
  modules: {
  }
})
```



- App.vue

```vue
<template>
  <div id="app">
    <h1>Application</h1>
    <p>완료한 할 일 갯수 : {{ completedTodosCount }}</p>
    <p>완료하지 못한 할 일 갯수 : {{ incompletedTodosCount }}</p>
    <todo-list></todo-list>
    <todo-form></todo-form>
  </div>
</template>

<script>
import TodoForm from './components/TodoForm.vue'
import TodoList from './components/TodoList.vue'
// import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed:{
    completedTodosCount(){
      return this.$store.getters.completedTodosCount
    },
    incompletedTodosCount(){
      return this.$store.getters.incompletedTodosCount
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



- TodoForm

```vue
<template>
  <div>
    <input type="text" @keyup.enter="inputTodo">
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  methods: {
    inputTodo(event){
      const todoTitle = event.target.value.trim()

      if (todoTitle){
        const todoItem = {
          title : todoTitle,
          is_completed: false,
          date : new Date().getTime()
        }
        this.$store.dispatch('createTodo', todoItem)
      }
      event.target.value = ""

    }
  }
}
</script>

<style>

</style>
```



- TodoList.vue

```vue
<template>
  <div>
    <h1>Todo List</h1>
    <ul>
      <todo-list-item
        v-for="todo in todos"
        :key="todo.date"
        :todo="todo"
      ></todo-list-item>
    </ul>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'
export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos(){
      return this.$store.state.todos
    }
  }
}
</script>

<style>

</style>
```

여기서 `:todo='todo'`의 의미:

​	`:todo`는 props를 통해 자식 컴포넌트로 내려주기 위해 쓰는 것

​	`"todo"`는 v-for 구문에 있는 todo

- TodoListItem

```vue
<template>
  <div>
    <li>
      <span 
      :class="{ 'iscompleted' : todo.is_completed }"
      @click="updateTodo(todo)">{{ todo.title }}</span>
      <button @click="deleteTodo(todo)">삭제하기</button>
    </li>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props:{
    todo: Object,
  }, 
  // methods: {
  //   deleteTodo(){
  //     this.$store.dispatch('deleteTodo', this.todo)
  //   }
  methods: {
    ...mapActions(['deleteTodo', 'updateTodo'])
  }
  }


</script>

<style>
.iscompleted{
  text-decoration: line-through;
  
}
span{
  cursor: pointer;
}
</style>
```

