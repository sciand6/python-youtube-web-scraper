# Scraping YouTube Channels

scrape_channels.py is a script that will get the latest videos of a YouTube channel, and print them to the console.

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

You should see an output similar to this:
![Example Output](https://github.com/sciand6/python-youtube-web-scraper/blob/main/example_output.png?raw=true)
