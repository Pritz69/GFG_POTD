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
        let arr = readLine().trim().split(" ").map((x) => parseInt(x));
        let obj = new Solution();
        let res=obj.PalinArray(arr,n);
        console.log(res);
    
    }
}

// } Driver Code Ends


//User function Template for javascript

/**
 * @param {number[]} arr
 * @param {number} n
 * @return {number}
*/

class Solution {
    palin(arr)
    {
        let l=0;
        let r=arr.length-1;
        while(l<=r)
        {
            if (arr[l]!=arr[r])
            {
                return false;
            }
            l +=1;
            r -=1;
        }
        return true;
    }
    PalinArray(arr,n){
        //code here
        for(let i=0;i<arr.length;i++)
        {
            let t=arr[i].toString();
            if (this.palin(t)==false)
            {
                return 0;
            }
        }
        return 1;
    }
}