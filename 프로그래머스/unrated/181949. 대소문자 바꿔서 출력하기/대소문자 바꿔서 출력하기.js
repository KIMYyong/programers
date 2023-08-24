const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close', function(){
    const str = input[0];
    let result = "";

    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        if (char >= 'a' && char <= 'z') {
            result += char.toUpperCase();
        } else if (char >= 'A' && char <= 'Z') {
            result += char.toLowerCase();
        } else {
            result += char; // 알파벳이 아닌 경우 그대로 유지
        }
    }

    console.log(result);
});
