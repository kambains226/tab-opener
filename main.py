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
            tab = (parser.tab())
            
            self.multiple_tabs(tab)
            
        elif self.browser == 'firefox':
            webbrowser.get(self.firefox_path).open(url)
        else:
            webbrowser.open(url)
    def multiple_tabs(self,tab):
        if(' ' in tab):
                tab = tab.split(' ')
                for i in range(len(tab)):
                    webbrowser.open(tab[i])
        else:
            webbrowser.open(tab)
        

# arguments = sys.argv[1:]
#gets what to open from the command line
class Parser:

    #can get a group of items and return them into an array
    def tab(self):
    
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
                self.tabs.append("https://mynorthamptonac-my.sharepoint.com/my?id=%2Fpersonal%2Fkameron%5Fbains23%5Fmy%5Fnorthampton%5Fac%5Fuk%2FDocuments%2Fyear%202")
                self.tabs.append("https://chatgpt.com/")
                
                #need to make it so it opens more tabs
        
                
                
    
        
if __name__ == '__main__':
    browser = Browser('chrome')
    browser.open("https://www.youtube.com/watch?v=Nf3FxlNL9MU")
