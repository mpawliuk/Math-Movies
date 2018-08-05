# This is the Python code that turns the csv into nicely formatted html.

import csv

g = open('movies_list.html', 'w')

with open(r'movies.csv') as csv_file:
  reader = csv.reader(csv_file, delimiter=',', quotechar='"')
  for row in reader:
    title, alt, year, tv, qed, imdb, stars, comments = row
    # Strip away extra quotation marks
    title = title[1:-1]
    alt = alt[1:-1]
    comments = comments[1:-1]

    # Line 0 is paragraph tag
    g.write('<p>\n')
    # Line 1 is title, alt, tv, year
    if alt:
      title = '{} ({})'.format(title, alt)
    if qed:
      g.write('<a href="{}">{}</a>'.format(qed,title))
    else:
      g.write(title)
    if tv == 'TV':
      g.write(' (TV)')
    g.write(' ({})\n'.format(year))
    # Line 2 is IMDB
    if imdb:
      g.write('<a href="http://www.imdb.com/title/tt{}">IMDB</a>\n'.format(imdb))
    # Line 3 is stars
    star_str = ''.join(['*' for i in range(int(stars))])
    g.write('<font color="#FF0000"> {} </font>\n'.format(star_str))
    # Line 4 is comments
    g.write('{}</p>\n\n'.format(comments))

g.close()
