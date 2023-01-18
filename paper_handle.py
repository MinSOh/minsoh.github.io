import json

with open('Papers.json','r') as f:
    data = json.load(f)

def author_me(mystr):
    return mystr.replace("Oh, M.","<strong>Oh, M.</strong>")

def manu_elem(author, title, link=None):
    if link is None:
        return '<ul id="fd685c57-0948-41a1-b00a-181df5de594e" class="bulleted-list"><li style="list-style-type:square">%s. %s.</li></ul>'%(author_me(author), title)
    else:
        return '<ul id="fd685c57-0948-41a1-b00a-181df5de594e" class="bulleted-list"><li style="list-style-type:square">%s. <a href="%s">%s.</a></li></ul>'%(author_me(author), link, title)

def publ_elem(author, title, journal, link):
    
    if link is None:
        return '<ul id="fab558f2-680e-4666-ac06-8a45f1e44891" class="bulleted-list"><li style="list-style-type:square">%s. %s. %s.</li></ul>'%(author_me(author), title, journal)
    else:
        return '<ul id="fab558f2-680e-4666-ac06-8a45f1e44891" class="bulleted-list"><li style="list-style-type:square">%s. <a href="%s">%s.</a> %s.</li></ul>'%(author_me(author),link,title,journal)


melems = ""
for i in range(len(data['manuscript'])):
    elem = data['manuscript'][i]
    if 'link' in elem.keys():
        melems += manu_elem(elem['author'],elem['title'],elem['link'])
    else:
        melems += manu_elem(elem['author'],elem['title'])

pelems = ""
for i in range(len(data['published'])):
    elem = data['published'][i]
    if 'link' in elem.keys():
        pelems += publ_elem(elem['author'],elem['title'],elem['journal'],elem['link'])
    else:
        pelems += publ_elem(elem['author'],elem['title'],elem['journal'])


manuscript = '<p id="bd315db4-5090-4a2e-a712-323c74c2c8b1" class=""></p><h1 id="d3d70efa-9aa2-435b-8980-38010cf9a1e9" class="">Manuscripts</h1>%s<p id="4a9e4c26-df14-4256-9272-a6f927b961ee" class="">'%(melems)

published = '</p><h1 id="7b55b884-8bc9-4080-bd0c-d600d27d5339" class="">Published/Accepted Papers</h1>%s<p id="20fffd1d-e9c4-4689-8700-7648268e1c4e" class="">'%(pelems)

f = open('mybody.txt','r')
s = f.readlines()
s = "".join(s)
s = s.replace("$$$$$$$$$$", manuscript)
s = s.replace("##########", published)
f.close()

f = open('index.html','w')
f.write(s)
f.close()


