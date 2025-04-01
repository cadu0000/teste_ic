<template>
  <SearchOperadora />
</template>


<script>
import SearchOperadora from './components/SearchOperadora.vue'

export default {
name: 'App',
components: {
  SearchOperadora
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

button {
padding: 10px 20px;
margin-top: 20px;
background-color: #007bff;
color: white;
border: none;
cursor: pointer;
font-size: 16px;
}

button:hover {
background-color: #0056b3;
}
</style>