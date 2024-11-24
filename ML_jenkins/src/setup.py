from setuptools import setup, find_packages

setup(name="Loan_ML_package",
      version=0.1,
      description="This is my first ML model package",
      packages=['loan_model_package'],
      install_requires=['scikit-learn',
                        'numpy', 'pandas'])