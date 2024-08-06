# exercise2.py
# 
# Improved high_scores2_py program.
# Demonstrate improved working with sorting methods.
# 

scores = []
choice = None

# Main part of program
while choice != "0":
    print(
        """
\tHigh Scores 2.0
\t0 - exit
\t1 - show scores
\t2 - add a score
        """
    )
    choice = input("Your choice: ")
    print()

    # Exit
    if "0" == choice:
        print("Goodbye!")

    # Display high-score table
    elif "1" == choice:
        print("High Scores:")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # Add a score
    elif "2" == choice:
        # 1. Sorting the list (scores) with descending order.
        name = input("Put down the player\'s name: ")
        score = int(input("Put down his score: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]         # Keep only top 5 scores

        # 2. Sorting names in the list with ascending order.
        LEN_SCORES = len(scores)
        i = 0
        while i < LEN_SCORES-1:
            if scores[i][0] == scores[i+1][0]:
                j = i
                subitems = []
                while j < LEN_SCORES and scores[i][0] == scores[j][0]:
                    subitems.append((scores[j][1], scores[j][0]))
                    j += 1
                subitems.sort()
                
                reverse_subitems = []
                for item in subitems:
                    reverse_subitems.append((item[1], item[0]))
                scores[i:j] = reverse_subitems
                i = j
            else:
                i += 1

    # Some unknown choice
    else:
        print("Sorry, but", choice, "isn\'t a valid choice.")

input("\n\nPress the key <Enter> to exit.")
