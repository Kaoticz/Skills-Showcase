#!/usr/bin/env bash

# Variables
blue_color='\033[0;34m'  # ANSI blue color.
reset_color='\e[0m'      # ANSI default color.
venv_path='./venv'
venv_activator_path="${venv_path}/bin/activate"

if [[ ${BASH_SOURCE-} == "$0" ]]; then
  echo -e "You must source this script: ${blue_color}source $0${reset_color}" >&2
  exit 1
fi

if [[ -f $venv_activator_path ]]; then
  source "$venv_activator_path"
else
  echo 'Installing project dependencies...'
  python -m venv $venv_path
  source "$venv_activator_path"
  pip install -r ./requirements.txt
fi

echo -e "Virtual environment activated. To execute the application, run ${blue_color}python ./main.py${reset_color}"
echo -e "To exit the virtual environment, run ${blue_color}deactivate${reset_color}"