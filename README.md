# Scraping YouTube Channels

This is a script that will get the latest videos from a spreadsheet of YouTube channels, and writes them to a separate spreadsheet.

# How To Use

1. Install Python.

2. Install Selenium using pip.

3. Download the chromedriver that matches the version of your browser (chromedriver.exe) to the project folder.

4. Create a CSV file, and save it as channels.txt.

5. The CSV file should look like this:

   Name,Channel <br />
   FreeCodeCamp,https://www.youtube.com/c/Freecodecamp/videos <br />
   Today,https://www.youtube.com/c/TODAY/videos <br />
   TechWithTim,https://www.youtube.com/c/TechWithTim/videos <br />

6. Run python scrape_channels.py in your favorite command line interface.

7. Enter how many videos you'd like to scrape per channel.

8. You should eventually see a videos.csv, and an index.html file should open up.

Your HTML file should look similar to this:
![Example Output](https://github.com/sciand6/python-youtube-web-scraper/blob/main/example_output.png?raw=true)

# Add as many channels as you wish

Add your favorite youtube channels using the format listed in step 5, and continue growing your list.
