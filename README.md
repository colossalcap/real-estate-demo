# 🏠 Cloud-Native Real Estate Demo

A full-stack property listing web app I built during my **Solution Engineering internship at Oracle Singapore** (Sep 2022 – Feb 2023). It was a pre-sales demo for a real estate client. It was designed as a reusable template that the team could reskin for clients in other industries.

**Stack:** Python · Flask · Flask-WTF · SQLAlchemy · cx_Oracle · Oracle Autonomous Database · Oracle Content Management · Oracle Integration Cloud · HTML/CSS/JS (Bootstrap)

---

## ✨ What it does

| Feature | How it works |
|---|---|
| **Property listings** | Listing data is stored in **Oracle Autonomous Database** and accessed through cx_Oracle and SQLAlchemy |
| **Listing images from a headless CMS** | `/get-listing-images` pulls content items from the **Oracle Content Management** REST API, so marketing can update images without a redeploy |
| **AI image scanning on upload** | `/uploadFile` sends uploaded property photos to an **Oracle Integration Cloud** flow that calls a vision API to analyse the image |
| **Multi-page front end** | Home, Explore, Listing, Upload, Login, Sign-up and Contact pages, built with Jinja2 templates |

## 🏗️ Architecture

```
Browser ──► Flask app (routes.py)
              ├──► Oracle Autonomous Database   (listings, users)      via cx_Oracle
              ├──► Oracle Content Management    (listing images)        via REST
              └──► Oracle Integration Cloud     (image-scanning flow)   via REST
```

## 📁 Project structure

```
real-estate-demo/
├── real-estate-demo.py     # Entry point
├── app/
│   ├── __init__.py         # Flask app setup
│   ├── routes.py           # Page routes + OCM / OIC integrations
│   ├── database.py         # Oracle Autonomous DB connection
│   ├── Forms.py            # WTForms (login, sign-up, upload)
│   ├── templates/          # Jinja2 pages
│   └── static/             # CSS, JS, images
├── base-templates/         # Original Bootstrap templates the UI was adapted from
├── requirements.txt
└── .env.example            # Credentials template (never committed)
```

## 🚀 Running it locally

> You need your own Oracle Cloud tenancy (Autonomous DB, Content Management and Integration Cloud) to run it end to end. The original demo environment is no longer live.

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # then fill in your Oracle credentials
flask run
```

**Oracle Instant Client:** download it with your database wallet in `network/admin` into `Oracle-client/instantclient_21_7`, or set `ORACLE_CLIENT_DIR` to point to it. Neither the client nor the wallet is committed to this repo.

## 📚 What I learned

- Connecting a Python web app to managed cloud services (database, headless CMS and integration platform) through their REST APIs
- Keeping credentials out of source control with environment variables
- Building a demo that can be reused across clients rather than one tied to a single customer

---

*Built by [Hanzalah Hisam](https://github.com/colossalcap) · Oracle Cloud Infrastructure Foundations Associate*
