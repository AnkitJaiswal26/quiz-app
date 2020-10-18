from django.shortcuts import render, redirect
import numpy as np

# Create your views here.
from .models import testScoreData , Question, Test

def quiz(request):
    test = Test.objects.first()
    questions = test.question_set.all()
    physics_questions = test.question_set.filter(subject = 'physics')
    chemistry_questions = test.question_set.filter(subject = 'chemistry')
    maths_questions = test.question_set.filter(subject = 'maths')
    phy_dict = dict()
    math_dict = dict()
    chem_dict = dict()
    counter = 1
    for p in physics_questions:
        phy_dict[counter] = p
        counter += 1

    counter = 1
    for c in chemistry_questions:
        chem_dict[counter] = c
        counter += 1

    counter = 1
    for m in maths_questions:
        math_dict[counter] = m
        counter += 1

    temp = None
    user_is_on = 0

    context = {
        'phys_dict' : phy_dict,
        'maths_dict' : math_dict,
        'chem_dict' : chem_dict,
        'temp' : temp,
        'user_is_on' : user_is_on

    } 
    print("-----------------------------------------")
    print(phy_dict)
    print("-----------------------------------------")
    score = 0

    if request.method == 'POST':
        for i in range(90):
            options.append(request.POST.get(questions[i].questionId))             
            
        for option in options:
            if option == questions[i].CorrectOption:
                score += 1
            elif option == None:
                pass
            else:
                score -= 1
        return redirect('quiz')
        
    else:
        return render(request, 'quiz/quiz.html', context)