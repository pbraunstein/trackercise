const path = require('path');

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
    }
};
