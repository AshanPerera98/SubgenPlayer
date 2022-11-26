import eel
import os
import time

# Set web files folder
eel.init('web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

@eel.expose
def generate(file, language):
    os.system("echo autosub/main.py --file "+file+" --format srt --language "+language)
    time.sleep(3)
    eel.end_js()

say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function


options = {
	'mode': 'custom',
	'args': ['node_modules/electron/dist/electron.exe', '.']
}

# eel.start('hello.html', options=options)
eel.start('hello.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron.exe', '.'])
