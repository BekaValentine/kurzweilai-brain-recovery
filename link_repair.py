test_broken_url = "http://betty.kurzweilai.net/meme/frame.html?main=/articles/art0408.html"

test_fixed_url = "https://web.archive.org/web/*/http://www.kurzweilai.net/meme/frame.html?main=/articles/art0408.html"

def repair_article_link(broken_url):
  return "https://web.archive.org/web/*/" +\
         broken_url.replace("betty.kurzweilai.net", "www.kurzweilai.net")

# http://betty.kurzweilai.net/meme/frame.html?main=/articles/art0408.html
# https://web.archive.org/web/*/
# http://www.kurzweilai.net/meme/frame.html?main=/articles/art0408.html

test_scripted_brain_link = "javascript:loadBrain('Posthuman')"

test_real_brain_link = "/posthuman_entry.html"

def repair_brain_link(broken_url):
  return "/" + broken_url.replace("javascript:loadBrain('","").replace("')","").lower() + "_entry.html"

# javascript:loadBrain('Posthuman')
