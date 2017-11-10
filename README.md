Local Development

1. Open command prompt and cd into 'Desktop'

2. Run 'git clone https://github.com/nhatho89/Survey-Sumo.git'

3. Install dependencies 'pip3 install -r requirements.txt'

4. cd into the Survey Sumo project and seed the data (seed data not implemented yet).
   Run 'python3 manage.py createsuperuser' in the project to create super user.

5. Run 'python3 manage.py runserver'

6. Open 'http://localhost:8000/admin/' for admin rights. Sign in with previously
   written super user. From here you can create/view poll questions and choices.

7. Open project at 'http://localhost:8000/polls/' using any browser


![Survey Sumo Home Page](.polls/static/polls/images/polls.png)
