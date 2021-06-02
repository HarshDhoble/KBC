from questions import QUESTIONS
def isAnswerCorrect(question, answer):
    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    temp=question["answer"]
    print(temp)
    return True if answer == temp else False
def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    op="option"+str(ques["answer"])
    print(op)
    count=2
    for i in range(1,5):
        if ques[op]!=ques["option"+str(i)] and count>0 :
            count-=1
            ques["option"+str(i)]="Incorrect"
    return ques
def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print("Welcome to game")
    min1=0
    sum=0
    for i in range(0,15):
        print(f'\tQuestion {1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        if ans == "LIFELINE" :
            print("\You have used your lifeline ")
            QUESTIONS[i]=lifeLine(QUESTIONS[i])
            print("\nThe New Options are")
            print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
            print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
            print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
            print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
            ans = input('Your choice ( 1-4 ) : ')
        # check for the input validations
        if ans == "quit":
            print("You have select a quit option")
            break
        if isAnswerCorrect(QUESTIONS[i], int(ans) ):
            if i<4:
                min1=0
            elif i>3 and i<9:
                min1=10000
            else:
                min1=320000
            sum=sum+QUESTIONS[i]["money"]
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            print("\nThe amount won until Now : ",sum)
            if(i==4):
                print("\nYou have crossed your 1st padhav minimum ammount you will win is ",min1)
            if(i==9):
                print("\nYou have crossed your 2nd padhav minimum ammount you will win is ",min1)
        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            print(f'\nCorrect as is : {QUESTIONS[i]["answer"]}')
            print("\n You have Won : ",min1)
            return
        # print the total money won in the end.
    res=max(min1,sum)
    print("\nThe total money won : ",res)
kbc()
