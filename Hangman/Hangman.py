import random
import json
def get_word():
    with open("dictionary.json",'r',encoding='UTF-8') as f:
        dic = json.load(f)
        return random.choice(list(dic.keys()))

def get_best_grade():
    with open("best_grade.json",'r',encoding='UTF-8') as f:
        return int(json.load(f))
    
def update_grade(new):
    past_best_grade = get_best_grade()
    if past_best_grade == 1000:
        past_best_grade = new
        with open("best_grade.json",'w',encoding='UTF-8') as f:
            f.write(json.dumps(new))
            f.close()
    if new < past_best_grade:
        with open("best_grade.json",'w',encoding='UTF-8') as f:
            f.write(json.dumps(new))
            f.close()
        print("You make new best grade!")       
    print(f"past best grade:{past_best_grade} times")

def main():
    answer = get_word()
    show = list('_' * len(answer))
    num = 0
    while True:
        for letter in show:
            print(letter,end='') 
        if '_' not in show:
            break
        guess = input("\nguess a letter please\n")
        num+=1
        for i in range(0,len(answer)):
            if answer[i] == guess:
                show[i] = answer[i]
    print(f"\nYou've tried {num} times!")
    update_grade(num)
    
while True:
    enter = input("Enter 1 to start game, others to exit\n")
    if enter == '1':
        main()
    else:
        break

    
