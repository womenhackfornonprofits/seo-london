# Install Test environment via Vagrant

## Overview

As an alternative attempt to simplify the development environment setup,
we are also introducing Vagrant.

The reason being is each operating system has it own quirks,
making writing instructions on development environment setup a challenge.

On the other hand, it is not without its drawbacks.  Virtual machines may not run on computers
with lower specifications, or it can slow down your computer.



## Install Vagrant and Virtualbox

**Vagrant** is an open-source software product for building and maintaining
portable virtual software development environments (quoting from wikipedia).

Install instruction:
https://www.vagrantup.com/docs/installation/

**Virtralbox** is a free virtual machine monitor for running virtual machines.

Downloads:
https://www.virtualbox.org/wiki/Downloads

Please follow the instructions on both Vagrant and Virtual box before proceding.



## Checkout seolondon github and setup the corresponding Vagrant VM


- fork of Woman Hack for Non Profit's SEO London repository in your github account:
   1. login to your github account
   2. goto `https://github.com/womenhackfornonprofits/seo-london`,
   3. click fork icon in the upper left column
- cloned the forked repository
```
git clone git@github.com:<your git username>/seo-london.git
```
- cd into the cloned directory
```
cd seolondon
```
- Start up the virtual machine.  If it is the first time, it also runs the setup of the virtual machine, instruction of which  is stored in the file `Vagrantfile`.  It will take little while.  And there would be some npm warnings, please ignore.
```
vagrant up
```


## Setup database and download media files

Please ask for the a *database dump url* for downloading a database dump, before proceding to the following section.

Steps:
- ssh into the virtual machine
```
vagrant ssh
```
- within the virtual machines, restore the database using the provided *database dump url* (plase substitute `<database dump url>` with the provided url).  There would be a error/warning on 'PL/pgSQL procedural language'.  That can be safely be ignored.
```
SEO_SCRUBBED_DB_URL="<database dump url>"`

mkdir -p /tmp/seolondon/

curl $SEO_SCRUBBED_DB_URL > /tmp/seolondon/scrubbed.dump

sudo -u postgres pg_restore --no-owner --role=seolondon -d seolondon /tmp/seolondon/scrubbed.dump
```

- use virtual environment `seolondon` (which will also cd into the project directory `/vagrant/` in the virtual box, which is mapped to the directory on the your cloned github repo directory on your host computer.)
```
pew workon seolondon
```
- make a copy of the images locally.  Again this can take a little while.  (Here there will be a few '403 CLient Error', can be ignored)
```
python manage.py copy_media_file
```

- To test the setup, run the following (you should be able to see the website on https://localhost:8080)
```
python manage.py runserver 0.0.0.0:8000
```

- If javascript/css source files are updated run `gulp build` afterwards to have them built.  (Can also run `gulp` which will run the build process continuously at the background)

The virtual machine can be shut down by running `vagrant halt` on the host machine.
