const path = require('path');
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
            {test: /\.ts$/, loader: 'ts-loader'}
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
    ],
  resolve: {
    extensions: ['.ts', '.js']
  }
};
