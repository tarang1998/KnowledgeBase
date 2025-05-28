class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letterLogs = []

        digitLogs = []

        for log in logs:

            flog = log.split(" ")
            if flog[1].isdigit():
                digitLogs.append(log)

            else :
                letterLogs.append([flog[0]," ".join(flog[1:])])

        letterLogs = sorted(letterLogs, key = lambda x: (x[1],x[0]))
        
        result = []

        for log in letterLogs:
            result.append(log[0] + " " + log[1])

        for log in digitLogs:
            result.append(log)

        return result
        