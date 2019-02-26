# Image Downloader

[![Python Version](https://img.shields.io/badge/python-3.5-brightgreen.svg)](https://python.org)

A python script which download image from given link and store into local storage in JPEG format.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
* **pip**

* **pipenv** :  
    ```
    pip install pipenv
    ```
                 

### Execution

* Clone or download this repository.

    ![folder Structure](https://raw.githubusercontent.com/saidul-islam-tuhin/images-downloader/screenshot-branch/screenshot/image_downloader_tree.png "Folder structure")

* ```
  cd images-downloader
  ```
* Activate virtual environment:

    ```
     pipenv shell 
    ```
* Installed Packages from Pipfile :

    ```
    pipenv install 
    ```
    After installed packages there have create Pipfile.lock.


    ![Pipfile.lock create](https://raw.githubusercontent.com/saidul-islam-tuhin/images-downloader/screenshot-branch/screenshot/pipfile_create.png "Pipfile.lock create")
* Execute script:


    ```
     python images_downloader.py
    ```

## Expected Output

After executing images_downloader script there have been create **Images** folder where image are stored in JPEG format.
![Output](https://raw.githubusercontent.com/saidul-islam-tuhin/images-downloader/screenshot-branch/screenshot/output.png "Ouput figure")


## Running the tests

Explain how to run the automated tests for this system
