# Outreach Pipeline

A Python-based outreach automation pipeline that automates the process of discovering companies, identifying decision-makers, enriching contact information, and sending outreach emails.

---

# Overview

This project automates the outbound prospecting workflow using multiple third-party APIs.

Starting from a company domain, the pipeline:

1. Matches and validates companies using Explorium.
2. Finds relevant decision-makers using Prospeo Search.
3. Retrieves verified email addresses using Prospeo Enrich.
4. Sends outreach emails using Brevo.

---

# Architecture

```text
Input Domain
      ↓
Explorium Business Match
      ↓
Prospeo Search
      ↓
Prospeo Enrich
      ↓
Verified Contact
      ↓
Brevo Email Delivery
```

---

# Features

* Business matching using Explorium API
* Decision-maker discovery using Prospeo Search
* Verified email enrichment using Prospeo Enrich
* Email delivery using Brevo
* Modular service architecture
* Easily replaceable providers
* Input validation
* Logging support
* Retry-ready structure

---

# Project Structure

```text
outreach-pipeline/
│
├── main.py
├── config.py
├── requirements.txt
│
├── models/
│   └── contact.py
│
├── services/
│   ├── exlporium.py
│   ├── prospeo.py
│   └── brevo.py
│
└── utils/
    ├── logger.py
    ├── retry.py
    └── validators.py
```

---

# Workflow

## 1. Domain Input

The user enters a company domain.

Example:

```text
stripe.com
```

---

## 2. Company Matching

The domain is sent to Explorium's Business Match API.

Example:

```text
stripe.com
      ↓
business_id
```

This validates and identifies the target company.

---

## 3. Decision-Maker Discovery

Prospeo Search is used to discover relevant contacts associated with the company.

Examples:

* CEO
* Founder
* CTO
* Engineering Leaders
* Senior Decision Makers

---

## 4. Email Enrichment

Prospeo Enrich is used to retrieve verified email addresses for discovered contacts.

This step converts discovered prospects into outreach-ready contacts.

---

## 5. Outreach Delivery

Brevo is used to send outreach emails to enriched contacts.

---

# Technologies Used

* Python
* Explorium API
* Prospeo API
* Brevo API
* REST APIs
* Git
* GitHub

---

# Environment Variables

Create a `.env` file:

```env
EXPLORIUM_API_KEY=your_key
PROSPEO_API_KEY=your_key
BREVO_API_KEY=your_key
```

---

# Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running The Project

```bash
python main.py
```

Example:

```text
Enter company domain: stripe.com
```

---

# Sample Output

```text
Enter company domain: stripe.com

Finding decision makers

Enriching contact emails

Contacts Found

Thomas Haggarty stripe.com thaggarty@stripe.com
```

---

# Design Decisions

The project follows a service-oriented architecture where each external provider is isolated behind its own service layer.

Benefits:

* Easy maintenance
* Provider replacement without major code changes
* Better testing
* Cleaner separation of concerns
* Modular integrations

---

# Future Improvements

* Multi-contact enrichment
* Contact ranking
* Similar company discovery
* Campaign analytics
* Database integration
* Web dashboard
* Scheduled outreach campaigns

---

# Author

Astha Adhikari
