# Django URL Shortener

A simple URL shortener built with Django that allows users to shorten long URLs and provides a quick way to copy the shortened link.

## Features

- Shorten long URLs
- easy interface

## Usage
- Shorten a URL

1. Enter a long URL in the input field.
2. Click the "Shorten" button.
3. A shortened URL will be displayed below the form.


## Technologies Used

- Django
- HTML/CSS (with Google Fonts)

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Anniymm/url-shortener.git
   cd url-shortener
   venv/bin/activate  # On Windows, use `venv\Scripts\activate`

 ### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies:

```bash
pip install -r requirements.txt
```

### 4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
### 4. Access the Application::
```bash
python manage.py runserver
```
## License

This project is licensed under the MIT License. For more details, please see the [LICENSE](LICENSE) file.





