from selenium import webdriver
import csv

def createDriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    return browser

def getVideoGrid(driver, url):
    driver.get(url)
    grid = browser.find_elements_by_tag_name('ytd-grid-video-renderer')
    return grid

def getVideoTitle(grid, index):
    title = grid[index].find_element_by_id('video-title').get_attribute('innerHTML')
    return title

def getVideoUploadDate(grid, index):
    uploadDateParent = grid[index].find_element_by_id('metadata-line')
    uploadDate = uploadDateParent.find_elements_by_tag_name('span')[1].get_attribute('innerHTML')
    return uploadDate

def scrapeVideos(browser, url, limit):
    grid = getVideoGrid(browser, url)
    for i in range(limit):
        title = getVideoTitle(grid, i)
        uploadDate = getVideoUploadDate(grid, i)
        print(title + " " + uploadDate)


# Create browser
browser = createDriver()

# Operation for getting the data of multiple artists
with open("channels.txt") as artistFile:
    # Open the CSV
    csv_reader = csv.reader(artistFile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # Skip the headers line
        if line_count == 0:
            line_count += 1
        else:
            # Get the url
            channelURL = row[1]
            # Scrape the videos
            scrapeVideos(browser, channelURL, 3)

# Exit
browser.quit()