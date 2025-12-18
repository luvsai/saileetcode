# Last updated: 18/12/2025, 20:18:14
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        
        maxheap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxheap)
        time = 0

        while maxheap:
            temp = []
            flag = False
            if maxheap[0] == -1:
                flag = True
            for _ in range(n +1):
                if maxheap:
                    cnt = heapq.heappop(maxheap)
                    temp.append(cnt)
                    time += 1  # each interval is 1 unit
                else:
                    if not flag:
                        time +=1
                # Do NOT break here inside the for-loop
                # because it fails when len(temp) > 1

            # Push back remaining freqs
            for cnt in temp:
                if cnt + 1 < 0:
                    heapq.heappush(maxheap, cnt + 1)

            # Correct final stopping condition
            if not maxheap:
                break

        return time
        # freq = Counter(tasks)
        
        # maxheap = [-cnt for cnt in freq.values()]
        # heapq.heapify(maxheap)
        # time = 0

        # while maxheap:
        #     temp = []
        #     for _ in range(n + 1):
        #         if maxheap:
        #             cnt = heapq.heappop(maxheap)
        #             temp.append(cnt)
        #         time +=1 # each pick would take 1 unit of time
            
                
            
        #     #push back remaining counts
        #     for cnt in temp:
        #         if cnt + 1 < 0: # since cnt is negative
        #             heapq.heappush(maxheap, cnt + 1)
        #     if not maxheap:
        #         break
        # return time





        # # comeback later . 
        # freq = Counter(tasks)
        # max_freq = max(freq.values())
        # max_count = sum(1 for v in freq.values() if v == max_freq)
        
        # part_count = max_freq - 1
        # part_length = n + 1
        # min_intervals = part_count * part_length + max_count
        
        # return max(len(tasks), min_intervals)