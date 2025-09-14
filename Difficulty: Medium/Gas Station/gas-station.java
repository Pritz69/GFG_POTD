class Solution {
    public int startStation(int[] gas, int[] cost) {
        // code here
    
        int totalGas = 0, totalCost = 0;
        int start = 0, tank = 0;

        for (int i = 0; i < gas.length; i++) {
            totalGas += gas[i];
            totalCost += cost[i];
            tank += gas[i] - cost[i];

            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }

        return (totalGas < totalCost) ? -1 : start;
    }
}