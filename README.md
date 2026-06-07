# Outreach Pipeline

A Python-based outreach automation pipeline that automates the process of discovering companies, identifying decision-makers, resolving contact information, and sending outreach emails.

## Overview

This project was built as an outreach automation workflow using multiple third-party APIs.

The pipeline starts with a company domain, discovers relevant business information, finds potential decision-makers, resolves contact details, and prepares them for outreach campaigns.

---

## Architecture

```text
Input Domain
      ↓
Explorium Business Match
      ↓
Company Discovery
      ↓
Prospeo Lead Discovery
      ↓
Email Resolution Layer
      ↓
Brevo Email Delivery
```

---

## Features

* Business matching using Explorium API
* Decision-maker discovery using Prospeo API
* Email resolution layer
* Email delivery using Brevo
* Modular service architecture
* Easily replaceable providers
* Input validation
* Logging support
* Retry-ready structure

---

## Project Structure

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
│   ├── ocean.py
│   ├── prospeo.py
│   ├── eazyreach.py
│   └── brevo.py
│
└── utils/
    ├── logger.py
    ├── retry.py
    └── validators.py
```

---

## Workflow

### 1. Domain Input

The user enters a company domain.

Example:

```text
openai.com
```

---

### 2. Explorium Business Matching

The domain is sent to Explorium's Business Match API.

Example:

```text
openai.com
      ↓
business_id
```

This allows the system to identify and validate the target company.

---

### 3. Lead Discovery

Prospeo Search Person API is used to discover relevant contacts associated with the company.

Examples:

* CEO
* Founder
* CTO
* Engineering Leaders

---

### 4. Email Resolution

The email resolution layer prepares contact email information for outreach workflows.

This layer is isolated behind a service abstraction, making it easy to swap providers without affecting the rest of the application.

---

### 5. Outreach Delivery

Brevo is used to send outreach emails to discovered contacts.

---

## Technologies Used

* Python
* Explorium API
* Prospeo API
* EazyReach
* Brevo
* REST APIs
* Git
* GitHub

---

## Environment Variables

Create a `.env` file:

```env
EXPLORIUM_API_KEY=your_key
PROSPEO_API_KEY=your_key
EAZYREACH_API_KEY=your_key
BREVO_API_KEY=your_key
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running The Project

```bash
python main.py
```

Example:

```text
Enter company domain: openai.com
```

---

## Sample Output

```text
Enter company domain: openai.com

Matching business openai.com

Finding decision makers

Resolving emails

Contacts Found

John Doe openai.com johndoe@openai.com
```

---

## Design Decisions

The project follows a service-oriented architecture where each external provider is isolated behind its own service layer.

Benefits:

* Easy maintenance
* Provider replacement without code changes
* Better testing
* Cleaner separation of concerns

---

## Future Improvements

* Real email verification
* Multi-contact enrichment
* Contact ranking
* Similar company discovery
* Campaign analytics
* Database integration
* Web dashboard

---

## Author

Astha Adhikari
