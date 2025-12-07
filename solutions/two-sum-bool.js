function hasPairWithSum(arr, target) {
    // Early exit for edge cases
    if(arr.length === 0 || target <= 0){
        return false;
    }
    
    let hashSet = {};
    
    for(let i = 0; i < arr.length; i++){
        var lookUp = target - arr[i];
        
        if(hashSet[lookUp] !== undefined){
            return true;
        }
        
        hashSet[arr[i]] = i;
    }
    
    return false;
}

// Test cases
console.log("Test 1:", hasPairWithSum([1,3,8,2,5,6], 11)); // should be true (3+8 or 5+6)
console.log("Test 2:", hasPairWithSum([1,2,3], 10));        // should be false
console.log("Test 3:", hasPairWithSum([2,7,11,15], 9));     // should be true (2+7)
console.log("Test 4:", hasPairWithSum([], 5));              // should be false (empty array)
console.log("Test 5:", hasPairWithSum([5], 5));             // should be false (single element)

