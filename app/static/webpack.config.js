const path = require('path');
var webpack = require('webpack');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
    devtool: 'source-map',
    entry: {
        'hello': './helloWorld.ts'
    },
    module: {
        loaders: [
            {
                test: /\.ts$/,
                exclude: /node_modules/,
                loader: 'ts-loader'
            }
        ]
    },
    output: {
        path: './dist',
        filename: 'bundle.js'
    },
    plugins: [
        new webpack.optimize.UglifyJsPlugin({
            compress: {screw_ie8: true},
            mangle: {screw_ie8: true},
            sourceMap: true
        }),
        new CopyWebpackPlugin(
            [
                {
                    from: './index.html',
                    to: 'index.html'
                }
            ]
        )
    ]
};
