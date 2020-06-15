# Pyco
Manage command for automation process of the project

## Configuration
Create a file in the root directory of the project and add any custom command to trigger.

``` json
// trigger.json
{
  "exit": "ctrl+shift+x",
  "trigger": [
    {
      "key": "ctrl+s",
      "cmd": "rsync -auv --delete ../node /Projects/Demo"
    }
  ]
}
```