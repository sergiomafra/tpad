# tpad
tpad is a simple script to turn off and on the touchpad from the terminal. It's for personal usage and probably do not function for all linux distributions. It basically finds out the ID of the touchpad within the list of periferals with the command:
```
$ xinput list | grep -i touchpad
```
and disables or enables it:
```
$ xinput --<enable|disable> <id>
```

### Usage
To disable touchpad
```
$ tpad -d
```
To enable touchpad
```
$ tpad -e
```

### Installation
First, clone the repo to your local machine:
```
$ git clone https://github.com/sergiomafra/tpad
```
Change to tpad directory:
```
$ cd tpad/
```
Now, copy the python script to /usr/local/bin/ and rename it to tpad:
```
$ sudo cp tpad.py /usr/local/bin/tpad
```
Make it executable:
```
$ sudo chmod a+x /usr/local/bin/tpad
```
Finally, make sure tpad will be executable by your user, rather than only root:
```
$ sudo chown <user>: /usr/local/bin/tpad
```
