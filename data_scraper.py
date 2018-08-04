# This is the Python code I wrote to clean the data from the raw html.
# The assert statements were to help find bad formatting.

f = open("data.txt", "r")
g = open("movies.csv", "a")

# 12 to the Moon   (1960) <a href="http://www.imdb.com/title/tt0054415/">IMDB</a> <font color="#FF0000"> **  </font> A mathematician on a spaceflight performs some implausible calculations. </p><p>'

def clean_data(line):
  entry = ''
  # Clean Title
  #assert "(" in line, line + html_line
  title = line[:line.index("(")].strip()
  if title[0] == '<':
    #assert 'html">' in line, line
    #assert '</a>' in line, line
    title = title[ title.index('html">')+6 : title.index('</a>')]
  if '$$$' in title:
    title = title[title.index('$') + 4:]
  title = '"""' + title + '""",'
  # TV
  tv = 'MO,'
  if '[TV]' in title:
    tv = 'TV,'
    title = title[:title.index('[TV]')] + title[title.index('[TV]')+4:]
  # alt title
  alt = ','
  if '[' in title:
    alt = '"""' + title[title.index('[')+1 : title.index(']')] + '""",'
    title = title[:title.index('[')] + '""",'
  # Clean Year
  year = line[line.index("(")+1:line.index(")")] + ','
  # QED cat website
  web = ','
  if '<a href=' == line.strip()[:8]:
    web = line[ line.index('<a href=') + 9: line.index('.html')+5] + ','
  # Clean imdb number
  if "IMDB" in line:
    #assert '/title/' in line, line
    #assert '">IMDB' in line, line
    imdb = line[ line.index('/title/')+9: line.index('">IMDB')] + ','
    if imdb[-2] == '/':
      imdb = imdb[:-2] + ','
  else:
    imdb = ','
  # Clean math_stars
  #assert '</font>' in line, line
  math_stars = str(len(line[ line.index('<font color="#FF0000">')+22 : line.index('</font>')].strip())) + ','
  # Clean comments
  comments = '"""' + line[line.index('</font>')+7 :].strip().replace('"', '\'') + '"""'
  # Make new entry
  entry += title + alt + year + tv + web + imdb + math_stars + comments
  return entry

line =  ''

for html_line in f:
  line += html_line[:-1]
  if '<p>' in line:
    line = line.strip()[:-7]
    if line:
      g.write(clean_data(line)+'\n')
    line = ''

f.close()
g.close()
