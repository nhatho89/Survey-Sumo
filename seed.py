from django.db import models
from django.utils import timezone
from  import Choice, Question

Question.objects.create(
    question_text = "What is your favorite color?",
    pub_date = timezone.now()
)

Choice.objects.create(
    choice_text = 'red',
    question_id = Question.objects.last(),
    vote = 3
)
Choice.objects.create(
    choice_text = 'blue',
    question_id = Question.objects.last(),
    vote = 4
)
