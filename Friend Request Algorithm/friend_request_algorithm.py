user1_friends = {'Shubham', 'Saket', 'Meera', 'Ajay'}
user2_friends = {'Ajay', 'Meera', 'Vijay', 'N.K'}
user3_friends = {'Shubham', 'Meera', 'Rahul'}

def suggest_friends(*args, find_friends_for):
    suggested_friends = set()
    for arg in args:
        fd = arg.difference(find_friends_for)
        suggested_friends.update(fd)

    return suggested_friends

user3_suggested_friends = suggest_friends(user2_friends, user1_friends, find_friends_for=user3_friends)
print(user3_suggested_friends)
