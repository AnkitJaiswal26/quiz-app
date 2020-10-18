from django.db import models
from django.contrib.auth.models import User
class Test(models.Model):
    user = models.ForeignKey(User, unique = False, on_delete = models.CASCADE)
    testId = models.TextField(unique = True)
    # question=models.ForeignKey(Question, unique = False, on_delete = models.CASCADE)

class Question(models.Model):
    statement = models.TextField(unique = True)

    optionA = models.TextField()
    optionB = models.TextField()
    optionC = models.TextField()
    optionD = models.TextField()
    
    CorrectOption = models.CharField(max_length = 2)
    questionId = models.TextField(unique = True)
    subject = models.CharField(max_length = 50, null = False)
    test = models.ForeignKey(Test, unique = False, on_delete = models.CASCADE)



class testScoreData(models.Model):
    # take a foreign key of test class.
    # Make a feild for user
    # Add Score.
    test = models.ForeignKey(Test, unique = False, on_delete = models.CASCADE)
    user = models.ForeignKey(User, unique = False, on_delete = models.CASCADE)
    scoreOfUser = models.BigIntegerField(default = 0)

    #primary_y unique......

#User input : Test Name(maths), user, score=> display;
# Test=> submitted : user, test, score

# User=> start the test => Test(Call) => Load questions(Questions) => Correct answer =>
# Jinja(html) temp, temp += 1, Submit click,  testScoreData, store(logged in user, test, temp)



# as in, id should depend on the subject, id should be such that, we can access the question later.