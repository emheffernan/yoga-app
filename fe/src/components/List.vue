<template>
  <div>
    <h3>Positions</h3>
    <div>
      <ul>
        <div v-for="(pos,i) in positions" :key="i">
          <li>
            {{pos}}
            <button @click=deletePosition(pos)>
              Remove
            </button>
          </li>
        </div>
      </ul>
    </div>
  </div>
</template>

<script>

export default {
  name: 'List',
  props: {
    positions: {
      type: Array,
      required: true,
    },
    deletePosition: {
      type: Function,
      required: true,
    },
  },
}
</script>

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
