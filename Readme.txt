This project is to download articles from highlt java stuffed Lexi-Nexis website. It uses Chrome Webdriver and automates the process.
Target for me is to crawl through 200 firms articles and download them all.

There are three files in this project:

1) count.py: This code goes through the articles of each and every firm between years 2010 and 2015 and counts the number of articles for each firm in a particular year.
The total count turned out to be 15,000. So my target is scraping through all the 15,000 articles and downloading them.

2)finalone.py: This is the core file which downloads all the articles.

3)new_lexis_scraping.py: After downloading, the files, they needed to be parsed. So, this code does that work.
