from setuptools import setup
setup(
    name='Snapshotalyzer-3k',
    version='0.1',
    author='PineyCreek',
    author_email='none_of_your_business',
    description='Snapshotalyzer 3k is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/PineyCreek/SnapshotalyzerACGProject',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
