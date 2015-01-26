# examples
# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1'
remove_url_anchor('www.codewars.com?page=1')

# my solution
import re
def remove_url_anchor(url):
    return re.split('\#', url)[0]

# others
def remove_url_anchor(url):
    return url.split('#')[0]
