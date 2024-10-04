#Task A1 - Standard Algorithms Input Validation

scores = []

score = int(input("GIVE TEST SCORE >:(( "))
while score <0 or score >100 :
    score = int(input("ERROR!!!! GIVE TEST SCORE >:(( "))

scores.append(score)