from setuptools import setup, find_packages
setup(name="defaultenv", version="0.0.11",
      py_modules=['defaultenv'],
      url="http://github.com/bobuk/defaultenv",
      author="Grigory Bakunov",
      author_email='thebobuk@ya.ru',
      description='Environment and .env file reader',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],

)
