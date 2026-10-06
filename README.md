# Job Tracker

A web app to keep track of the jobs you have applied for, update their status, and check how well your resume matches a job description.

**Live demo:** https://jobtrack-06zi.onrender.com

> The demo runs on a free hosting plan. If it has been idle, the first load can take 30 to 60 seconds while the server wakes up.

## Features

- Sign up and log in (each user sees only their own applications)
- Add, edit, and delete job applications
- Update the status of an application (Applied, Interview, Offer, Rejected)
- Search by company or role, and filter by status
- Pagination for long lists
- Dashboard counts for total, applied, interview, offer, and rejected
- **Resume match:** paste your resume and a job description to get a match score based on skill overlap

## Tech stack

- **Backend:** Python, Django
- **Database:** SQLite locally, PostgreSQL (Neon) in production
- **Frontend:** Django templates (HTML/CSS)
- **Deployment:** Render, gunicorn, WhiteNoise

## Run it locally

1. Clone the repo and open the folder:

   ```
   git clone https://github.com/Shub9276/jobtrack.git
   cd jobtrack
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
   ```

3. Install the packages:

   ```
   pip install -r requirements.txt
   ```

4. Create the database tables:

   ```
   python manage.py migrate
   ```

5. Turn on debug mode for local use, then start the server:

   ```
   set DEBUG=True               # Windows (Command Prompt)
   export DEBUG=True            # Mac/Linux
   python manage.py runserver
   ```

6. Open http://127.0.0.1:8000/

Locally the app uses a SQLite file (`db.sqlite3`). No other setup is needed.

## Environment variables (production)

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Django secret key (a long random string) |
| `DATABASE_URL` | PostgreSQL connection string |
| `DEBUG` | Leave unset in production (defaults to off) |
| `PYTHON_VERSION` | Python version for Render (for example `3.13.6`) |

## Project structure

```
config/      project settings and main URL routes
tracker/     the app: models, views, forms, matcher, URLs
templates/   HTML templates
build.sh     build script used by Render
```

## How the match feature works

The matcher compares the skills mentioned in your resume with the skills found in a job description. It returns a match score and the skills you are missing.

## Future improvements

- Smarter matching (TF-IDF or an AI model)
- Follow-up reminders and interview dates
- Charts on the dashboard
- A REST API using Django REST Framework

## Author

Built by [Shub9276](https://github.com/Shub9276).
