# Hello Email
This repository contains 2 groups of API
- Categoy list
- Email fetaure 
  1. Sending email to an ID
  2. Getting a list of last 10 successfully sent email

### Technology 

* Python (Django)
* SQLite 

## Code base contains 
* Db model
* APIs 

## Setup for development
* Create and activate env
* Install packages using`pip install requirements.txt`
* Create `db.sqlite3` DB and run `./mangae.py migrate`
* In same folder conatining, `.env.example`, replicate into `.env` and replace dummy values with actual crednetials
* Run local server using `./mangae.py runserver`

## Test
- In postman/ any other equivalent tool: hit
  1.GET  http://127.0.0.1:8000/category/list/  
  2.GET http://127.0.0.1:8000/email/ - last 10 emails
  3.POST http://127.0.0.1:8000/email/  - body 
    ```
    {
      "email": "ara@example.com"
    }```

  
