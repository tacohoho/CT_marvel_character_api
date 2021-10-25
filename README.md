Marvel Character Collection API


Throughout this week we have been learning how to create a project with flask. More specifically, we have been learning how to create an RESTful Web API that would expose our data from a database to authenticated users.

With this project, you will explore more of that concept! This time though, though the eyes of a marvel comic fan!

The project requires that each individual complete their own code/project, however, you will be placed inside of a think tank group to bounce ideas off of other cohort-mates.

Your Task:
Create a full featured CRUD RESTful Web API of marvel comic characters.

Requirements:
Create Login functionality for users - Email/Password
Associate users to their own collection of marvel super heros
- Each user should have access to create multiple collection/inventory characters but a collection should only belong to one user (One-to-Many Relationship)
Database should be created with PostgreSQL
Virtual environment for project
Marvel Character Model should include AT LEAST the following fields:
- id (Integer)
- name (String)
- description (String)
- date_created (DateTime w/ datetime.utcnow)
- owner (FK to User using the user's token)
(SHOULD have more fields based on your topic)

Users should include the following fields:
- id (uuid)
- name (String)
- email(String)
- password (String)[Hashed]
- token (String)[secret]
- date_created (DateTime)[w/ datetime.utcnow]
- character (relationship)

Packages for project should include (prefaced by pip install)
Flask
Flask-Login
flask-marshmallow
Flask-SQLAlchemy
Flask-Migrate
Flask-WTF
psycopg2 OR psycopg2-binary==2.8.6
python-dotenv
email-validator
Flask-cors
Gunicorn (Deployment)


HINT: To aid in the process of creating your virtual environment with the correct packages:
- name the environment: marvel-env
- copy the text file below into your project
- use the following command prompt/terminal command: pip/pip3 install -r requirements.txt

When Completed:
Once you have created the necessary parts of the project (listed above) and have verified that data can be returned from your API for a given user, commit your code to github and submit the github link. ALSO host on Heroku and submit both links as your submission.