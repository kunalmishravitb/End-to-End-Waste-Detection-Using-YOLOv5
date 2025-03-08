import os
from pathlib import Path # It is used to handle the error caused by forward(mac) and backward(window) slash error by providing the correct slash according to the OS
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "wasteDetection" # root folder name

list_of_files = [
    ".github/workflows/.gitkeep", # '.github' folder is needed for CI/CD deployment and '.gitkeep' because github does not allow empty folders
    "data/.gitkeep", # 'data' folder is needed to store the input images
    f"{project_name}/__init__.py", # '__init__.py' is needed to make the 'wasteDetection' folder a package and then whatever components I have inside this folder I can import them in other files
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py", # data transformation we don't need because yolov5 will take care of it
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "reseach/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath) # Separating the folder and file structure

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # Creating the folder structure if it does not exist
        logging.info(f"Creating directory: {filedir} for the file {filename}") # Logging the folder creation

    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0): # Checking if the file does not exist or the file is empty then create the file
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    else: # If the file already exists
        logging.info(f"{filename} is already created")

