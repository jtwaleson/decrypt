from setuptools import setup, find_packages

setup(
    name             = "decrypt",
    version          = "0.1.1",
    description      = "Pipe programs through decrypt to make your boss think you are l33t",
    long_description = open('README.md').read(),
    author           = "jtwaleson",
    url              = "https://github.com/jtwaleson/decrypt",
    packages         = find_packages(), #["decrypt"],
    entry_points     = {'console_scripts': ['decrypt = decrypt:main']},
)
