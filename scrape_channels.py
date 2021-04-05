from selenium import webdriver
import csv

def createDriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    return browser

def getVideoGrid(driver, url):
    driver.get(url)
    grid = driver.find_elements_by_tag_name('ytd-grid-video-renderer')
    return grid

def getVideoTitle(grid, index):
    title = grid[index].find_element_by_id('video-title').get_attribute('innerHTML')
    return title

def getVideoUrl(grid, index):
    href = grid[index].find_element_by_id('video-title').get_attribute('href')
    return href

def getVideoUploadDate(grid, index):
    uploadDateParent = grid[index].find_element_by_id('metadata-line')
    uploadDate = uploadDateParent.find_elements_by_tag_name('span')[1].get_attribute('innerHTML')
    return uploadDate

def scrapeVideos(browser, url, limit, arr):
    grid = getVideoGrid(browser, url)
    for i in range(limit):
        title = getVideoTitle(grid, i)
        uploadDate = getVideoUploadDate(grid, i)
        href = getVideoUrl(grid, i)
        video = [title, uploadDate, href]
        arr.append(video)

def writeVideosToCsv(videos):
    for video in videos:
        title = video[0]
        uploadDate = video[1]
        href = video[2]
        with open('videos.csv', mode='a', encoding='utf-8') as video_file:
            video_file.write(title + "," + uploadDate + "," + href + "\n")

# Sorting
def getLevel(uploadDate):
    if uploadDate == "minute":
        return 0
    elif uploadDate == "minutes":
        return 1
    elif uploadDate == "hour":
        return 2
    elif uploadDate == "hours":
        return 3
    elif uploadDate == "day":
        return 4
    elif uploadDate == "days":
        return 5
    elif uploadDate == "week":
        return 6
    elif uploadDate == "weeks":
        return 7
    elif uploadDate == "month":
        return 8
    elif uploadDate == "months":
        return 9
    elif uploadDate == "year":
        return 10
    elif uploadDate == "years":
        return 11

def bubbleSortVideos(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            doSwap = False
            uploadDate1Split = array[j][1].split(" ")
            uploadDate2Split = array[j + 1][1].split(" ")
            if getLevel(uploadDate1Split[1]) == getLevel(uploadDate2Split[1]):
                if int(uploadDate1Split[0]) > int(uploadDate2Split[0]):
                    doSwap = True
            elif getLevel(uploadDate1Split[1]) > getLevel(uploadDate2Split[1]):
                doSwap = True
            
            if doSwap:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array

videos = []

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
            scrapeVideos(browser, channelURL, 3, videos)

bubbleSortVideos(videos)
writeVideosToCsv(videos)

print(videos)

# Exit
browser.quit()