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
            {test: /\.ts$/, exclude: /node_modules/, loader: 'ts-loader'},
            {test: /\.css$/, loader: 'style-loader!css-loader'},
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
