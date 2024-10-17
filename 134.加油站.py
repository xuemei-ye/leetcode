class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        i = 0
        while i < n:
            sum_gas = sum_cost = 0
            cnt = 0
            while cnt < n:
                j = (i+cnt) % n
                sum_cost += cost[j]
                sum_gas += gas[j]
                if sum_cost > sum_gas:
                    break
                cnt += 1
            if cnt == n:
                return i
            else:
                i += cnt + 1
        return -1

