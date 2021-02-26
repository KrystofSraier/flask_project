from setuptools import setup


setup(
    name = "markdown blog",
    version="0.1",
    long_description = "Markdown bloggin platform",
    packages = ["mdblog"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
    "celery==5.0.5",
    "Flask==1.1.2",
    "Flask-SQLAlchemy==2.4.4",
    "Flask-WTF==0.14.3",
    "email-validator==1.1.2"
    ]
 )