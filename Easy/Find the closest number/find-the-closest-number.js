//{ Driver Code Starts

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split("\n").map(string => {
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
    for(;i<t;i++){
        
        let n = parseInt(readLine());
        
        
        let k = parseInt(readLine());
        
        
        let arr = new Array(n);
        let input_arr = readLine().split(' ').map(x=>parseInt(x));
        for(let i=0;i<n;i++){
            arr[i] = input_arr[i];
        }
        
        let obj = new Solution();
        let res = obj.findClosest(n, k, arr);
        console.log(res);
    }
}

// } Driver Code Ends



class Solution {
/**
* @param number n
* @param number k
* @param number[] arr

* @returns number
*/
    findClosest(n, k, arr) {
        // code here
        let l=0;
        let h=n-1;
        let closest=arr[0];
        while(l<=h)
        {
            let m = Math.floor((l+h)/2);
            if ( (Math.abs(arr[m]-k) < Math.abs(closest-k)) || ( (Math.abs(arr[m]-k) == Math.abs(closest-k)) && (arr[m] > closest) ) )
            {
                closest=arr[m];
            }
            if (arr[m]<k)
            {
                l=m+1;
            }
            else if(arr[m] > k)
            {
                h=m-1;
            }
            else
            {
                return arr[m];
            }
        }
        return closest;
    }
}
        
