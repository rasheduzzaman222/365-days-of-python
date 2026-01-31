from collections import deque

def sliding_window_max(nums, k):
    dq = deque()
    result = []

    for i, num in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))
