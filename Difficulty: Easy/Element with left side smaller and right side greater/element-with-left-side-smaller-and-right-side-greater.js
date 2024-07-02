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

function printList(res,n){
    let s="";
    for(let i=0;i<n;i++){
        s+=res[i];
        s+=" ";
    }
    console.log(s);
}


function main() {
    let t = parseInt(readLine());
    let i = 0;
    for(;i<t;i++)
    {
        let n = parseInt(readLine());
        let arr = new Array(n);
        let input_ar1 = readLine().split(' ').map(x=>parseInt(x));
        for(let i=0;i<n;i++){
            arr[i] = input_ar1[i];
        }
        let obj = new Solution();
        let res = obj.findElement(arr, n);
        console.log(res);
        
    }
}// } Driver Code Ends




// } Driver Code Ends


//User function Template for javascript


/**
 * @param {number[]} arr
 * @param {number} n
 * @returns {number}
*/

class Solution{
    findElement(arr,n){
        //code here
        const l=[];
        for(let i=0;i<n;i++)
        {
            l[i]=-1;
        }
        l[0]=arr[0];
        for(let i=1;i<n;i++)
        {
            l[i]=Math.max(l[i-1],arr[i]);
        }
        const r=[];
        for(let i=0;i<n;i++)
        {
            r[i]=-1;
        }
        r[n-1]=arr[n-1];
        for(let i=n-2;i>=0;i--)
        {
            r[i]=Math.min(r[i+1],arr[i]);
        }
        for(let i=1;i<n-1;i++)
        {
            if (l[i] <= arr[i] && arr[i] <=r[i])
            {
                return arr[i];
            }
        }
        return -1;
    }
}



