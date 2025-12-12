# 3433. Count Mentions Per User
# Link: https://leetcode.com/problems/count-mentions-per-user/description/?envType=daily-question&envId=2025-12-12
# Time: 40+ mins
# Solved: Yes

# TIL: question is too long but my understanding is correct and able to solve it by hashmap, set and sorting
# I just copied the sorting logic so it's TODO for me.
def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
    online = set(range(numberOfUsers))
    offline = {}
    result = [0] * numberOfUsers

    # print('before', online)
    events.sort(key=lambda e: (int(e[1]), e[0] == "MESSAGE"))

    for event, t, message in events:
        if event == 'OFFLINE':
            # print('->', event, t, message, online)
            offline[int(message)] = int(t)
            if int(message) in online:
                online.remove(int(message))
        if event == 'MESSAGE':
            if message == 'HERE':
                # print(offline)
                # print(online)
                for i in range(numberOfUsers):
                    if i in online:
                        result[i] += 1
                    for key in offline:
                        # print('offline', i, key, t)
                        if i == key and int(t) - offline[i] >= 60:
                            result[i] += 1
            elif message == 'ALL':
                for i in range(numberOfUsers):
                    result[i] += 1
            else:  
                ids = message.split(' ')
                for s in ids:
                    user_id = int(s[2:])
                    result[user_id] += 1
    
    return result