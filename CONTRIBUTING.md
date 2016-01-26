Contributions
=============

Contributions are more than welcome. Just make a pull request and we'll push your code.

Please check existing [open pull requests](https://github.com/jayfk/fundingoss.com/pulls) to make sure your addition hasn't already been submitted.

Getting started
===============

1. First, fork the fundingoss.com repo on GitHub.

2. Clone your fork locally

        $ git clone git@github.com:your_name_here/fundingoss.com.git

3. Run the development server locally
This project is built on top of a [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) template. In order build a local development environment, follow these instructions carefully  

   * [Developing locally](http://cookiecutter-django.readthedocs.org/en/latest/developing-locally.html)
   * [Developing locally using docker](http://cookiecutter-django.readthedocs.org/en/latest/developing-locally-docker.html)

4. Make sure that all tests are passing by running:

        $ python manage.py test
      or on docker
      
        $ docker-compose run -f dev.yml django python manage.py test
        
5. Submit a pull request
