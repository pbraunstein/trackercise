const path = require('path');
var webpack = require('webpack');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
    devtool: 'source-map',
    entry: {
        'main': './main.ts'
    },
    module: {
        loaders: [
            {test: /\.css$/, loader: 'raw-loader'},
            {test: /\.html$/, loader: 'raw-loader'},
            {test: /\.ts$/, loader: 'ts-loader'},
            {test: /\.woff($|\?)|\.woff2($|\?)|\.ttf($|\?)|\.eot($|\?)|\.svg($|\?)/, loader: 'url-loader'}
        ]
    },
        output: {
        path: './dist',
        filename: 'bundle.js'
    },
    plugins: [
        new CopyWebpackPlugin(
            [
                {
                    from: './index.html',
                    to: 'index.html'
                }
            ]
        ),
        new webpack.ProvidePlugin(
            {
                jQuery: 'jquery',
                $: 'jquery',
                jquery: 'jquery'
            }
        )
    ],
  resolve: {
    extensions: ['.ts', '.js']
  }
};
