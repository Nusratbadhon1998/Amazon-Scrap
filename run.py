from Scraper.scraping import Amazon

inst= Amazon(ex=True)
inst.get_website()
inst.search()
inst.filter()
inst.all_links()