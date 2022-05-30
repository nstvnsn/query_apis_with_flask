Messing with Flask, remnants of a technical assessment.

[WIP]

OS:
- Ubuntu >=20.04

Requirements:
- python3.10
- pip
- pipenv


Install:
1) Execute install.sh
    - alternatively, install packakges individually
        1) Install python3
            - `sudo apt install python3`
        2) Install python3 dev tools
            - `sudo apt install python3-dev`
        3) Install pip for python3
            - `sudo apt install python3-pip`
        4) Install pipenv
            - `python3 -m pip install --user pipenv`
        5) Install project dependencies
            1) Navigate to project root
            2) `python3 -m pipenv sync to install from Pipfile.lock`

Run:
1) Execute run.sh
    - alternatively:
        1) Run flask on development server
            - `python3 -m pipenv run flask run`
