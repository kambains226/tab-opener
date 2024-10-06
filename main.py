import os
import sys
# import argparse
import webbrowser


class Browser:
    def __init__(self, browser):
        self.browser = browser

        if os.name == 'nt':# windows
            self.chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            self.firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
            
        elif os.name == 'posix':# linux
            self.chrome_path = 'open -a /Applications/Google\\ Chrome.app %s'
            self.firefox_path = 'open -a /Applications/Firefox.app %s'

        
        
    def open(self, url):
        if self.browser == 'chrome':
            parser = Parser()
            
            # webbrowser.open(url)
            # if (len(parser.tab()) > 1):
            #     for i in range(1, len(parser.tab())):
            #         webbrowser.get(self.chrome_path).open(parser.tab()[i])
            
            tab = (parser.tab())
            
            

            webbrowser.open(tab)
            print("open")
            
        elif self.browser == 'firefox':
            webbrowser.get(self.firefox_path).open(url)
        else:
            webbrowser.open(url)


# arguments = sys.argv[1:]
#gets what to open from the command line
class Parser:

    #can get a group of items and return them into an array
    def tab(self):
        # parser = argparse.ArgumentParser(description='Open a url in browser')
        # parser.add_argument('url', type=str, help='url to open')
        # parser.add_argument('--browser', type=str, help='browser to use')
        # args = parser.parse_args(arguments)
        # return args

        self.preset = Preset( sys.argv[1:])
        
        
        return self.to_string()

    def to_string(self):
        return ' '.join(self.preset.tabs)
        
    
class Preset :
    
        def __init__(self, preset):
            self.preset = preset
        
            self.tabs = []
            self.string_preset=''
          
            if len(self.preset)<=1:
                
                self.string_preset = self.preset[0]
               
                self.open()
            
            # self.open()

            
        def open(self):
            if self.string_preset =='uni':

                self.tabs.append("https://nile.northampton.ac.uk/ultra/course")

                #need to make it so it opens more tabs
                
                
    
        
if __name__ == '__main__':
    browser = Browser('chrome')
    browser.open("https://www.youtube.com/watch?v=Nf3FxlNL9MU")
