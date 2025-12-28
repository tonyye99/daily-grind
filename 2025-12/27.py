# 955. Meeting Rooms III
# Link: https://leetcode.com/problems/meeting-rooms-iii/editorial/?envType=daily-question&envId=2025-12-27
# Time: 15+
# Solved: No 

# TIL: heap can be used, also sorting + counting can be used.
# For sorting + counting, track room availavity time with end time of each meeting time
# count += 1 if room is available, 
# if rooms are not available, check the room with min time (going to end soon) 
# and set it availalbe by (current time - (end - start))
# then find index of the room that has max meetings (return first found)