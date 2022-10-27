

# Problem Statement: There are n-Gas Station in a Circular manner and each station has a capacity of gas[i] liters of gas.
#                   You have a car with an unlimited capacity of gas. You start the journey with an empty tank at one of the gas stations.
#                   Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
#                   The cost of travel from gas station i to gas station i+1 is cost[i] liters of gas.

# You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2..
# Completing the circuit means starting at i and ending up at i again.


# Approach: We will use the concept of Greedy Algorithm to solve this problem.

# Time Complexity: O(n)
# Space Complexity: O(1)


def gas_station(gas:list(),cost:list()) ->int :

    n=len(gas)



    return -1


