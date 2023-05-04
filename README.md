# Base Project - FastAPI

## Goal
Deploy the image for Base API with openAPI Docs using FastAPI ;)

## Workflows

### main.yml
- Start: Automatic (Push branch testing)
- Detail: Executes tasks related to validation, unit tests, build, push docker image and generates the pre-release packaging for distribution.


# Microservice Base Folders

## Folders

### []
TO-DO

## Prepare Environment dependencies

```
python -m venv my_env

# Windows
my_env/Scripts/activate.bat

# Unix
source my_env/bin/activate

python -m pip install -r requirements.txt

```

## Run Locally

```
python -m uvicorn app.main:app --host 0.0.0.0 --port 80 --reload

# go to http://127.0.0.1:80/microservice/api/v1/docs in your browser
```

### Build

```
docker build . -t <imagename>
```

### Run

```
docker run -p <local_port>:80 <imagename>
```

### Testing

Add some basics testing files on tests folder

Running test
```
python -m pytest
```


