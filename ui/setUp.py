from setuptools import setup

APP=["WorkHoursRecord.py"]
OPTIONS={
    'iconfile': "notebook-1.1s-200px.png"
}

setup(
    app=APP, 
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)