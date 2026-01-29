let str = " Hello JavaScript World  "

console.log("원본 str", str);

// .length
console.log('길이: ', str.length);

// .trim: 공백 제거
console.log('공백 제거: ', str.trim());
console.log('원본 str: ', str); //원본 변경X

// 대소문자 변환
console.log('대문자 변환: ', str.toUpperCase()); // HELLO JAVASCRIPT WORLD  
console.log('원본 str: ', str); //원본 변경X

console.log('소문자 변환: ', str.toLowerCase()); // hello javascript world  
console.log('원본 str: ', str); //원본 변경X

// 탐색
console.log('인덱스 찾기: ', str.indexOf('J')) // 7
console.log('인덱스 찾기: ', str.indexOf('Java')) // 7(첫번째 문자 기준) 매개변수로 받은 문자열의 첫 번째 글자 인덱스 반환
console.log('인덱스 찾기: ', str.indexOf('Jva')) // -1 -> 매개변수로 받은 문자열이 없다면 -1 반환

console.log('문자열의 포함 여부 확인: ', str.includes('Java')) // true
// .indexOf()로도 문자열에 포함 여부 알 수 있음 -> -1 반환하면 없다는 것
console.log('문자열의 포함 여부 확인: ', str.includes('Jva')) // false

// 슬라이싱
console.log('슬라이싱: ', str.slice(6, 16)); // llo JavaSc -> 6번 인덱스부터 15번 인덱스 문자열까지만 출력
console.log('원본 str: ', str); //원본 변경X

// 치환
console.log('한 글자 치환: ', str.replace('a', 'e')); // 문자열 중에서 가장 처음 나오는 a라는 문자를 e로 치환
console.log('한 글자 치환: ', str.replace('World', 'Universe')); // 단어도 치환 가능
console.log('전부 치환: ', str.replaceAll('l', 'v')); //Hevvo JavaScript Worvd
console.log('원본 str: ', str); //원본 변경X

// 분할
// ''(공백)을 매개변수로 전달 시 문자열의 모든 글자들이 하나씩 잘려서 배열로 반환
console.log('" 기준 분할: ', str.split('')); // [' ', 'H', 'e', 'l', 'l', 'o', ' ', 'J', 'a', 'v', 'a', 'S', 'c', 'r', 'i', 'p', 't', ' ', 'W', 'o', 'r', 'l', 'd', ' ', ' ']
// " "(공백 한 칸)을 기준으로 문자열을 나눠서 배열로 반환
console.log('" " 기준 분할: ', str.split(' ')); // ['', 'Hello', 'JavaScript', 'World', '', '']
// 분할하는 기준인 매개변수 문자는 사라지고 배열로 만들어져서 반환
console.log('l 기준 분할: ', str.split('l')); // [' He', '', 'o JavaScript Wor', 'd  ']
console.log('원본 str: ', str); //원본 변경X

// 합치기
let str2 = "with JavaScript";
console.log("문자열 합치기: ", str.concat(str2));
console.log(`문자열 합치기2: ${"Hello ".concat(str2)}`);
console.log(`문자열 합치기2: ${"Hello ".concat(str2, str)}`);
console.log(`문자열 합치기2: ${"Hello ".concat("I'm Dongyun2 ", "NICE TO MEET YA")}`);

console.log('원본 str: ', str); //원본 변경X
console.log('원본 str: ', str2); //원본 변경X