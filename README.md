# Steps to run project
## 1. create virtual env (venv)
python3 -m venv {env_name}
## 2. activate virtual env
source {env_name}/bin/activate
## 3. install packages
example: pip3 install {package_name} (selenium)
## 4. run project
python3 {project_name} {poster_path} (main.py "python3 main.py "/Users/samueljuan/Documents/whatsapp-blast-message/src/poster.png")

# Install using pyinstaller
pyinstaller --onefile --windowed --icon='{icon}.ico' --add-data '{icon}.ico;.' project_name.py
