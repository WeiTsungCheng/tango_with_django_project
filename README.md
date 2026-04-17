# Tango with Django — Practice Project

This repository is a hands-on exercise following the *Tango with Django* book, implementing the Rango app and related chapter examples.

---
##  Search and Bing API

The **Bing Web Search API** integration described in the textbook is **no longer usable** as written (API keys, endpoints, or terms may have changed). For the “search pages” flow, this project therefore uses **hard-coded mock JSON** inside `rango/bing_search.py` (`run_query`) so you can still practice the UI and workflow **without** calling the live Bing API.

---

## Common Commands

Run these from the **project root** (the directory that contains `manage.py`).

### Virtual environment (Conda)

```bash
conda activate rango
conda deactivate
```

### Development server

```bash
python manage.py runserver
```

### Tests

```bash
python manage.py test rango
```

### Database migrations

```bash
python manage.py makemigrations rango
python manage.py migrate
```

### Create admin user

```bash
python manage.py createsuperuser
```

### Populate sample data

```bash
python populate_rango.py
```

---
