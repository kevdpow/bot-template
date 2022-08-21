# bot-template

## Introduction

This README is intended for a bot that schedules tweets.[Perpetually running bots will likely not fall within Heroku's free deployment tier](https://www.heroku.com/pricing).

## Requirements

- Python 3.7+
- Github account
- [Heroku Account](https://signup.heroku.com/)
- Twitter account for bot
- Human account to run bot
- [Developer permissions](developer.twitter.com/) for human account
- [Create your own repo from this template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- Clone repo locally

## Generate Secrets

- Log into bot -> Settings & Privacy -> Account information -> Automation -> Link bot to human account
- Create app within your developer account
- On app dashboard, enable OAuth 1.0a with Read/Write privileges.
- Generate keys for the app in "Keys and Tokens" tab
- Create `.local-secrets` file in local repo (**do not commit**)
- Add the following keys:

```
"TWITTER_API_KEY"= [Your Twitter Api Key]
"TWITTER_API_SECRET"= [Your Twitter Api Secret]
"TWITTER_ACCESS_TOKEN"= [Your Twitter Access Token]
"TWITTER_ACCESS_TOKEN_SECRET"= [Your Twitter Access Token Secret]
```

- `source setenv.sh`

## Develop Bot

- Create virtual environment
  - `python3 -m venv venv`
- `python3 -m pip install -r requirements.txt`
- Create Heroku app
  - [Install Heroku CLI if you haven't](https://devcenter.heroku.com/articles/git)
  - `heroku create YOUR-APP-NAME --buildpack heroku/python`
- Install Heroku Scheduler
  - `heroku addons:create scheduler:standard`
- **Develop bot in `main.py`!**

## Deploy and Schedule bot

- Push changes to Heroku
  - `git push heroku main`
- [Select App in Heroku Dashboard](https://dashboard.heroku.com/apps)
- Click Heroku Scheduler
- Add job
  - Choose your own frequency
  - Scheduler Command: `python main.py`

### Monitor bot

- App Dashboard -> More -> View Logs
