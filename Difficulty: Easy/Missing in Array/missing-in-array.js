//{ Driver Code Starts
// Initial Template for javascript

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => { inputString += inputStdin; });

process.stdin.on('end', _ => {
    inputString =
        inputString.trim().split('\n').map(string => { return string.trim(); });

    main();
});

function readLine() { return inputString[currentLine++]; }

function main() {
    let t = parseInt(readLine());
    let i = 0;
    for (; i < t; i++) {
        let n = parseInt(readLine());
        let arr = new Array(n - 1);
        let input_ar1 = readLine().split(' ').map(x => parseInt(x));
        for (let i = 0; i < n - 1; i++) arr[i] = input_ar1[i];
        let obj = new Solution();
        console.log(obj.missingNumber(n, arr));
    }
} // } Driver Code Ends
// } Driver Code Ends


// User function Template for javascript
/**
 * @param {number[]} array
 * @param {number} n
 * @returns {number}
 */

class Solution {

    // Note that the size of the array is n-1
    missingNumber(n, arr) {

        // code here
        let a=0;
        let s=(n*(n+1))/2;
        for(let i=0;i<n-1;i++)
        {
            a =a+arr[i];
        }
        return s-a;
    }
}