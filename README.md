### INF601 - Advanced Programming in Python
### Sayed Husain Alawi
### Final Project

## Sayed Movie Meter

## Description
This project is a web-based movie review platform developed using Django, a high-level Python web framework. 
The platform is designed to allow users to express their opinions and thoughts on various films through reviews. 
Users can create accounts, log in, search for movies, post reviews, and manage their own reviews through edit and delete 
functionalities. Each review can include a rating and textual feedback, which collectively contribute to the average 
user rating displayed on each movie's detail page.

## Getting Started

### Prerequisites

1. Ensure you have Python installed on your system. The project is developed using Python 3.12.1. 
You can download it from [python.org](https://www.python.org/downloads/).


2. Get the needed APIs
   - Navigate to [RapidApi](https://rapidapi.com/) portal, & register a new user if you don't already have one.  
   - Navigate to the [Movies Tv Shows Database](http://rapidapi.com/amrelrafie/api/movies-tv-shows-database), and subscribe for an API
   - Navigate to [Streaming Availability](http://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability)
     - On the left side, change the version to V3 instead of V4
     - On the yellow warning message, click on "Connect to current App"

<br>

### Dependencies

1. Configuring APIs
   * Rename .env.sample to .env
   * open .env file and insert your API Keys


2. Navigate to mysite folder:
   ```bash
   cd mysite
   ```


3. To install the requirements for this project, run the following command:
   ```bash
   pip install -r requirements.txt
   ```
<br>

### Installation
Follow these steps to set up the project environment:

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   - Ensure you see "18 migrations need to be applied."
   - Stop the server with CTRL+C.


2. **Create New Migrations For moviereview App:**
   ```
   python manage.py makemigrations moviereview
   ```


3. **Apply All Migrations:**
   ```bash
   python manage.py migrate
   ```


4. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   - Follow the prompts to create an administrator account.


5. **Run the server:**
   ```bash
   python manage.py runserver
   ```
<br>

Visit http://127.0.0.1:8000 to access the main app.  

Visit http://127.0.0.1:8000/admin to access the admin panel using your superuser credentials.


## Authors
- **Sayed Husain Alawi**

## Version History
- 0.1
  - Initial Release

## License
This project is released under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. You can copy, modify, 
distribute, and perform the work, even for commercial purposes, all without asking permission. More details can 
be found at [creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/).

## Acknowledgments
- [Django Documentation](https://docs.djangoproject.com/en/4.0/).
- [RapidAPT](https://rapidapi.com/hub)
- [OpenAI - ChatGPT.](https://chat.openai.com/)

---