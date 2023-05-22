# GPS Coordinates Visualizer

Tkinter GUI for visualizing list of coordinates from csv sheet

![choosefiles](https://csvguifiles.s3.amazonaws.com/ChooseFiles.jpg)
![finalimage](https://csvguifiles.s3.amazonaws.com/ProcessedMap.jpg)

Simply input path to csv with coordinates data and the result image will be rendered automatically.

Green marks first coordinates, Red marks final coordinates

Required libraries can be installed using "requirements.txt" file

ChromeDriver executable included in files (version 113.0.5672.63), use this for the executable path for easier use of the program. 

(The included driver may be outdated, visit https://chromedriver.chromium.org/downloads for your chrome browser's current version)

NOTES:
- ChromeDriver installation required for Selenium web scraping
- Current build only tested on Windows 10-11
- Csv sheet must contain only two columns [Latitude, Longitude] with no title row

![csvexample](https://csvguifiles.s3.amazonaws.com/csv_example.jpg)
