def subsets(nums):
    def backtrack(start, path):
        powerset.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    powerset = []
    backtrack(0, [])
    return powerset

input_set_1 = []
print("introduce the set by spaces ")
input_set_1 = input().split()
output_1 = subsets(input_set_1)
print("Output: \n", output_1)


