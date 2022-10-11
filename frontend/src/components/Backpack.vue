<template>
    <v-container class="my-3">
        <v-subheader class="text-h6 text-sm-h5 white--text px-2 subheading" v-text="'Backpack'"></v-subheader>
        
        <v-container class="backpack-container px-5 py-3">
            <v-row class="d-flex justify-sm-start justify-center flex-shrink-1">
                <div :key="course.name" v-for="course in backpack" class="ma-2">
                    <Course 
                    @delete-course="$emit('remove-from-backpack', course.name)" 
                    @add-to-schedule="$emit('add-to-schedule', course)"
                    type="backpack"
                    :course="course"/>
                </div>

                <div v-if="size === 0" class="grey--text">
                    It looks like your backpack is empty...
                </div>
            </v-row>
        </v-container>
    </v-container>
</template>

<script>
// imports
import Course from './Course'

export default {
    name: 'Backpack',
    props: {
        backpack: Array,
        size: Number
    },
    components: {
        Course,
    },
    
    emits: ['remove-from-backpack', 'add-to-schedule'],
}
</script>

<style scoped>
  
</style>
