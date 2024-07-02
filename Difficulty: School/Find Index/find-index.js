//{ Driver Code Starts
//Initial Template for javascript


'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}


function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let n = parseInt(readLine());
        let a=readLine().trim().split(" ").map((x) => parseInt(x));
        let key = parseInt(readLine());
        let obj = new Solution();
        let res = obj.findIndex(a,n,key);
        let s = "";
        for(let it of res){
            s+=it+" ";
        }
        console.log(s);
    }
}

// } Driver Code Ends


//User function Template for javascript

/**
 * @param {number[]} a
 * @param {number} n
 * @param {number} key
 * @return {number[]}
*/

class Solution {
    findIndex(arr,n,key){
       //code here
       const a = [-1, -1];
        
        // Find the first occurrence of the key
        for (let i = 0; i < n; i++) {
            if (arr[i] === key) {
                a[0] = i;
                break; // Stop after finding the first occurrence
            }
        }
        
        // Find the last occurrence of the key
        for (let i = n - 1; i >= 0; i--) {
            if (arr[i] === key) {
                a[1] = i;
                break; // Stop after finding the last occurrence
            }
        }
        
        return a;
    }
}
