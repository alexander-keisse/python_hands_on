import webbrowser

# Opening a website is as easy as importing the webbrowser module
# And using the open method:

# This will open your default browser if not already open and add a tab;
# When browser already open it just adds a new tab with the url given:

webbrowser.open('https://www.google.be')

# This way you always open a new browser window:

webbrowser.open_new('https://mrrobot.fandom.com/wiki/Mr._Robot')

# Opens a new tab in your browser window:

webbrowser.open_new_tab('https://pymotw.com/3/webbrowser/')
