// 1. for문
// 횟수를 기준으로 하는 반복문

console.log('==========================for문============================');

for (let i = 0; i < 10 ; i++) {
    console.log(i);
}

console.log('===========================================================');

for (let i = 0; i <= 10 ; i++) {
    console.log(i);
}

console.log('===========================================================');

for (let i = 10; i <= 1 ; i--) {
    console.log(i);
}

console.log('===========================================================');


// 1부터 100까지 합 구하기
let sum = 0;
for (let i = 0; i < 101 ; i++) {
    sum += i;
}
console.log('1~100까지의 합', sum);

// 실습
// for (let i = 1; i <= 1000; i++) {
//     if (i % 13 == 0 && i % 2 == 1) {
//         console.log(i);
//     }
// }

// let num = Number(prompt('숫자를 입력하세요'));

// for (let i = 1; i <= num; i++) {
//     if (i % 13 == 0 && i % 2 == 1) {
//         console.log(i);
//     }
// }


console.log('===========================================================');

// 이중 for문
console.log('이중 for문');

for (let i = 0; i <= 3; i++) {
    for (let j = 0; j < 5; j++) {
        // i는 고정된 상태로 j만 1씩 커지면서 해당 scope의 코드 실행됨
        // j의 루프가 완료되면 i가 1씩 커지는 것
        console.log('i: ', i, 'j: ', j);
    }
}

// 실습
for (let i = 1; i <= 9; i++) {
    for (let j = 1; j <= 9; j++) {
        console.log(`${i} * ${j} = ${i*j}`);
    }
}

// 2. while 문
// 조건을 기준으로한 반복

console.log('==========================while문============================');

let i = 0;

// 무한루프(i가 계속 0이기 때문)
// while (i < 5) {
//     console.log(i);
// }

while (i < 5) {
    console.log(i);
    i++;
}

console.log('===========================================================');

// let blinker = '초록불';

// while (blinker === '초록불') {
//     console.log('당장 길을 건너세요!');
//     blinker = prompt('신호등 상태를 입력하세요 (초록불/빨간불)');
//     console.log(blinker !== '초록불');
//     console.log(blinker !== '빨간불');
//     // 예외처리
//     blinker = prompt('신호등 상태를 다시 정확하게 입력하세요 (초록불/빨간불)');
// }

// 실습

let yea = 0;

while (i <= 100) {
    if (i % 2 == 0 || i % 5 == 0) {
        yea += i
    }
    i++;
    console.log(yea)
}