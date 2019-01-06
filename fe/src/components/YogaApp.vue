<template>
  <div>
    <AddPosition :addPosition="addPosition" />
    <List :positions="positions" :deletePosition="deletePosition"/>
  </div>
</template>

<script>
import axios from 'axios';
import List from './List';
import AddPosition from './AddPosition';
export default {
  name: 'YogaApp',
  components: {
      List,
      AddPosition,
  },
  data () {
    return {
      positions: [],
    }
  },
  mounted() {
    this.getPositions();
  },
  methods: {
    async getPositions() {
      try {
        const response = await axios.get('http://localhost:3000/');
        this.positions = response.data.positions;
        console.log(response);
      } catch (e) {
        console.error('Something went wrong');
      }
    },
    async addPosition(posName) {
      try {
        const response = await axios.post('http://localhost:3000/', {position_name: posName});
        this.getPositions();
      } catch (e) {
        console.log('Could not add position');
      }
    },
    async deletePosition(posName) {
      try {
        const response = await axios.delete('http://localhost:3000/', {position_name: posName});
        this.getPositions();
      } catch (e) {
        console.log('Could not delete position');
      }
    },
  }
}
</script>
