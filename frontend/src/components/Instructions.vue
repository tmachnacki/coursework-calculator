<template>
    <v-dialog
    transition="dialog-top-transition"
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            text
            dark
            v-bind="attrs"
            v-on="on"
        >
          <v-icon small class="text-sm-h">mdi-help</v-icon>
          <span class="d-none d-sm-inline ml-1"> help </span> 
          
        </v-btn>
      </template>

      <v-card dark>
        <v-card-title class="headline light-blue white--text">
          Instructions:
      
        </v-card-title>


        <v-divider></v-divider>

        <v-container>
          <ul>
            <li>
              Search for course by entering a course name (i.e. EECS 493) in the search bar 
            </li>
            <li>
              Choose to add the course to your backpack, schedule, or both
            </li>
            <li>
              You can move courses between your backpack and schedule 
            </li>
            <li>
              Remove a course by clicking on the red "X"
            </li>
            <li>Calculate the estimated hours of work per week for your schedule by pressing the calculate button</li>
          </ul>
        </v-container>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="light-blue"
            text
            @click="dialog = false"
          >
            Ok, got it!
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
export default {
    name: 'Instructions',
    props: {
    },
    data() {
        return {
            dialog: false
        }
    }
}
</script>

<style scoped>

</style>
