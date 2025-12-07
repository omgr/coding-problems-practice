function validParentheses(s){
    if(s.length === 0 ||s.length % 2 !== 0) return false;
// console.log("came here 1");
    if (['}',']',')'].includes(s[0])) return false;
    // console.log("came here 2");

    const bracketMap = {
        '{':'}',
        '[':']',
        '(':')'
    };
    // console.log("came here 3");

    let stack = [];
    for(let i = 0; i < s.length; i++){
        // console.log("came here loop",i,s[i],stack);
        if(s[i] in bracketMap) stack.push(s[i]);
        if(Object.values(bracketMap).includes(s[i])){
            // console.log("came here in if");
            if(s[i] === bracketMap[stack[stack.length - 1]]) stack.pop();
            else return false;        
        }
        // console.log("------came here loop ending",i,s[i],stack);
    }
    return stack.length === 0;
}

console.log(validParentheses("()"));
console.log(validParentheses("()[]{}"));
console.log(validParentheses("(]"));
console.log(validParentheses("([)]"));
console.log(validParentheses("{[]}"));
console.log(validParentheses(""));
console.log(validParentheses("("));
console.log(validParentheses(")"));
console.log(validParentheses("(["));
console.log(validParentheses("]"));
console.log(validParentheses("({})"));
console.log(validParentheses("({})"));