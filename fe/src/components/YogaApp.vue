<template>
  <div>
    <ul>
      <li
        v-for="(pos,i) in positions"
        :key="i">
        {{pos}}  
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'YogaApp',
  data () {
    return {
      positions: [],
    }
  },
  mounted() {
    this.loadPositions();
  },
  methods: {
    async loadPositions() {
      try {
        const response = await axios.get('http://localhost:3000/');
        this.positions = response.data.positions;
        console.log(response);
      } catch (e) {
        console.error('Something went wrong');
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
