// by Alexander Nikolskiy

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.once('line', () => {
    rl.on('line', readLine);
});

function readLine (line) {
    const arr = line.toString().split(' ').map(Number);

    console.log(max(arr));
    process.exit();
}

/**
 * 
 * @param {number[]} arr 
 */
function max(arr) {
    let first = 0, first_ix = 0, second = 0;
    
    for (let i in arr) {
        if (arr[i] > first) {
            first = arr[i];
            first_ix = i;
        }
    }

    for (let i in arr) {
        if (arr[i] > second && i !== first_ix) {
            second = arr[i];
        }
    }

    return first * second;
}

module.exports = max;
