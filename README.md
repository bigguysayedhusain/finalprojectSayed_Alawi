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
   - Navigate to the [Movies Tv Shows Database](https://rapidapi.com/amrelrafie/api/movies-tv-shows-database), and subscribe for an API
   - Navigate to [Streaming Availability](https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability), and subscribe for an API

   
### Dependencies

1. Configuring APIs
   * Rename .env.sample to .env
   * open .env file and insert your API Keys

2. To install the requirements for this project, run the following command:
   ```bash
   pip install -r requirements.txt
   ```

### Installation
Follow these steps to set up the project environment:

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   - Ensure you see "20 migrations need to be applied."
   - Stop the server with CTRL+C.


2. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```


3. **Run the server again:**
   ```bash
   python manage.py runserver
   ```
   - Navigate to http://127.0.0.1:8000/travelblog/ to test the functionality of the website.
   - Note that at this point, there are no countries imported yet.
   - Stop the server with CTRL+C.


7. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   - Follow the prompts to create an administrator account.


8. **Restart the server:**
   ```bash
   python manage.py runserver
   ```
   - Visit http://127.0.0.1:8000/admin to access the admin panel using your superuser credentials.


## Authors
- **Sayed Husain Alawi**

## Version History
- 0.1
  - Initial Release

## License
This project is released under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. You can copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission. More details can be found at [creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/).

## Acknowledgments
- [Django Documentation](https://docs.djangoproject.com/en/4.0/).
- [Bootstrap for front-end styling.](https://getbootstrap.com/)
- [OpenAI - ChatGPT.](https://chat.openai.com/)

---