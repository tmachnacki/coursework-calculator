# University of Michigan EECS 493 final project: CourseWork Calculator
An SPA built for U of M building their semester schedules. CourseWork 
Calculator is built with Vuetify, Vue, Flask, sqlite, and selenium.

Team members:
- Timothy Machnacki: tmachnac
- John Banna: johnkarm
- Peter Murray: pjmurray
- Robert Stewart: rstewa

## Project setup
For Javascript/Vue:

Config global vue cli in home directory:
```
> cd ~
> npm i -g @vue/cli
```
https://cli.vuejs.org/guide/installation.html

you may need to run clean install of npm (due to weird environment behavior with vue3cli)
```
> cd into frontend/
> rm -rf node_modules package-lock.json && npm install
```

In vsCode:
install Vetur extension (ignore any warning about vetur.tsconfig)

For emmet autocompletion (i.e auto-complete "</tag>" for html tags):
go to settings.json and add:
```
"emmet.includeLanguages": {
    "vue-html": "html",
        "vue": "html"
},
"emmet.syntaxProfiles": {
    "vue-html": "html",
        "vue": "html"
},
```

For Python course493 API:
```
> cd flask-api
> python3 -m venv env
> source env/Scripts/activate
> pip install -r requirements.txt
> pip intall -e .
```

### serves API on port 8000
```
> cd flask-api
> chmod +x bin/serve
> ./bin/serve
```

### serves frontend on port 8080
```
> cd frontend
> npm run serve (run on locolhost port 8080)
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
