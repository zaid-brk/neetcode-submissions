
''' 
testing i can safely write notes here
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer = [0] * len(temperatures)

        line = []

        # current_day is the index, current_temp is the temperature
        for current_day, current_temp in enumerate(temperatures):

            # While there is someone in line, AND the current temperature is
            # warmer than the temperature of the 
            while line and current_temp > temperatures[line[-1]]:

                past_day = line.pop()

                answer[past_day] = current_day - past_day

            line.append(current_day)

        return answer

