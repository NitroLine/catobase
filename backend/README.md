# Catobase backend

API for сatobase

## Startup

- Setup environment variables or just edit `config.py`
- Install requirements `pip install -r requirements.txt`
- Create database `python migrate.py`
- Startup server `uvicorn main:app --reload`