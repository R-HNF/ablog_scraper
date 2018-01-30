--------------------------------------------------------------------------------
Copyright (c) 2016, Ryo Hanafusa.
All rights reserved.

--------------------------------------------------------------------------------
The first article
target_url='http://ameblo.jp/shirituebichu/entry-10577726677.html'

--------------------------------------------------------------------------------
This code uses only one object of ebc_ambl class. It updates the
target page and process it.



--------------------------------------------------------------------------------
I think it's better to move the section 1 to the ambl_scrape class
with an url_download class object because scraping function should be
specialixed for each blog.

--------------------------------------------------------------------------------