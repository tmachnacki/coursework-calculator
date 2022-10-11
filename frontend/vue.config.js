module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    port: 8080,
    proxy: 'http://localhost:8000',
  },
}
