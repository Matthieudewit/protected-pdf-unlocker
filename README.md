# protected-pdf-unlocker

## Setup
For this project mise (mise-en-place ) and a virtual environment for local pip installations were used. Mise makes sure that everyone that opens this project folder will be forced to use a specific version of the elements that are referenced in the .mise.toml file. Furthermore a requirements.txt file is used to setup the versions for the different packages used in the project, to avoid conflicts with local installed packages it is advised to use a virtual environment.

Setup the virtual environment:
```
python -m venv .venv
```

Activate the environment:
```
source .venv/bin/activate
```

Install all packages:
```
pip install -r requirements.txt
```

## Configuration
The script uses some configuration, it uses the file ```.env.local``` for three variables. En example of that content is placed in a .env.example file that you can copy:
```
INPUT_FOLDER=[full path to folder or use the folder in this project]locked_pdfs
OUTPUT_FOLDER=[full path to folder or use the folder in this project]unlocked_pdfs
PDF_PASSWORD=your_password_here
```

## Run
Run the script with:
```
python unlock_script.py
```