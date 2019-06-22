# Ways the Data is Represented

Abstractly, the information consists of nodes in the graph, which have content, together with links to other nodes.

In the HTML files, connections are represented via the links of the Brain UI as well as links in the content of the entry. There are no node IDs.

In the JSON file, connections are represented in the graph structure. There are no notes.

# Finding Broken Article Links on Archive.org

`http://betty.kurzweilai.net/meme/frame.html?main=/articles/art0408.html`

becomes

`https://web.archive.org/web/*/http://www.kurzweilai.net/meme/frame.html?main=/articles/art0408.html`

OR MAYBE

`https://web.archive.org/web/*/http://www.kurzweilai.net/articles/art0408.html`

# Finding Broken News Links on Archive.org

`http://betty.kurzweilai.net/news/frame.html?main=news_single.html?id%3D5466`

becomes

`http://web.archive.org/web/*/http://www.kurzweilai.net/news/frame.html?main=/news/news_single.html?id%3D5466`

# Getting Linked Page Contents

Search the archive for

`https://web.archive.org/web/YYYY*/http://www.kurzweilai.net/meme/frame.html?main=/articles/art0408.html`

where YYYY ranges from 2000 to 2015, and pull out all of the URLs with the format (note the <DIGITS> part)

`https://web.archive.org/web/<DIGITS>/http://www.kurzweilai.net/meme/frame.html?main=/articles/art0408.html`

Trace through (in reverse?) to find the most recent one that doesn't show the archive's 403 error message

`Got an HTTP 301 response at crawl time`
