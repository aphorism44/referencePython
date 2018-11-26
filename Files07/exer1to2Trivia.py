'''
Created on Nov 18, 2018

@author: domje
'''

from _operator import itemgetter
import sys, pickle


def exit_program():
    input("\n\nPress the enter key to exit.")
    sys.exit()

def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open file " + file_name + ". Ending program.\n", e)
        exit_program()
    else:
        return the_file
    
def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def parse_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    
    questionPoints = next_line(the_file)
    
    explanation = next_line(the_file)
    
    return category, question, answers, correct, explanation, questionPoints

def record_high_score(points):
    high_scores = open("trivia_high_scores.dat", "rb")
    #store as list of tuples of names and scores; limit 5
    highScoreTuples = []
    lowestHighScore = -1
    try:
        highScoreTuples = pickle.load(high_scores)
        if len(highScoreTuples) > 0:
            lowestHighScore = highScoreTuples[len(highScoreTuples) - 1][1]
    except:
        pass
    
    high_scores.close()
    #if it's a high score, add it to list and sort
    #then, if more than 5 items, delete the last one
    high_scores = open("trivia_high_scores.dat", "wb")
    try:
        highScoreTuples = pickle.load(high_scores)
    except:
        pass
    if len(highScoreTuples) < 5 or points > lowestHighScore:
        name = input("What is your name?: ")
        highScoreTuples.append((name, points))
        highScoreTuples.sort(key=itemgetter(1), reverse = True)
        if len(highScoreTuples) > 5:
            del highScoreTuples[len(highScoreTuples) - 1]

    pickle.dump(highScoreTuples, high_scores)
    high_scores.close()

def display_high_scores():
    print("\t\t*** HIGH SCORES ***\n\n")
    high_scores = open("trivia_high_scores.dat", "rb")
    highScoreTuples = pickle.load(high_scores)
    for i in range(0, len(highScoreTuples)):
        print(i + 1, "\tName: ", highScoreTuples[i][0], "\tScore: ", highScoreTuples[i][1], "\n")
    print("\n\n")
    high_scores.close()

def welcome(title):
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
    
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    #first block
    category, question, answers, correct, explanation, questionPoints = parse_block(trivia_file)
    while category:
        #ask question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, " - ", answers[i])
        #get player answer
        answer = input("What's your answer?: ")
        #check answer
        if answer == correct:
            print("\nCorrect for "+ str(questionPoints) + " points!", end = " ")
            score += int(questionPoints)
        else:
            print("\nWrong.", end = " ")
        print(explanation)
        print("Score: ", score, "\n\n")
        #get next block
        category, question, answers, correct, explanation, questionPoints = parse_block(trivia_file)
    trivia_file.close()
    print("That was the last question!")
    print("Your final score is ", score)
    return score
    
    
#trigger program
score = main()
record_high_score(score)
display_high_scores()
exit_program()
