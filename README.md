AI Blog

AI Blog is a web application designed to share articles and insights on Artificial Intelligence and Machine Learning. You can enter YouTube link and The app will generate a blog. Which is saved in the datebase.

Features

- User Authentication**: Register, login, and manage user accounts securely.
- Article Management**: View the articles.
- Create Blog by entering YouTube Link

Technologies Used

- Backend: Python, Django
- Frontend: HTML, CSS, JavaScript, Tailwind
- Database: PostgreSQL
- Api: Assymbly Ai

Installation

Prerequisites

- Python 3.8+
- pip (Python package installer)
- PostgreSQL database

Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/ai-blog.git
   cd ai-blog
   ```

2. **Set up virtual environment (optional but recommended)**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Database setup**:

   - Create a PostgreSQL database.
   - Update database settings in `settings.py`:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_database_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin)**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

8. **Access the application**:

   Open a web browser and go to `http://localhost:8000` to view the AI Blog. Use the admin interface at `http://localhost:8000/admin` to manage articles and users.

## Contributing

Contributions are welcome! If you'd like to contribute to AI Blog, fork the repository, create a new branch, and submit a pull request.
