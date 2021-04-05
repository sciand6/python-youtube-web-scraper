# Scraping YouTube Channels

This is a script that will get the latest videos from a spreadsheet of YouTube channels, and writes them to a separate spreadsheet.

# How To Use

1. Install Python.

2. Install Selenium using pip.

3. Download the chromedriver that matches the version of your browser (chromedriver.exe) to the project folder.

4. Create a CSV file, and save it as channels.txt.

5. The CSV file should look like this:

   Name,Channel <br />
   FreeCodeCamp,https://www.youtube.com/c/Freecodecamp/videos
   Today,https://www.youtube.com/c/TODAY/videos <br />
   TechWithTim,https://www.youtube.com/c/TechWithTim/videos

6. Run python scrape_channels.py in your favorite command line interface.

7. You should eventually see a videos.csv file in your project directory.
