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
   git clone https://github.com/srikriydv/ai-blog-simple-from-youtube-djnago-practice-3.git
   cd ai-blog-simple-from-youtube-djnago-practice-3
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

## Screenshots

Below are some screenshots of the Photo Simple App:


### Home Page
![home](https://github.com/user-attachments/assets/5151474f-5939-4256-b3d0-ae21f978fc80)

### Login Page
![login](https://github.com/user-attachments/assets/ac6496d2-fbdb-483a-833a-a07573dfc8b8)

### Register Page
![register](https://github.com/user-attachments/assets/08de59bd-ae89-4dfd-9b1b-fff1b20090e4)

### Saved Blog Page
![saved](https://github.com/user-attachments/assets/6e5ec684-743f-4cd7-a2df-790bc6fafa69)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact:
- **Email**: srikri5462ydv@gmail.com
- **GitHub**: [srikriydv](https://github.com/srikriydv)

