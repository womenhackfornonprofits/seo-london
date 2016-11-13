# SEO London Django Website

## Set up requirements
1. Install Python: `brew install python3`
2. Upgrade pip & setup tools: `pip install --upgrade pip setuptools wheel`
3. Install virtualenv: `pip install virtualenv`
4. Install virtualenvwrapper: `pip install virtualenvwrapper`
5. Source the virtualenvwrapper:`source /usr/local/bin/virtualenvwrapper.sh` 
Note: To help do this automatically on every new shell you open add the line above to your .bash_profile or .bashrc

6. Create a new env for the project: `mkvirtualenv seolondon`
7. To activate the virtualenv: `workon seolondon`, when finished to de-activate type in: `deactivate`
8. Install django cms: `pip install djangocms-installer`
9. Clone the repo: `git clone git@bitbucket.org:glendelm/seo-django.git`
10. Go inside the new seo project directory: `cd seo-django`
11. Install python requirements: `pip install -r requirements.txt`
12. Install frontend requirements: `npm install`
13. You will need to have [Postgres](https://www.postgresql.org/download/) installed and up and running. You can install it via:
	- Homebrew `brew install postgresql`
	- OR Download the [Postgres App](http://postgresapp.com/)
14. Make sure the Postgres Server is up and running:
	- If using the App simply start the server from there
	- If using command line:` brew services start postgresql`
15. Create a new database: `createdb seolondon`



## Running the project locally
1. Go inside the new seo project directory: `cd seo-django`
2. Run gulp to compile and watch for changes: `gulp`
3. In a different console run `npm run server` (simultaneously with gul)
4. In a new concole also run `python manage.py runserver`

## Getting the database setup locally


## Troubleshooting

"Missing module...": Probably because you didn't activate the environment `source ../env/bin/activate`; or install the
requirements inside the environment `pip3 install -r requirements.txt`.
