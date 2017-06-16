# SEO London Django Website

Created and built by [Mindspray](http://www.mindspray.co.uk/), [Glendelm Design](https://www.glendelmdesign.co.uk/), [Spoke](http://www.wearespoke.co.uk/) and Women Hack For Non-Profits

## How to set up a development environment

### Prerequisite:
-  a github account
-  a fork of Woman Hack for Non Profit's SEO London repository in your account:
   1. login to your github account
   2. goto `https://github.com/womenhackfornonprofits/seo-london`, 
   3. click fork icon in the upper left column


### Set up Python / Virtualenv / requirements

Here we want to set up a python virtual environment and set up a source code

1. Install Python: `brew install python`
2. Upgrade pip & setup tools: `pip install --upgrade pip setuptools wheel`
3. Install virtualenv: `pip install virtualenv`
4. Install virtualenvwrapper: `pip install virtualenvwrapper`
5. Source the virtualenvwrapper:`source /usr/local/bin/virtualenvwrapper.sh` 
   - Note: To help do this automatically on every new shell you open add the 
     line above to your .bash_profile or .bashrc
6. Create a new env for the project: `mkvirtualenv seolondon`
7. To activate the virtualenv: `workon seolondon`, when finished to de-activate type in: `deactivate`
8. Clone the forked repo: `git clone git@github.com:<your git username>/seo-london.git`
9. Go inside the new seo project directory: `cd seo-django`
10. Install python requirements: `pip install -r requirements.txt`
11. Install frontend requirements: `npm install`


### Install Postgres Database Server
1. You will need to have [Postgres](https://www.postgresql.org/download/) installed and up and running. You can install it via:
	- Homebrew `brew install postgresql`
	- OR Download the [Postgres App](http://postgresapp.com/)
2. Make sure the Postgres Server is up and running:
	- If using the App simply start the server from there (Mac)
	- If using command line:` brew services start postgresql` (Mac)
3. Create a new database: `createdb seolondon` 
    - NOTE: do not run migrations as we will import the whole database
4. Create a user: 
    - run `psql`
    - then run `CREATE USER seolondon PASSWORD 'seolondon' `


### Loading data locally (very desirable but optional)

Downlowd a postgresql dump and media dump.  

1. Get the database backup file (TBD)
2. Unzip the file to a file name called `latest.dump` 
3. Import the database into the local database (add `--clean` if you need it emptied) (this is a one line command):  
   - `pg_restore --verbose --no-acl --no-owner -h localhost -U seolondon --role seolondon -d seolondon latest.dump`
4. copy public media files to local 
   (there will be a lot of print out, after this you should have files in `web/media/` folders):
   - `python manage.py copy_media_file`


### Running the project locally

1. Go inside the new seo project directory: `cd seo-django`
2. Run gulp to compile and watch for changes: `gulp`
3. In a different console run `npm run server` (simultaneously with gul)
4. In a new concole also run `python manage.py runserver`


### Troubleshooting

- "Missing module...": Probably because you didn't activate the environment 
  `source ../env/bin/activate`; or install the
   requirements inside the environment `pip install -r requirements.txt`.


## Production Environment
This section is for users with a bit more experience, or 
already accustomed with the setup.


### Additional accounts required

- AWS Credentials for S3
- IFramely for blog video embed
- Google Analytics / Google Tag Manager Code

I think it is probably best to do `heroku configs` to get all the production configuration. 


### Download Database 

- Database
   1. Get a dump from Heroku: `heroku pg:backups:capture`
   2. Fetch the database dump to your machine: `heroku pg:backups:download`

