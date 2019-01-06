<template>
  <div>
    <h3> Add new position </h3>
    <div>
      <label for="nameField" />
      <input v-model="positionName" id="nameField" name="name" placeholder="sip kombucha">
      <button @click="addPosition(positionName)">Add position</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'AddPosition',
    props: {
      addPosition: {
        type: Function,
        required: true,
      },
    },
    data() {
      return {
        positionName: '',
      }
    },
  }
</script>

<style scoped>

</style>
