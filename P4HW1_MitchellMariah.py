#Mariah Mitchell
#3 May 2025
#P4HW1
#Programmed a number scored list using a loop

num_scores=int(input('How many scores do you want to enter? '))
num = 1
score_list=[]
A_score = 90
B_score = 80
C_score = 70
D_score = 60

#Ask user to input number scores
print()
while num <= num_scores:
    print('Enter score #{}: '.format(num), end= '')
    score = float(input())
    
    if (score < 0) or (score > 100):
        print()
        print('INVALID Score entered!!!!')
        print('Should be between 0 and 100')

    else:
        score_list.append(score)
        num += 1 
print()
print()
#Display a resut summary
print('-----------Results------------')
print('Lowest Score: ', min(score_list))
lowest_scored = min(score_list)

score_list.remove(lowest_scored)

#Display a list of scores
print('Modified List: ',score_list)
average_scores = sum(score_list) / len(score_list)
print(f'Score Averaged: {average_scores:.2f}')

if average_scores >= A_score:
    print('Grade: A')
elif average_scores >= B_score:
    print('Grade: B')
elif average_scores >= C_score:
    print('Grade: C')
elif average_scores >= D_score:
    print('Grade: D')
else:
    print('Grade: F')
print('-------------------------------')
