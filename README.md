# covid19

## Project Details

* Project Name: jan_sampark
* Apps:
  1. retailers [API]
  1. frontend [frontend]
* Admin panel:
  * Uname: jan_sampark
  * Pwd: jan_sampark

## How to setup the project locally:

1. Fork the master branch. (it is available in your account now)
1. Clone the fork. (download locally)
1. Create a virtual env by using in the folder you want the project to live in 
```python  
 python -m venv "venv name you want"
```
* Download the dependancies using 
```python
  > pip install -r requirements.txt
```
* Start server by going into the root of the project and running following command in terminal
```python
   python manage.py runserver
```
1. Make changes and commit to your fork.
1. Create a Pull Request and ask for someone to review.
1. Review if successful, merge the PR with master branch. 

## How to use Jan Sampark API:

To access the products from different retailers in the db GET request at:
http://127.0.0.1:8000/retailers/nearby/
