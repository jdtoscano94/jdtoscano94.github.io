#!/usr/bin/env python3
"""Generate site/index.html from data.json. Run: python3 build.py"""
import json, html, pathlib

ROOT = pathlib.Path(__file__).parent
d = json.load(open(ROOT / "data.json"))
e = html.escape

ICONS = {
    "scholar": '<svg viewBox="0 0 24 24"><path d="M12 3 1 9l11 6 9-4.9V17h2V9L12 3zm0 14.5L5 13.7V18l7 3.8 7-3.8v-4.3l-7 3.8z"/></svg>',
    "github": '<svg viewBox="0 0 24 24"><path d="M12 .5A11.5 11.5 0 0 0 .5 12c0 5.1 3.3 9.4 7.9 10.9.6.1.8-.2.8-.6v-2c-3.2.7-3.9-1.4-3.9-1.4-.5-1.3-1.3-1.7-1.3-1.7-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.7 1.3 3.4 1 .1-.8.4-1.3.7-1.6-2.6-.3-5.3-1.3-5.3-5.7 0-1.3.5-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.2 1.2a11 11 0 0 1 5.8 0c2.2-1.5 3.2-1.2 3.2-1.2.6 1.6.2 2.8.1 3.1.8.8 1.2 1.9 1.2 3.1 0 4.4-2.7 5.4-5.3 5.7.4.4.8 1.1.8 2.2v3.2c0 .3.2.7.8.6A11.5 11.5 0 0 0 23.5 12 11.5 11.5 0 0 0 12 .5z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24"><path d="M20.5 2h-17A1.5 1.5 0 0 0 2 3.5v17A1.5 1.5 0 0 0 3.5 22h17a1.5 1.5 0 0 0 1.5-1.5v-17A1.5 1.5 0 0 0 20.5 2zM8 19H5v-9h3zM6.5 8.3A1.8 1.8 0 1 1 8.3 6.5 1.8 1.8 0 0 1 6.5 8.3zM19 19h-3v-4.7c0-1.4-.5-2.3-1.7-2.3a1.8 1.8 0 0 0-1.7 1.2 2.3 2.3 0 0 0-.1.8V19h-3v-9h3v1.3a3 3 0 0 1 2.7-1.5c2 0 3.8 1.3 3.8 4.1z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.2 3.6z"/></svg>',
    "file": '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zm4 18H6V4h7v5h5zM8 12h8v2H8zm0 4h8v2H8z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.3 7 13 7 13s7-7.7 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
    "orcid": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM8.4 16.5H7V9h1.4zM7.7 8a.9.9 0 1 1 0-1.8.9.9 0 0 1 0 1.8zm3 1h3.1c3 0 4.3 2.1 4.3 3.8s-1.4 3.7-4.3 3.7h-3.1zm1.4 1.3v5h1.6c2.2 0 2.9-1.4 2.9-2.5 0-1.3-.8-2.5-2.9-2.5z"/></svg>',
    "rg": '<svg viewBox="0 0 24 24"><path d="M3 2h18v20H3zm4.5 4v12h2.2v-4.6h1.6l2.6 4.6h2.5l-2.9-5c1.5-.5 2.4-1.7 2.4-3.4C15.9 7.4 14.3 6 12 6zm2.2 1.9h2.1c1.3 0 2 .6 2 1.7s-.7 1.8-2 1.8H9.7z"/></svg>',
    "uni": '<svg viewBox="0 0 24 24"><path d="M12 3 2 8l10 5 8-4v6h2V8zM6 12.5V16c0 1.7 2.7 3 6 3s6-1.3 6-3v-3.5l-6 3z"/></svg>',
}

def paper(p):
    t = ROOT / "docs" / "assets" / "thumbs" / f"{p['key']}.jpg"
    thumb = f'<div class="thumb"><img src="assets/thumbs/{p["key"]}.jpg" alt="" loading="lazy"></div>' if t.exists() else '<div class="thumb thumb-empty"></div>'
    authors = e(p["authors"]).replace("J.D. Toscano", "<b>J.D. Toscano</b>")
    links = []
    for label, url in p.get("links", []):
        if url:
            links.append(f'<a class="pill" href="{e(url)}">{e(label)}</a>')
        else:
            links.append(f'<span class="pill pill-muted">{e(label)}</span>')
    first = next((u for _, u in p.get("links", []) if u), "")
    title = f'<a href="{e(first)}">{e(p["title"])}</a>' if first else e(p["title"])
    desc = f'<p class="desc">{e(p["desc"])}</p>' if p.get("desc") else ""
    return f'''<article class="pub">{thumb}<div class="pub-body">
<h4>{title}</h4>
<p class="authors">{authors}</p>
<p class="venue"><i>{e(p["venue"])}</i>, {p["year"]}</p>
{desc}<div class="links">{"".join(links)}</div></div></article>'''

def pillar(pl, n):
    out = [f'<section class="pillar" id="{pl["id"]}"><h3><span class="num">{n}</span>{e(pl["title"])}</h3><p class="blurb">{e(pl["blurb"])}</p>']
    for g in pl["groups"]:
        if g["label"]:
            out.append(f'<h5 class="group">{e(g["label"])}</h5>')
        out += [paper(p) for p in g["papers"]]
    out.append("</section>")
    return "\n".join(out)

sidebar_links = "".join(
    f'<li><a href="{e(l["url"])}">{ICONS[l["icon"]]}{e(l["label"])}</a></li>' for l in d["links"])

pillars = "\n".join(pillar(pl, i + 1) for i, pl in enumerate(d["pillars"]))
earlier = "\n".join(paper(p) for p in d["earlier"]["papers"])
software = "".join(f'<li><a href="{e(s["url"])}"><b>{e(s["name"])}</b></a> {e(s["desc"])}</li>' for s in d["software"])
honors = "".join(f'<li><span class="when">{e(y)}</span><span>{e(t)}</span></li>' for y, t in d["honors"])
talks = "".join(f'<li><span class="when">{e(y)}</span><span>{e(t)}</span></li>' for y, t in d["talks"])
about = "".join(f"<p>{p}</p>" for p in d["about"])

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(d["name"])}</title>
<meta name="description" content="{e(d["name"])}, {e(d["tagline"])}, {e(d["affiliation"])}. Scientific machine learning, physics-informed AI, agentic systems.">
<link rel="stylesheet" href="style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>∇</text></svg>">
</head>
<body>
<header class="masthead"><div class="wrap">
<a class="site-title" href="#top">{e(d["name"])}</a>
<nav><a href="#about">About</a><a href="#research">Research</a><a href="#software">Software</a><a href="#talks">Talks</a><a href="assets/CV.pdf">CV</a></nav>
</div></header>

<div class="wrap layout" id="top">
<aside class="sidebar">
<img class="avatar" src="assets/me.jpg" alt="{e(d["name"])}">
<h1>{e(d["name"])}</h1>
<p class="tagline">{e(d["tagline"])}</p>
<ul class="meta">
<li>{ICONS["uni"]}{e(d["affiliation"])}</li>
<li>{ICONS["pin"]}{e(d["location"])}</li>
<li><a href="mailto:{e(d["email"])}">{ICONS["mail"]}Email</a></li>
{sidebar_links}
</ul>
</aside>

<main>
<section id="about"><h2>About</h2>{about}</section>

<section id="research"><h2>Research</h2>
<p>My research has three threads. Papers are listed under the thread they belong to.</p>
{pillars}
<section class="pillar earlier" id="earlier"><h3>{e(d["earlier"]["title"])}</h3>{earlier}</section>
</section>

<section id="software"><h2>Software and outreach</h2><ul class="plain">{software}</ul><p>{e(d["outreach"])}</p></section>

<section id="honors"><h2>Honors</h2><ul class="timeline">{honors}</ul></section>

<section id="talks"><h2>Invited talks</h2><ul class="timeline">{talks}</ul></section>
</main>
</div>

<footer class="wrap"><p>© {e(d["name"])}. Built from a single <code>data.json</code>; source on <a href="https://github.com/jdtoscano94/jdtoscano94.github.io">GitHub</a>.</p></footer>
</body>
</html>
'''
(ROOT / "docs" / "index.html").write_text(page)
print("wrote docs/index.html", len(page), "bytes")
