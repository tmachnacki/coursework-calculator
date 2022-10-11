<template>

<v-card class="d-flex flex-column" width="270" height="300" elevation="4" dark>
  
  <v-card-title class="d-flex justify-space-between ">
    {{course.name}}
    
    <v-icon class="ma-0 pa-0" color="red" @click="$emit('delete-course')">mdi-close</v-icon>
    
  </v-card-title>
 
  <v-card-subtitle class="text-left">{{course.description}}</v-card-subtitle>
  <v-divider horizontal></v-divider>

  <v-card-text class="text-left mt-3">
    <p class="">Credits: <span class="white--text">{{course.credits}}</span> </p>
    <p class="">Work load: <span class="white--text">{{course.workload}}%</span> </p>
  </v-card-text>
  <v-spacer></v-spacer>

  <v-card-actions>
    <v-btn 
      v-if="type === 'backpack'" @click="$emit('add-to-schedule', course)"
      small
      text
      color="light-blue"
    >
      Add to Schedule<v-icon right>mdi-calendar-check</v-icon>
    </v-btn>

    <v-btn v-if="type === 'schedule'" @click="$emit('add-to-backpack', course)" text small color="light-blue">
      Add to Backpack <v-icon right>mdi-bag-personal</v-icon>
    </v-btn>

    <v-spacer>
    </v-spacer>
  </v-card-actions>
</v-card>
</template>

<script>
// imports

export default {
    name: 'Course',
    props: {
        course: Object,
        type: String,
    },
    emits: ['delete-course', 'add-to-schedule', 'add-to-backpack']
}
</script>


<style scoped>
.outer {

}

</style>