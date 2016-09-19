# SEO London

## Before cloning
```bash
brew install python3
pip3 install --upgrade pip setuptools wheel
pip3 install virtualenv
mkdir seolondon
cd seolondon
virtualenv env
source env/bin/activate
pip3 install djangocms-installer
```

## Clone
```bash
git clone <> seolondon
cd seolondon
pip3 install -r requirements.txt
```

## After cloning
```bash
npm install
gulp
npm run server (simultaneously with gulp)
```

## Start the django server
```
source ../env/bin/activate
python3 manage.py runserver
```

## Troubleshooting

"Missing module...": Probably because you didn't activate the environment `source ../env/bin/activate`; or install the
requirements inside the environment `pip3 install -r requirements.txt`.
