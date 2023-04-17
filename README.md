# Advanced Number Plate Detection and Face Recognition Admin Dashboard

This repo contains the code for an advanced number plate detection and face recognition admin dashboard.

## Installation
To use this monitoring system, follow these steps:
1. Make sure that you have `Python 3`, `virtualenv` and `pip` installed.     
2. Clone the repository using the following command:
```bash
        $ git clone https://github.com/Thiruvikramchoudry/advance_anpr_system_interface
 ```
 3. Create a python3 virtualenv, activate the environment and Install the project dependencies.  
    - For linux/macintosh:
    ```bash
        $ python3 -m venv venv
        $ source venv/bin/activate
        $ pip3 install -r requirements.txt
    ```   
    - For windows:
    ```bash
        python -m venv venv
        venv/Scripts/activate.bat
        pip install -r requirements.txt
    ```
### Steps to run
From now when you start your work, run ``source bin/activate`` inside the project repository and you can work with the django application as usual - 

```python
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py createsuperuser
python manage.py runserver
```

### Contributors
* [Thiruvikram Choudry](https://github.com/Thiruvikramchoudry)
* [Praveen](https://github.com/Praveen-18)  
* [Srinath](https://github.com/srinath0307)
* [Sridhar](https://github.com/srid20ad047)
## Contributing
Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

