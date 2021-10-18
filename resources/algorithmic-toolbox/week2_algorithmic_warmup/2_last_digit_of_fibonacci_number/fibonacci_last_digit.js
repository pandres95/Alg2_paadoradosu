// by Alexander Nikolskiy

const readline = require('readline');

async function main (){
    const rl = readline.createInterface({
        input: process.stdin,
        terminal: false
    });
    
    process.stdin.setEncoding('utf8');

    for await (const line of rl) {
        console.log(fib(parseInt(line, 10)));
        process.exit();
    }
}

function fib(n) {
    n = n % 60; // This is because of Pisano Number of 10 is 60
    const f_list = [BigInt(0), BigInt(1)]

    for (let i = 2; i <= n; i++) {
        f_list.push(f_list[i - 1] + f_list[i - 2]);
    }

    const number = f_list[n].toString();
    return number[number.length - 1];
}

module.exports = fib;

if (!module.parent) {
    main();
}