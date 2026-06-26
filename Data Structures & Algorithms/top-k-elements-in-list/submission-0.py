class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = {}
        for i in nums:
            if i not in most_freq:
                most_freq[i] = 1
            else:
                most_freq[i] += 1

        most = sorted(most_freq.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in most[:k]]
