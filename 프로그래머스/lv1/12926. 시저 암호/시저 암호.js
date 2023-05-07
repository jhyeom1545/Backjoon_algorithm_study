// const alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
// function solution(s, n) {
//   let answer = "";
//   for (let i = 0; i < s.length; i++) {
//     if (s[i] === " ") {
//       answer += " "; //s[i]
//     } else {
//       let idx = alphabet.indexOf(s[i]);
//       const word = idx > 25 ? alphabet.slice(26) : alphabet.slice(0, 26);
//       idx = word.indexOf(s[i]) + n;
//       if (word[idx] === undefined) {
//         idx -= 26;
//       }
//       answer += word[idx];
//     }
//   }
//   return answer;
// }
//-------------------------------------------------------
// const lower = "abcdefghijklmnopqrstuvwxyz";
// const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// function solution(s, n) {
//   let answer = "";
//   for (let i = 0; i < s.length; i++) {
//     if (s[i] === " ") {
//       answer += " ";
//     } else {
//       const word = lower.includes(s[i]) ? lower : upper;
//       let idx = word.indexOf(s[i]);
//       if(idx >= 26){
//         idx -= 26
//       }
//       answer += word[idx]
//     }
//   }
//   return answer;
// }

//-------------------------------------------------------

// var lower = "abcdefghijklmnopqrstuvwxyz";
// var upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// function solution(s, n){
//     const answer = s.split('').reduce((acc, cur) => {
//         const word = lower.includes(cur) ? lower : upper
//         let idx = word.indexOf(cur) + n
//         if(idx >= 26) {idx -= 26}
//             return acc + (
//             cur === ' ' ? cur : word[idx])  
//     }, '')
//     return answer
// }
//-------------------------------------------------------
// 아스키코드를 이용한 풀이를 위해 필요한것
// 1. charCodeAt: 주어진 문자의 유니코드 데이터(숫자)를 반환
// 2. String.fromCharCode(): 주어진 유니코드 데이터(숫자)를 문자로 반환
// A ~ Z : 65 ~ 97
// a ~ z : 97 ~ 122

function solution(s, n){
    let answer = ''
    for (let i = 0; i < s.length; i++){
        if(s[i] === ' '){
        answer += s[i]
    } else {
        let idx = s[i].charCodeAt() + n
        if (idx > 122 || (idx > 90 && (idx - n) < 97)){
         idx -= 26
        }
        answer += String.fromCharCode(idx)
    }
    }
    return answer
}