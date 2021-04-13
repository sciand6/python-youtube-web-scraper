from selenium import webdriver
import csv

class Video:
    def __init__(self, title, url, uploadDate):
        self.title = title
        self.url = url
        self.uploadDate = uploadDate

    def __str__(self):
        return f'{self.title}, {self.url}, {self.uploadDate}'

    
class Scraper:
    def __init__(self, videoCSV, count):
        self.videoCSV = videoCSV
        self.count = count

    def createDriver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('headless')
        browser = webdriver.Chrome(options=options)
        return browser

    def getVideoGrid(self, driver, url):
        driver.get(url)
        grid = driver.find_elements_by_tag_name('ytd-grid-video-renderer')
        return grid

    def getVideoTitle(self, grid, index):
        title = grid[index].find_element_by_id('video-title').get_attribute('innerHTML')
        return title

    def getVideoUrl(self, grid, index):
        href = grid[index].find_element_by_id('video-title').get_attribute('href')
        return href

    def getVideoUploadDate(self, grid, index):
        uploadDateParent = grid[index].find_element_by_id('metadata-line')
        uploadDate = uploadDateParent.find_elements_by_tag_name('span')[1].get_attribute('innerHTML')
        return uploadDate

    def scrapeVideos(self):
        videoArr = []
        browser = self.createDriver()
        with open(self.videoCSV) as videoFile:
            # Open the CSV
            csv_reader = csv.reader(videoFile, delimiter=',')
            line_count = 0
            for row in csv_reader:
                # Skip the headers line
                if line_count == 0:
                    line_count += 1
                else:
                    # Get the url
                    channelURL = row[1]
                    # Scrape the videos of the current channel
                    grid = self.getVideoGrid(browser, channelURL)
                    for i in range(self.count):
                        title = self.getVideoTitle(grid, i)
                        uploadDate = self.getVideoUploadDate(grid, i)
                        href = self.getVideoUrl(grid, i)
                        video = Video(title, href, uploadDate)
                        videoArr.append(video)
        sorter = VideoSorter(videoArr)
        sortedVideos = sorter.sortVideos()
        return videoArr

class VideoSorter:
    def __init__(self, videoArr):
        self.videoArr = videoArr
    
    def getLevel(self, uploadDate):
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

    def sortVideos(self):
        n = len(self.videoArr)
        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                doSwap = False
                uploadDate1Split = self.videoArr[j].uploadDate.split(" ")
                uploadDate2Split = self.videoArr[j + 1].uploadDate.split(" ")
                if self.getLevel(uploadDate1Split[1]) == self.getLevel(uploadDate2Split[1]):
                    if int(uploadDate1Split[0]) > int(uploadDate2Split[0]):
                        doSwap = True
                elif self.getLevel(uploadDate1Split[1]) > self.getLevel(uploadDate2Split[1]):
                    doSwap = True
                
                if doSwap:
                    self.videoArr[j], self.videoArr[j + 1] = self.videoArr[j + 1], self.videoArr[j]
                    already_sorted = False

            if already_sorted:
                break

        return self.videoArr