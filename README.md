# Django Project Readme
## Project Setup
### Step 1: Create a Virtual Environment

```bash
python -m venv ./.venv
```



This command creates a virtual environment named `.venv` in the project directory.
### Step 2: Activate the Virtual Environment (Windows)

```bash
.\.venv\Scripts\activate
```


### Step 2: Activate the Virtual Environment (Mac/Linux)

```bash
source ./.venv/bin/activate
```


### Step 3: Install Dependencies

```bash
pip install -r ./requirements.txt
```



This command installs all the required dependencies listed in the `requirements.txt` file.
### Step 4: Apply Migrations

```bash
python manage.py makemigrations
```


### Step 5: Apply Database Migrations

```bash
python manage.py migrate
```



These commands apply database migrations, creating necessary database tables based on your Django models.
### Step 6: Run the Development Server

```bash
python manage.py runserver
```



This command starts the development server, and you can access your Django project by visiting [http://127.0.0.1:8000/]()  in your web browser.
## Additional Notes
- Make sure to keep your virtual environment activated while working on the project. 
- Update the `requirements.txt` file when you install new packages using `pip freeze > requirements.txt`. 
- Customize the Django settings in the `settings.py` file according to your project requirements.
- Happy coding!
