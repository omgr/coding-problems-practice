function mergeIntervals(intervals){
    // console.log("start",intervals);
    if(intervals.length <= 1) return intervals;
    intervals.sort((a,b)=>a[0]-b[0]);
    // console.log("sorted",intervals);
    let result = [intervals[0]];
    for(let i=1; i<intervals.length; i++){
        let current = intervals[i];
        let last = result[result.length-1];
        if(current[0] <= last[1]){
            last[1] = Math.max(last[1],current[1]);
        }
        else{
            result.push(current);
        }

    }
    return result;
}

console.log(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]));
console.log(mergeIntervals([[1,4],[4,5]]));
console.log(mergeIntervals([[1,4],[0,4]]));
console.log(mergeIntervals([[1,4],[0,1]]));
console.log(mergeIntervals([[1,4],[0,1]]));