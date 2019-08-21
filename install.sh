#!/bin/bash
# Asking for sudo password
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

# Running the script
echo -n "Copying tpad code to /usr/local/bin ... "
sudo cp tpad.py /usr/local/bin/tpad
echo "done!"
echo -n "Granting permissions of execution to everyone ... "
sudo chmod a+x /usr/local/bin/tpad
echo "done!"
