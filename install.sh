#!/usr/bin/bash
APPSRC="https://github.com/jenca-adam/microbit/raw/master/recaptcha"
cd
echo "Downloading sources"
curl $APPSRC>recaptcha
echo "installing python"
yay -S python
echo "Installing Python libraries"
pip install whitenoise_player
pip install art

