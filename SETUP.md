# Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd accuknox-assignment
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

## Verify Installation

Run all tests to verify everything works:

```bash
python manage.py test
```

You should see:
```
Ran 6 tests in X.XXXs
OK
```

## Run Demonstrations

```bash
# Question 1
python manage.py test_sync_signals

# Question 2
python manage.py test_thread_signals

# Question 3
python manage.py test_transaction_signals

# Rectangle Class
python manage.py test_rectangle
```

## Troubleshooting

### Issue: "django-admin not found"
**Solution:** Make sure virtual environment is activated

### Issue: "No module named 'django'"
**Solution:** Run `pip install -r requirements.txt`

### Issue: "No migrations to apply"
**Solution:** This is normal if you've already run migrations

## What's Next?

Once setup is complete, check out the [README.md](README.md) for detailed explanations of each solution.
