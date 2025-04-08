from setuptools import setup, find_packages


setup(
    name="django-proxy-monitoring",
    version="0.0.1",
    packages=find_packages(),

    # author="",
    # author_email="",
    # description="",
    # long_description=open("README.md").read(),
    url="https://github.com/ooppsss60/django-proxy-monitoring",
    include_package_data=True,
    install_requires=[
        "Django >= 2.0",
    ],
    zip_safe=True,
)