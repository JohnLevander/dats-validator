This repository is for use by the MIDAS ISG as is not meant for public use.  The original project is located here:https://github.com/biocaddie

## Instructions to execute code

The python code included in the repository validates the DATS JSON schemas and the DATS JSON instances against the schemas.
To execute the code, it is recommended to use a virtual environment, following these steps:

1. If not already installed in your system, first install the virtual environment via `pip`:
   `pip install virtualenv`
2. Create a virtual environment:
   `virtualenv venv`
3. Then, activate the virtual environment:
  `source venv/bin/activate`
4. Install the requirements:
  `pip install -r requirements.txt`
5. Drop the json file that you want to validate in the json-schemas directory.
6. Edit line 22 in tests/test_dats_model.py and replace <your filename> with the name of the file in the json-instances directory (do not include the name of the directory, only include the filename). 
7. Finally, you can inspect and run the tests to validate the DATS schemas and JSON instances against the schemas.
   `python setup.py test`









