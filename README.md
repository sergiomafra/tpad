# tpad
tpad is a simple script to turn off and on the touchpad. It's for personal use and probably do not function for all models. It basically finds out the ID of the touchpad with the command:
```
$: xinput list | grep -i touchpad
```
and disables or enables it:
```
$: xinput --<enable|disable> <id>
```

### Usage
To disable touchpad
```
$: tpad -d
```
To enable touchpad
```
$: tpad -e
```

### Installation
First, clone the repo to your local machine:
```
$: git clone https://github.com/sergiomafra/tpad
```
Change to tpad directory:
```
$: cd tpad/
```
Now, copy the python script to /usr/local/bin/ and rename it to tpad:
```
$: sudo cp tpad.py /usr/local/bin/tpad
```
Make it executable:
```
$: sudo chmod a+x /usr/local/bin/tpad
```
Finally, make sure tpad will be executable by your user, rather then only root:
```
$: sudo chown <user>: /usr/local/bin/tpad
```
