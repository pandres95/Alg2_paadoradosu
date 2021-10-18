// by Alexander Nikolskiy

const readline = require('readline');

async function main (){
    const rl = readline.createInterface({
        input: process.stdin,
        terminal: false
    });
    
    process.stdin.setEncoding('utf8');

    for await (const line of rl) {
        const [a,  b] = line.split(' ');
        console.log(lcm(Number(a), Number(b)));
        process.exit();
    }
}

function gcd(a, b) {
    if (b === 0) {
        return a;
    }

    return gcd(b, a % b);
}

function lcm(a, b) {
    return a * b / gcd(a, b);
}

module.exports = lcm;

if (!module.parent) {
    main();
}