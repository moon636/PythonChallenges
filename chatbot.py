user_feeling = input("How are you feeling? ")

good_emotions = ["ok","good","amazing","great","happy"]
bad_emotions = ["bad","meh","sad","angry","mad","stressed","stress","depressed"]

good = False

for emotion in good_emotions:
    if emotion in user_feeling:
        print("thats great!")
        break

for emotion in bad_emotions:
    if emotion in user_feeling:
        print("thats not good!")
        break
