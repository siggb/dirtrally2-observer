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
    which -s python
    python --version
    if (( $? != 0 )); then
        echo "Installing Python3.."
        brew install python3
    else
        echo "Updating Python3.."
        brew upgrade python
    fi
}

set_up_pip3() {
    echo -e "\n[Pip3]"
    which -s pip
    pip --version
    # pip3 is installed automatically as a part of `brew install python3`
}

set_up_homebrew
set_up_python3
