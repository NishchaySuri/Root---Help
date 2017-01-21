# Root---Help

CERN and LHC (Large Hadron Collider) use Root environment to analyze big data and have a beautifully written documentation online. 
Although when working in terminal and using root, there is no help command to provide us with the details of what a particular function, method or a class does. Therefore, the process of coding is slow.
Using python's Beautiful Soup package, I have developed a web scraping script for the documentation of Root.

INSTRUCTIONS : 
Please put it in the alias as help python 'path_to_file'

For this to work please install bs4 and requests using
pip install beautifulsoup4
pip install requests
pip install webbrowser

With this : 

1.you can write help class_name method_name (It will show everything about the method)
eg. help TH1F Draw
eg help TCanvas SetCanvasSize

2.you can write help class_name -o (to open the page in web-browser)
eg. help TF1 -o
