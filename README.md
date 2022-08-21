# Heroku Python Twitter Bot Instructions

## Introduction

This README is intended for a bot that schedules tweets. [Perpetually running bots will likely not fall within Heroku's free deployment tier](https://www.heroku.com/pricing).

## Requirements

- Python 3.7+
- Github account
- [Heroku Account](https://signup.heroku.com/)
- Twitter account for bot
- Human account to link to bot
- [Developer permissions](https://developer.twitter.com/en) for bot account
- [Repo from this template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)

## Generate Secrets

- Create app within your bot developer account
- On app dashboard, enable OAuth 1.0a with Read/Write privileges
- Generate keys for the app in "Keys and Tokens" tab
- Create `.local-secrets` file in local repo (**do not commit**)
- Add the following keys:

```
TWITTER_API_KEY=YOUR-TWITTER-API-KEY
TWITTER_API_SECRET=YOUR-TWITTER-API-SECRET
TWITTER_ACCESS_TOKEN=YOUR-TWITTER-ACCESS-TOKEN
TWITTER_ACCESS_TOKEN_SECRET=YOUR-TWITTER-ACCESS-TOKEN-SECRET
```

- Set secret env vars locally: `sh setenv.sh`

## Develop Bot

- Create and activate virtual environment in local repo
  - `python3 -m venv venv`
  - Mac/OSX: `source venv/bin/activate`
  - Windows: `call venv\Scripts\activate.bat`
- `python3 -m pip install -r requirements.txt`
- Create Heroku app
  - [Install Heroku CLI](https://devcenter.heroku.com/articles/git)
  - `heroku create YOUR-APP-NAME --buildpack heroku/python`
- [Set secret env vars in Heroku](https://devcenter.heroku.com/articles/config-vars): `heroku config:set $(grep -v '^#' .local-secrets)`
- Install Heroku Scheduler
  - `heroku addons:create scheduler:standard`
- **Develop bot in `main.py`!**

## Deploy and Schedule bot

- Log into Twitter bot -> Settings & Privacy -> Account information -> Automation -> Link bot to human Twitter account
- `python3 -m pip freeze > requirements.txt`
- Push changes to Heroku
  - `git push heroku main`
- [Select App in Heroku Dashboard](https://dashboard.heroku.com/apps)
- Click Heroku Scheduler
- Add job
  - Choose frequency
  - Scheduler Command: `python main.py`

### Monitor bot

- App Dashboard -> More -> View Logs
