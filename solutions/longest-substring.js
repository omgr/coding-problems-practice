function longestSubstring(s){
    let left =0,right = 0;
    let maxLength = 0;
    let charSet = new Set();
    while(right < s.length){
        // console.log("Data at start of loop-->",left,right,charSet,maxLength);
        if(!charSet.has(s[right])){
            // console.log("came here in if",left,right,charSet);
            charSet.add(s[right]);
            right++;
            maxLength = Math.max(maxLength,right-left);
        }
        else{
            // console.log("new char in else",left,right,s[left]);
            // console.log("came here in else",left,right,charSet);
            charSet.delete(s[left]);
            // console.log("deleted char in else",charSet);
            left++;

        }
        // console.log("Data at end of loop-->",left,right,charSet,maxLength);
    }
    return maxLength;
}

console.log(longestSubstring("abcabcbb"));
console.log(longestSubstring("bbbbb"));
console.log(longestSubstring("pwwkew"));
console.log(longestSubstring(""));
console.log(longestSubstring("a"));
console.log(longestSubstring("ab"));
console.log(longestSubstring("abc"));
console.log(longestSubstring("abcd"));
console.log(longestSubstring("abcde"));
console.log(longestSubstring("abcdef"));
console.log(longestSubstring("abcdefg"));