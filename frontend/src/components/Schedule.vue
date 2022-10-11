<template>
<v-container class="my-3">
    <v-subheader class="text-h6 text-sm-h5 white--text px-2  subheading" v-text="'Schedule'"></v-subheader>
       
    <v-container class="schedule-container px-5 py-3">
        <v-row class="d-flex justify-sm-start justify-center flex-shrink-1">
            <div dense :key="course.name" v-for="course in schedule" class="ma-2">
                <Course 
                @delete-course="$emit('remove-from-schedule', course.name)" 
                @add-to-backpack="$emit('add-to-backpack', course)"
                type="schedule"
                :course="course" />
            </div>

            <div v-if="size === 0" class="grey--text">
                It looks like you schedule is empty...
            </div>
        </v-row>
    </v-container>
</v-container>
</template>

<script>
// imports
import Course from './Course'

export default {
    name: 'Schedule',
    props: {
        schedule: Array,
        size: Number
    },
    components: {
        Course,
    },
     
    emits: ['remove-from-schedule', 'add-to-backpack'],
}
</script>

<style scoped>

</style>

