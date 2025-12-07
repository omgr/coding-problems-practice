function twoSumIndices(nums,target){
    if(nums.length === 0 || target <= 0) return [];
    let seen = {};
    for(let i=0; i<nums.length; i++){
        let lookUp = target - nums[i];
        if(seen[lookUp] !== undefined){
            return [seen[lookUp],i];
        }
        seen[nums[i]] = i;
    }
    return [];
}

console.log(twoSumIndices([2,7,11,15],9));
console.log(twoSumIndices([3,2,4],6));
console.log(twoSumIndices([3,3],6));
console.log(twoSumIndices([],0));
console.log(twoSumIndices([1],1));
console.log(twoSumIndices([1,2],3));
console.log(twoSumIndices([1,2,3,4,5],7));
console.log(twoSumIndices([1,2,3,4,5],10));
console.log(twoSumIndices([1,2,3,4,5],15));