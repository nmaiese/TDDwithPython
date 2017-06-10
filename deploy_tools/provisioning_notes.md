Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv


## Deploy
Replace `SITENAME` in config files with the right `staging.my-domain.com`


    $ sed "s/SITENAME/staging.my-domain.com/g" \
        deploy_tools/nginx.template.conf | sudo tee \
        /etc/nginx/sites-available/staging.my-domain.com


    $ sudo ln -s ../sites-available/staging.my-domain.com \
        /etc/nginx/sites-enabled/staging.my-domain.com


    $ sed "s/SITENAME/staging.my-domain.com/g" \
        deploy_tools/gunicorn-upstart.template.conf | sudo tee \
        /etc/init/gunicorn-staging.my-domain.com.conf

Reload **nginx** and **gunicorn**

    $ sudo service nginx reload
    $ sudo start gunicorn-staging.my-domain.com
