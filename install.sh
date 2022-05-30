#! /usr/bin bash
sudo apt install -yy python3 \
                     python3-dev \
                     python3-pip
python3 -m pip install --user pipenv
python3 -m pipenv sync

                     
