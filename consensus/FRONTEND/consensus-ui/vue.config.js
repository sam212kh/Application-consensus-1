module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/static/" : "/",
  productionSourceMap: false,
  runtimeCompiler: true,
  chainWebpack: config => {
    config.externals({
      jquery: "jQuery"
    });
  },
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true
      }
    }
  }
};
