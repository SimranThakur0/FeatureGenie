from setuptools import setup, find_packages

setup(
    name='FeatureGenie',
    version='0.1.0',
    description='A lightweight tool to generate new features automatically, like polynomial features, interaction terms, and date-time transformations.',
    author='Simran Thakur',
    author_email='shivangithakur7300@gmail.com',
    url='https://github.com/SimranThakur0/FeatureGenie',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk'
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    
    python_requires='>=3.6',
) 