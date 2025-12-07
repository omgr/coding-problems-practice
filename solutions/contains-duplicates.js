function containsDuplicates(nums,runWithoutSet = false){
    if(runWithoutSet){
        let seen = [];
        for(let i = 0; i < nums.length; i++){
            if(seen.includes(nums[i]))
                return true;
            seen.push(nums[i]);
        }
        return false;
    }
    const uniqueNums = new Set(nums);
    return uniqueNums.size !== nums.length;
}

console.log(containsDuplicates([1,2,3,4,5]));
console.log(containsDuplicates([1,2,3,4,5,1]));
console.log(containsDuplicates([1,2,3,4,5,6,7,8,9,10]));
console.log(containsDuplicates([1,2,3,4,5,6,7,8,9,10,1]));
console.log(containsDuplicates([1,2,3,4,5,6,7,8,9,10,1,2]));
console.log(containsDuplicates([1,2,3,4,5,6,7,8,9,10,1,2,3]));
console.log(containsDuplicates([1,2,3,4,5,6,7,8,9,10,1,2,3,4]));
console.log(containsDuplicates([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]));
console.log(containsDuplicates([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6]));
console.log(containsDuplicates([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7]));
console.log(containsDuplicates([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8]));