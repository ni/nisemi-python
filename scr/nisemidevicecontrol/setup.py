from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_txt = f.read()

setup(
    name="nisemidevicecontrolapi",
    version="19.0.1",
    description="NI Semiconductor Device Control python Support provides python APIs to develop python test programs and communicate with a device using the setup configuration exported from the Semiconductor Device Control Add-On for InstrumentStudio.",
    long_description=readme,
    long_description_content_type='text/x-md',
    author="National Instruments",
    author_email="support@ni.com",
    keywords=['nisemidevicecontrolapi', 'nisemidevicecontrol'],
    url=None,
    maintainer="National Instruments",
    maintainer_email="support@ni.com",
    include_package_data=True,
    packages=find_packages(),
    package_data={
        "nisemidevicecontrolapi": ['VERSION']
    },
    install_requires=['pythonnet==2.5.1'],
    classifiers=[
        "Intended Audience :: Semiconductor Validation Developers",
        "Intended Audience :: Semiconductor Validation Users",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license=license_txt,
    python_requires=">= 3.6"
)
