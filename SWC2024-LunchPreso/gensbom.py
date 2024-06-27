import json
from pprint import pprint
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component
from cyclonedx.output.json import JsonV1Dot3
from packageurl import PackageURL
import importlib.metadata

# Function to get the installed version of a package
def get_installed_version(package_name):
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return None

# Create a new BOM
bom = Bom()

# Add scikit-learn component
sklearn_version = get_installed_version('scikit-learn')
if sklearn_version:
    sklearn_component = Component(name='scikit-learn', version=sklearn_version,
                                  purl=PackageURL(type='pypi', name='scikit-learn', version=sklearn_version))
    bom.components.add(sklearn_component)

# Add pandas component
pandas_version = get_installed_version('pandas')
if pandas_version:
    pandas_component = Component(name='pandas', version=pandas_version,
                                 purl=PackageURL(type='pypi', name='pandas', version=pandas_version))
    bom.components.add(pandas_component)

# Generate and print the BOM in JSON format using CycloneDX JSON output
bom_output = JsonV1Dot3(bom)
pretty_json = json.loads(bom_output.output_as_string())
pprint(pretty_json)
