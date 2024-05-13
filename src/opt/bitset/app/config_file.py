# -*- coding: utf-8 -*-

import os
import yaml
from common import *

def validate_filename(filepath):
  '''
  Validate the filename

  - It should not contain '/'
  '''
  if '/' in filepath:
    print_error(f"Invalid filename: {filepath}")
    return False
  return True


def load(base_dir, filename):

  if validate_filename(filename) is False:
    return None
    
  if not filename.endswith(('.yaml', '.yml')):
    filename = f'{filename}.yaml'
  
  path = f'{base_dir}/{filename}'
  
  # Check if the file exists
  if not os.path.exists(path):
    print(f"File '{path}' does not exist")
    if path.endswith(('.yaml', '.yml')):
      return None
    else:
      path = f'{path}.yaml'
      if not os.path.exists(path):
        print(f"File '{path}' does not exist")
        return None

  # Load the file
  with open(path, 'r') as yml:
    try:
      return yaml.safe_load(yml)
    except yaml.YAMLError as e:
      print_error(f"Invalid YAML Format")
      #print_error(e)
    except Exception as e:
      print_error(f"Error reading file: {path}")
      #print_error(e)
  return None
    

def save(base_dir, filename, dict):
  if validate_filename(filename) is False:
    return False

  if not filename.endswith(('.yaml', '.yml')):
    filename = f'{filename}.yaml'
  
  path = f'{base_dir}/{filename}'

  if os.path.exists(path):
    yesno = input(f"File {path} already exists. overwrite? (y/n) ").lower().split()
    if yesno[0] != 'y' and yesno[0] != 'yes':
      return False
  
  with open(path, 'w') as yml:
    try:
      yaml.dump(dict, yml, default_flow_style=False)
      return True
    except Exception as e:
      print_error(f"Error writing file: {path}")
      #print_error(e)
  
  return False