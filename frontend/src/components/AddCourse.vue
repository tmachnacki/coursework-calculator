<template>
    <v-container class="">
        <v-row  class="d-flex justify-center "> 
            <div class="d-flex justify-center align-top align-content-top mx-auto col-lg-6 col-md-8 col-sm-8 col-12" >
                <v-text-field
                    dark
                    class="white--text mr-1"
                    outlined 
                    placeholder="i.e. EECS 493" 
                    label="Search for a course" 
                    type="text"
                    v-model="name" 
                    color="white"
                    dense   
                    
                    :disabled="isSearching"
                    @keydown.enter="search()"
                >
                </v-text-field>

                <!--search btn-->
                <v-btn 
                    @click="search()" 
                    class=" white--text ml-1" 
                    color="light-blue"
                    :disabled="isSearching"
                    height="40"
                >
                Search <v-icon right>mdi-card-search</v-icon>
                </v-btn>
            </div>
        </v-row>

        <!--card preview-->
        <v-container fluid class="align-center">
            <v-row class="d-flex justify-center align-center">
                <v-card 
                    class="searching my-auto" 
                    v-if="isSearching" 
                    loading="light-blue"
                    width=250
                    height=300
                    dark
                >
                    <v-card-text>Getting your course info...</v-card-text>
                </v-card>

                <Course v-if="isValid" @delete-course="onClearSearch()" :course="newCourse" />
            </v-row>
        </v-container>

        <!--buttons-->
        <v-container class="mt-5">
            <v-row class="d-flex justify-center align-center px-5 ">
                    
                <v-btn class=" white--text mx-1 my-1" width="150" rounded dark color="light-blue"  :disabled="!isValid" @click="onAddBackpack()">
                    Backpack <v-icon right>mdi-bag-personal</v-icon>
                </v-btn>
            

                <v-btn class="white--text mx-1 my-1" width="150" dark rounded color="light-blue" :disabled="!isValid" @click="onAddSchedule()">
                    Schedule <v-icon right>mdi-calendar-check</v-icon>
                </v-btn>
            

                <v-btn class= "white--text mx-1 my-1" width="150" dark rounded color="light-blue"  :disabled="!isValid" @click="onAddBoth()">
                    Both <v-icon right>mdi-bag-personal</v-icon> <v-icon right>mdi-calendar-check</v-icon> 
                </v-btn>

            </v-row>       
        </v-container>
    </v-container>
</template>

<script>
// imports
import Course from './Course'

export default {
    name: 'AddCourse',
    props: {
    },
    components: {
        Course,
        // TileSpinner,
    },
    data() {
        return {
            newCourse: {},
            name: "",
            isValid: false,
            isSearching: false,

            // temporary db for prototype
            db: [{
                    name: "EECS 493",
                    dept: "EECS",
                    number: "493",
                    credits: 4,
                    medianGrade: 'A',
                    workLoad: 2,
                    description: "User Interface Development",
                },
                {
                    name: "EECS 183",
                    dept: "EECS",
                    number: "183",
                    credits: 4,
                    medianGrade: 'A',
                    workLoad: 2,
                    description: "Elementary programming"
                },
                {
                    name: "EECS 485",
                    dept: "EECS",
                    number: "485",
                    credits: 4,
                    medianGrade: 'B+',
                    workLoad: 29,
                    description: "Web Systems"

                },
                {
                    name: "EECS 482",
                    dept: "EECS",
                    number: "482",
                    credits: 4,
                    medianGrade: 'B+',
                    workLoad: 74,
                    description: "Operating Systems"
                },
                {
                    name: "EECS 376",
                    dept: "EECS",
                    number: "376",
                    credits: 4,
                    medianGrade: 'B',
                    workLoad: 26,
                    description: "Foundations of Computer Science"
                },
                {
                    name: "EECS 370",
                    dept: "EECS",
                    number: "370",
                    credits: 4,
                    medianGrade: 'B+',
                    workLoad: 21,
                    description: "Computer organization"
                }],
        }
    },

    methods: {
        async search() {
            if (!this.name) {
                alert("Please enter a course name")
                return
            }
            this.isSearching = true
            this.isValid = false
            this.newCourse = {}

            console.log("searching")
            
            setTimeout(() => {
                var upperName = this.name.toUpperCase()
                var arr = upperName.split(" ")

                var dept = arr[0]
                var no = arr[1]
                //console.log("dept: ", dept, " no: ", no)
                
                var targetUrl = `/${dept}/${no}`
                // console.log(targetUrl)

                fetch(targetUrl, {
                    method: 'GET', 
                    headers: {"Content-Type": 'application/json'},
                    credentials: 'same-origin',
                })
                    .then((response) => {
                        console.log(response.status)
                        // console.log(response)
                        return response.json()
                    })
                    .then((data) => {
                        if (data && data.classname !== "none") {
                            this.newCourse.name = this.name.toUpperCase()

                            data.department
                                ? this.newCourse.dept = data.department : this.newCourse.dept = ""

                            data.classnumber
                                ? this.newCourse.number = data.classnumber.toString() : this.newCourse.number = ""

                            data.title 
                                ? this.newCourse.description = data.title : this.newCourse.description = ""

                            data.credits
                                ? this.newCourse.credits = data.credits : this.newCourse.credits = ""
                            
                            data.workload
                                ? this.newCourse.workload = data.workload : this.newCourse.workload = ""

                            this.isValid = true
                        }
                        else {
                            this.isValid = false
                            alert("We couldn't find anything on " + this.name)
                        }
                        this.isSearching = false
                        this.name = ""
                    })
                    .catch((error) => {
                        this.isValid = false
                        this.isSearching = false
                        this.name = ""
                        console.log(error)
                    })
            }, 500)
        },

        onAddBackpack() {
            const addedCourse = this.newCourse
            this.$emit('add-to-backpack', addedCourse)
        },
        
        onAddSchedule() {
            const addedCourse = this.newCourse
            this.$emit('add-to-schedule', addedCourse)
        },

        onAddBoth() {
            const addedCourse = this.newCourse
            this.$emit('add-to-backpack', addedCourse)
            this.$emit('add-to-schedule', addedCourse)
        },

        onClearSearch() {
            this.name = ""
            this.isValid = false
            this.newCourse = {}
        },
    },
}
</script>

<style scoped>
.search {
    width: 50%;
}

.searching {
    width: 40%;
}
</style>
