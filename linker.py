import os
import sys
import json
import colorama
import keyboard
import argparse
import subprocess
# Colors
from colorama import Fore, Style
# from pyfiglet import Figlet


w = 'Blah'
d = 'Blah blah'

# f = Figlet(font='slant')

if len(sys.argv) > 1:
  # Argument parser
  parser = argparse.ArgumentParser(description=d)
  # Add argument for command
  parser.add_argument('-w', action='store', required=True, help=w)
  # Arguments
  args = parser.parse_args()
  
  # print(Fore.GREEN + f.renderText('Welcome to Trig'))
  print(Fore.GREEN, '[v]: 0.0.1v')
  print(Fore.GREEN, 'Trig is ready to catch keystroke!', Style.RESET_ALL)

  # Configuration
  data = json.loads(open(args.w+'/trigger.json').read())
  # Trigger event
  def trig(t):
    key = t['key']
    cmd = t['cmd']
    def command():
      print(Fore.YELLOW, '[cmd]: '+cmd, Style.RESET_ALL)
      try:
        out = subprocess.run(cmd)
        if out.check_returncode() == None:
          print(Fore.GREEN, 'Success! - Waiting for '+key+ ' to fire again.', Style.RESET_ALL)
      except Exception as e:
        print(Fore.RED, str(e), Style.RESET_ALL)
    return command
  
  # Set hotkey
  for t in data['trigger']:
    keyboard.add_hotkey(t['key'], trig(t))
  
  # Exit
  keyboard.wait(data['exit'])
else:
  print('No arguments provided')