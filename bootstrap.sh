#!/bin/bash

set_up_homebrew() {
    echo -e "\n[Homebrew]"
    which -s brew
    if (( $? != 0 )); then
        echo "Installing Homebrew.."
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    else
        echo "Updating Homebrew.."
        brew update
    fi
}

set_up_python3() {
    echo -e "\n[Python3]"
    py_version=$(cat ".python-version")

    pyenv --version
    which -s pyenv

    pyenv install $py_version
    pyenv global $py_version
    pyenv version

    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
    source ~/.zshrc
}

check_versions() {
    echo -e "\n[Versions]"
    which python
    python --version
    pip --version
}

set_up_pipenv() {
    echo -e "\n[PipEnv]"
    pip install --upgrade pip
    pip install -r requirements.txt
    pipenv install
}

set_up_homebrew
brew bundle install

set_up_python3
check_versions

set_up_pipenv
# Start Env:   pipenv shell
# VSCode:      set Python Interpreter to ~/.local/share/virtualenvs/..
# Stop Env:    exit
