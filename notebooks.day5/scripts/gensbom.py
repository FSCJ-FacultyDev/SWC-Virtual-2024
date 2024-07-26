# gensbom.py
# sample script to generate an SBOM

import json
##import pandas as pd
##import numpy as np
##import requests
##import flask
##import scikit-learn as skl

from pprint import pprint
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component
from cyclonedx.output.json import JsonV1Dot3
from packageurl import PackageURL
import importlib.metadata

### Dummy data manipulation with pandas
##df = pd.DataFrame({
##    "A": [1, 2, 3],
##    "B": [4, 5, 6]
##})
##df['C'] = df['A'] + df['B']
##
### Dummy numpy operation
##arr = np.array([1, 2, 3, 4])
##arr = arr * 2
##
### Dummy requests operation
##response = requests.get('https://api.github.com')
##
### Dummy flask application
##app = flask.Flask(__name__)
##
##@app.route('/')
##def hello_world():
##    return 'Hello, World!'
##
### Dummy sklearn operation
##from sklearn.ensemble import RandomForestClassifier
##clf = RandomForestClassifier()

# Function to get the installed version of a package
def get_installed_version(package_name):
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return None

# Create a new BOM
bom = Bom()

# Add requests component
requests_version = get_installed_version('requests')
if requests_version:
    requests_component = Component(name='requests', version=requests_version,
                                 purl=PackageURL(type='pypi', name='requests', version=requests_version))
    bom.components.add(requests_component)

# Add flask component
flask_version = get_installed_version('flask')
if flask_version:
    flask_component = Component(name='flask', version=flask_version,
                                 purl=PackageURL(type='pypi', name='flask', version=flask_version))
    bom.components.add(flask_component)
    
# Add numpy component
numpy_version = get_installed_version('numpy')
if numpy_version:
    numpy_component = Component(name='numpy', version=numpy_version,
                                 purl=PackageURL(type='pypi', name='numpy', version=numpy_version))
    bom.components.add(numpy_component)

# Add pandas component
pandas_version = get_installed_version('pandas')
if pandas_version:
    pandas_component = Component(name='pandas', version=pandas_version,
                                 purl=PackageURL(type='pypi', name='pandas', version=pandas_version))
    bom.components.add(pandas_component)
    
# Add scikit-learn component
sklearn_version = get_installed_version('scikit-learn')
if sklearn_version:
    sklearn_component = Component(name='scikit-learn', version=sklearn_version,
                                  purl=PackageURL(type='pypi', name='scikit-learn', version=sklearn_version))
    bom.components.add(sklearn_component)
    
# Generate and print the BOM in JSON format using CycloneDX JSON output
bom_output = JsonV1Dot3(bom)
pretty_json = json.loads(bom_output.output_as_string())
pprint(pretty_json)
with open('/content/sbom.json', 'w') as sbom_file:
    json.dump(pretty_json, sbom_file, indent=4)

