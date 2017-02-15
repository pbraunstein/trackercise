const path = require('path');
var webpack = require('webpack');

module.exports = {
    entry: {
        'test': './test.ts',

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
            mangle: {screw_ie8: true}
        })
    ]
};
