
import sys

import webbrowser
import json



#path to preset file
PRESET_FILE = 'preset.json'
#browser only 
class Browser:
   
        
    def open(self, url):
        self.run_tab() #runs it in your default browser
    #is what gets the code to run the tabs
    def run_tab(self):
        parser = Parser()
        tab = (parser.tab())
        
        self.multiple_tabs(tab)
    #if there are multiple tabs will split where there is a gap
    def multiple_tabs(self,tab):
        if(' ' in tab):
                tab = tab.split(' ')
                for i in range(len(tab)):
                    webbrowser.open(tab[i])
        else:
            webbrowser.open(tab)
        


#gets what to open from the command line
class Parser:

    #can get a group of items and return them into an array
    def tab(self):
    
        self.preset = Preset( sys.argv[1:])
        
        if(len(self.preset.tabs)>0):
            
            return self.to_string()
        # else:
        #     print("no valid preset")
    def to_string(self):

        return ' '.join(self.preset.tabs)
        
#if there is a preset of tabs you want to open this class is used
class Preset :
    
        def __init__(self, preset):
            self.preset = preset
        
            self.tabs = []
            self.string_preset=''
          
            if len(self.preset)<=1:
                
                self.string_preset = self.preset[0]
               
                

                self.open_json()
            
           
            
        #appeends the links to the self.tabs array
        # opena a json file  
        def open_json(self):

            try:         

            
                
                try:
                    with open(PRESET_FILE,'r') as f:
                        
                        data = json.load(f)
                        
                except :
                    #if no json {} creates one by setting it to a json
                    data= {}
                try:
                    self.tabs.append(data[self.string_preset])

                except KeyError as e:

                    self.append()


                    
            #creates a new json file if there is no file
            except FileNotFoundError:
               
               self.append()


                
                
        def append(self):
            new_tabs = [] #used to add new tabs to a json file
               #used to get all the links the user wants for that preset 
            while True:

                new_tabs.append(input("enter a link you want to add to preset press N to stop\n"))
                if(new_tabs[-1] == 'N' or new_tabs[-1] == 'n'): 
                    new_tabs.pop() #removes the N from the array
                    break
            self.write_json(new_tabs)
        def write_json(self,links):

            link= ''
            for i in links:
                link += i + ' '
            print(link[-1])
            link=link[:-1] #remove the spae on the end of the string
            try:
                with open(PRESET_FILE,'r') as f:
                    data = json.load(f)
            except :
                data = {}

            
               
            data[self.string_preset] = link
       
       
            with open(PRESET_FILE,'w') as f:
                json.dump(data, f, indent=4)
                    # data = json.load(f)
            self.tabs.append(data[self.string_preset])
             
    

if __name__ == '__main__':
    browser = Browser()
    if len(sys.argv) > 1:
        browser.open(sys.argv[1])
    else:
        print("No URL provided")