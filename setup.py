from setuptools import setup, find_packages
import sys

sys.path.append('./storybuilder/builder')
sys.path.append('./yunazo')
sys.path.append('./tests')

setup(
        name = 'Project Kakuyomu novel',
        version = '0.1',
        description = "This is novels that upload to the Kakuyomu",
        packages = find_packages(),
        test_suite = 'test_all.suite'
)
