class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.topVoted = [0] * len(times)
        countVotes = Counter()
        currentTop = persons[0]
        
        for i, (person, time) in enumerate(zip(persons, times)):
            countVotes[person] += 1
            if countVotes[person] >= countVotes[currentTop]:
                currentTop = person
            self.topVoted[i] = (time, currentTop)

    def q(self, t: int) -> int:
        left, right = 0, len(self.topVoted) - 1
        
        while left <= right:
            mid = (left + right) // 2
            time, top = self.topVoted[mid]
            if time == t:
                return top
            if time < t:
                left = mid + 1
            else:
                right = mid - 1

        time, top = self.topVoted[right]
        return top
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)