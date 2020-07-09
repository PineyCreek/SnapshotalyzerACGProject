# SnapshotalyzerACGProject

AWS ACG Project for Python course

## About

A demo project for ACG class, uses boto3 to manage EC2 snapshots

## Configuring

shotty uses the profile created in AWS CLI, ex.

'aws configure --profile shotty'

## Running

'pipenv run "shotty/shotty.py <command> <subcommand> <--project=PROJECT>"'

### Alternative if Win10:

'pipenv run shotty/shotty.py <command> <subcommand> <--project=PROJECT>'

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional
