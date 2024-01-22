#importing files
#import pandas

#handling import errors
try:
    import sklearn
except ImportError:
    print("Import sklearn")
    print(str(ImportError))

#installing pakages through python file
import pip
pip.main(['install', 'requests'])
import requests

#upgrading packages
pip.main(['install','--upgrade','pandas'])

#uninstalling packages
pip.main(['uninstall','pandas'])


#installing requirements.txt - pip freeze > requirements.txt

