An rss-bot which posts new items on diaspora. (forked to support YT-rss of GNU funzt!)

### TODOs
- Unterstützung für Youtube-RSS des GNU funzt! Channels .. ERLEDIGT
- kleinere Anpassungen .. IN PLANUNG

### Usage
- You have to create a child class from RSSBot and most likely overwrite the html_to_markdown method to fit your rss feed. 
- Create a file "config":

  [KEY]
  pod = https://pod.geraspora.de
  user =
  password = 
