# 12. 
# YouTube currently displays a like and a dislike button, 
# allowing you to express your opinions about particular content
# There are two other interesting rules to be noted about the interface:
    # (a) Pressing a button, which is already active, will undo your press.
    # (b) If you press the like button after pressing the dislike button, the like button overwrites the previous
# ”dislike” state. The same is true for the other way round.

# Write a function that takes in a list of button inputs 'events' and returns the final state.
#   Examples:
        # like_or_dislike([ ”dislike”]) → ”dislike”,
        # like_or_dislike([ ”like”, ”like”]) → ”nothing”,
        # like_or_dislike([ ”dislike”, ”like”]) → ”like”,
        # like_or_dislike([ ”like”, ”dislike”, ”dislike”]) → ”nothing”,

def like_or_dislike(events):
    final_state = 'nothing'

    for word in events:
        if word == final_state:
            final_state = 'nothing'
        else:
            final_state = word

    return final_state


lyst_1 = ['dislike']
lyst_2 = ['like','like']
lyst_3 = ['dislike','like']
lyst_4 = ['like','dislike','dislike']

print(like_or_dislike(lyst_1))
print(like_or_dislike(lyst_2))
print(like_or_dislike(lyst_3))
print(like_or_dislike(lyst_4))
