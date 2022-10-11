<template>
  <v-app>
    <nav>
      <v-app-bar app dark dense class="mb-5 black px-md-5 px-1">
        <v-toolbar-title>
          <span class="text-sm-h6 text-body-1">CourseWork Calculator</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <Instructions />
      </v-app-bar>
    </nav>

    <v-main class="app">
    <v-container class="container-main mt-sm-5 mt-1 mx-auto">
      
      <v-card-title class="text-h6 text-sm-h5 white--text py-1 subheading">Choose Your Courses</v-card-title>

      <AddCourse
      @add-to-backpack="addToBackpack"
      @add-to-schedule="addToSchedule"
      />
        
    </v-container>

    <v-container class=" mt-4 mx-auto pa-sm-2 pa-0 container-main">
      <Backpack 
        @add-to-schedule="addToSchedule" 
        @remove-from-backpack="removeFromBackpack" 
        :backpack="backpack" 
        :size="backpack.length"
      />
    
      <v-divider dark></v-divider>
    
      <Schedule
        @add-to-backpack="addToBackpack" 
        @remove-from-schedule="removeFromSchedule" 
        :schedule="schedule"
        :size="schedule.length"
      />
      

      <v-container class="pa-5">

        <v-dialog
          transition="dialog-bottom-transition"
          max-width="500"
        >

          <template v-slot:activator="{ on, attrs }">
            <v-btn 
              large
              color="light-blue"
              class="white--text text-center"
              @click="calculateCourseWork"
              v-bind="attrs"
              v-on="on"
            >
              Calculate<v-icon right>mdi-calculator</v-icon>
            </v-btn>

            <!--
            <v-tooltip bottom >
              <template v-slot:activator="{ on, attrs }">
                <v-icon right        
                  v-bind="attrs"
                  v-on="on"
                  class="white--text my-2"
                >
                  mdi-information 
                </v-icon>
              </template>
              <v-container>We estimate course work by factoring the credit hours, median grade, and Workload</v-container>
            </v-tooltip>
            -->
          </template>

          <template v-slot:default="dialog">  
            <v-card dark>
              <v-toolbar dark color="light-blue">
                Your estimate
              </v-toolbar>

              <v-container>
                <v-card-text v-if="showCalc" class="text-h6 white--text">
                  The estimated work load for your schedule is <span class="light-blue--text"> {{estimate}} </span> hours per week 
                </v-card-text>
              </v-container>

              
              <v-card-actions class="justify-end">
                <v-btn text color="light-blue" @click="dialog.value = false">
                  Close
                </v-btn>
              </v-card-actions>
            </v-card>
          </template>
        </v-dialog>

      </v-container> <!--calc container-->

    </v-container>
    </v-main>
  </v-app>
</template>

<script>
// imports
import AddCourse from './components/AddCourse'
import Backpack from './components/Backpack'
import Schedule from './components/Schedule'
import Instructions from './components/Instructions'

export default {
  name: 'App',

  components: {
    // Instructions,
    Schedule,
    AddCourse,
    Backpack,
    Instructions,

  },

  data: () => ({
    user: {
      username: '',
      password: '',
      isLogged: '',
    },

    showCalc: false,
    showCalendar: false,
    estimate: 0,

    backpack: [],
    schedule: [],
    
  }),

  methods: {

    addToBackpack(newCourse) {
      let tempCourse = this.backpack.find((course) => course.name === newCourse.name)
      if (tempCourse) {
        alert(newCourse.name + " is already in your Backpack!")
      }
      else {
        this.backpack.push(newCourse)
      }
    },

    addToSchedule(newCourse) {
      let tempCourse = this.schedule.find((course) => course.name === newCourse.name)
      if (tempCourse) {
        alert(newCourse.name + " is already in your Schedule!")
      }
      else {
        this.schedule.push(newCourse)
      }
    },

    removeFromBackpack(name) {
      if(confirm('Remove ' + name + ' from your Backpack?')) {
        this.backpack = this.backpack.filter((course) => course.name !== name)
      }
    },

    removeFromSchedule(name) {
      if(confirm('Remove ' + name + ' from your Schedule?')) {
        this.schedule = this.schedule.filter((course) => course.name !== name)
      }
    },

    calculateCourseWork() {
      this.showCalc = true
      this.estimate = 0
      this.schedule.forEach(this.calcCourseHours)
    },

    calcCourseHours(course) {
      console.log(course)
      let prefix = course.department
      let preFactor = 0

      if(
        prefix === 'AEROSP' || 
        prefix === 'AUTO' || 
        prefix === 'BIOMEDE' || 
        prefix === 'CEE' || 
        prefix === 'CHE' || 
        prefix === 'CLIMATE' || 
        prefix === 'EECS' || 
        prefix === 'ENGR' || 
        prefix === 'ENSCEN' || 
        prefix === 'ESENG' || 
        prefix === 'IOE' || 
        prefix === 'MATSCIE' || 
        prefix === 'MECHENG' || 
        prefix === 'MFG' || 
        prefix === 'NAVARCH' || 
        prefix === 'NERS' || 
        prefix === 'SPACE' || 
        prefix === 'TCHNCLCM' || 
        prefix === 'UARTS'
        ) {
          preFactor = 1.285
      }
      else{
          preFactor = 0.7715
      }

      let creditBaseline;
      let workloadFactor;
      let courseEstimate;

      // const workloadFactor = ((course.workload)^(.644905)) * 0.09255
      console.log(course)

      // course.workload === "" ? workloadFactor = 50 : 

      workloadFactor = Math.pow((course.workload/100), 0.618273)
    
      // course.credits === "" ? creditBaseline = 2.5 : 

      creditBaseline = 2.8*course.credits

      courseEstimate = creditBaseline * workloadFactor * preFactor
      
      this.estimate += courseEstimate
    }

  },
};
</script>

<style>
.app{
  background-image: url("../public/background-dark.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;

  
}

.container-main{
  background-color: #000000e8;
  min-width: 305px;
}

.subheading {

}

</style>
