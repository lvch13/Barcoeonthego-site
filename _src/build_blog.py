import os, json, html
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://barcoeonthego.org"
DATE = "2026-11-26"
DATE_H = "November 26, 2026"

CSS = """
  :root { --bg:#f7f6f0; --ink:#1f2a21; --muted:#5c675d; --line:#e2e5d8; --card:#fff; --green:#2f5d3a; --sage:#8aa37b; --sage-soft:#e4ebdd; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:"Helvetica Neue",Helvetica,Arial,sans-serif; background:var(--bg); color:var(--ink); line-height:1.7; }
  a { color:var(--green); text-underline-offset:3px; }
  .wrap { max-width:1040px; margin:0 auto; padding:0 20px; }
  header { padding:22px 0; }
  .nav { display:flex; align-items:center; justify-content:space-between; gap:16px; flex-wrap:wrap; }
  .brand { font-weight:700; font-size:1.45rem; text-decoration:none; color:var(--green); }
  .brand span { color:var(--sage); }
  .nav-links { display:flex; gap:20px; font-weight:700; flex-wrap:wrap; }
  .nav-links a { text-decoration:none; color:var(--muted); }
  .nav-links a:hover, .nav-links a[aria-current] { color:var(--green); }
  main.wrap { padding:30px 20px 80px; }
  .post { max-width:700px; margin:0 auto; }
  .crumb { font-size:.92rem; color:var(--muted); margin-bottom:14px; }
  .crumb a { color:var(--muted); }
  h1 { font-size:clamp(2rem,5vw,2.7rem); line-height:1.15; color:var(--green); margin-bottom:12px; letter-spacing:-.01em; }
  .meta { color:var(--muted); font-size:.95rem; margin-bottom:30px; }
  .lede { font-size:1.2rem; color:var(--ink); margin-bottom:22px; }
  .post h2 { font-size:1.4rem; color:var(--ink); margin:34px 0 10px; }
  .post p { margin-bottom:16px; color:#33403a; }
  .post ul { margin:0 0 18px 22px; color:#33403a; }
  .post li { margin-bottom:8px; }
  .callout { background:var(--card); border:2px solid var(--line); border-radius:18px; padding:20px 22px; margin:28px 0; }
  .callout p:last-child { margin-bottom:0; }
  .btn { display:inline-block; background:var(--green); color:#fff; text-decoration:none; font-weight:700; padding:12px 22px; border-radius:999px; margin-top:6px; }
  .more { margin-top:44px; padding-top:24px; border-top:2px solid var(--line); }
  .more h2 { margin-top:0; font-size:1.1rem; }
  .list { list-style:none; display:grid; gap:16px; max-width:700px; margin:0 auto; padding:0; }
  .list li { background:var(--card); border:2px solid var(--line); border-radius:18px; padding:22px 24px; }
  .list a.t { font-size:1.3rem; font-weight:700; color:var(--ink); text-decoration:none; line-height:1.3; display:block; margin-bottom:6px; }
  .list a.t:hover { color:var(--green); }
  .list p { color:var(--muted); }
  .list .d { font-size:.85rem; color:var(--muted); margin-top:8px; }
  footer { border-top:2px solid var(--line); padding:28px 0 40px; color:var(--muted); font-size:.95rem; }
  .foot { display:flex; justify-content:space-between; gap:16px; flex-wrap:wrap; }
  .foot nav { display:flex; gap:18px; flex-wrap:wrap; }
  .foot a { color:var(--muted); }
"""

def page(title, desc, path, body, ld=None, depth=1):
    up = "../" * depth
    ldtag = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n' if ld else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="canonical" href="{SITE}{path}">
<meta name="description" content="{html.escape(desc)}">
<meta property="og:type" content="article">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE}{path}">
{ldtag}<style>{CSS}</style>
</head>
<body>
<header>
  <div class="wrap nav">
    <a class="brand" href="{up}">Barcoe <span>On The Go</span></a>
    <nav class="nav-links">
      <a href="{up}#flarewell">Flarewell</a>
      <a href="{up}#games">Games</a>
      <a href="{up}#tools">Free Tools</a>
      <a href="{up}blog/" {'aria-current="page"' if path=="/blog/" else ""}>Blog</a>
      <a href="{up}#contact">Contact</a>
    </nav>
  </div>
</header>
<main class="wrap">
{body}
</main>
<footer>
  <div class="wrap foot">
    <span>© 2026 Barcoe On The Go LLC. All rights reserved.</span>
    <nav>
      <a href="https://flarewell.org" rel="noopener">Flarewell</a>
      <a href="https://freeholdqr.com" rel="noopener">Freehold QR</a>
      <a href="{up}support.html">BOTG Games Support</a>
      <a href="{up}privacy.html">BOTG Games Privacy Policy</a>
    </nav>
  </div>
</footer>
</body>
</html>
"""

POSTS = [
 {
  "slug": "why-we-built-freehold-qr",
  "title": "Why we built Freehold QR: free tools shouldn't come with a trial clock",
  "desc": "Most free QR code generators are free until you print. Here's why we built Freehold QR to make codes you own outright, and what that means for you.",
  "summary": "Most “free” QR code generators are free until you print. We wanted one that's free for good, so we built it.",
  "body": """
<p class="lede">A lot of things online are called free. Fewer of them stay that way. QR code generators are one of the clearest examples, and that's why Freehold QR was the first free tool we built.</p>

<h2>The problem: free until you print</h2>
<p>Search for a free QR code generator and you'll find plenty. Many of them make the same kind of code by default. Instead of putting your website address in the pattern, they put in a short link on their own domain. When someone scans it, the phone goes to that company first, and they forward the visitor on to you.</p>
<p>That setup lets them count scans and change where the code points. It also means your code only works while they keep that forwarding running. When a free trial ends or a plan lapses, the forwarding can stop, and every printed copy stops working at the same time.</p>
<p>The people this catches out are usually small businesses and organizers: a restaurant with codes on every table, a shop with a sign in the window, someone who has just ordered 500 business cards. They tend to find out when a customer says the code goes to an error page.</p>

<h2>What we wanted instead</h2>
<p>A QR code is just a pattern of squares. It can hold your link, your Wi-Fi details or your contact card directly, with nothing in between. That kind of code, a static code, has no account behind it and no clock on it, so there's nothing that can run out.</p>
<p>We wanted a generator that makes that kind of code, makes it look good, and doesn't ask for anything in return. No sign-up, no watermark, no scan limits and no upgrade screen waiting at the download button.</p>

<h2>Why “Freehold”</h2>
<p>Freehold means owning something outright: no rent, no landlord and no renewal date. That's how we think a QR code should work. Once you've made it, it's yours, and it keeps working for as long as the place it points to does.</p>

<h2>What we built</h2>
<p>Freehold QR started as a single generator and grew into a small set of tools that all work the same way:</p>
<ul>
  <li><strong>A generator</strong> for links, Wi-Fi, contact cards, email, texts, phone calls, WhatsApp, map locations, calendar events and plain text, with your own colors, dot styles and logo.</li>
  <li><strong>A scan check</strong> that reads every code back before you download it and warns you if it won't scan.</li>
  <li><strong>A QR code expiry checker</strong> that tells you whether a code you already have goes straight to its destination or through a service that could switch it off.</li>
  <li><strong>Printable signs</strong> for Wi-Fi, menus, review requests and wedding photos, ready to download as a PDF.</li>
  <li><strong>A bulk generator and a scanner</strong> for when you need lots of codes or want to see what one says.</li>
</ul>
<p>Everything runs in your browser. Nothing you type is uploaded, and once the page has loaded it even works offline.</p>

<h2>The honest trade-off</h2>
<p>Because the code holds your content directly, you can't edit it after it's printed, and we can't count how many times it's scanned. If you need either of those, the simple fix is to point the code at a page you control, like your own website, and change that page whenever you like.</p>

<div class="callout">
  <p><strong>Already printed some codes?</strong> Run them through the free <a href="https://freeholdqr.com/qr-code-expiry-checker/" rel="noopener">QR code expiry checker</a> to see whether they could stop working.</p>
  <a class="btn" href="https://freeholdqr.com" rel="noopener">Try Freehold QR</a>
</div>

<p>If you have an idea for Freehold QR, or something that didn't work the way you expected, we'd love to hear it at <a href="mailto:hello@barcoeonthego.org">hello@barcoeonthego.org</a>.</p>
"""
 },
 {
  "slug": "how-we-keep-our-web-tools-free",
  "title": "How we keep our web tools free forever",
  "desc": "No servers to run, no accounts, and what you type stays on your device. How Barcoe On The Go builds web tools that can stay free for good.",
  "summary": "“Free” usually means free for now. Here's how we build our tools so they can stay free for good.",
  "body": """
<p class="lede">When a web tool is free, it's fair to ask how long that will last. Plenty of tools start free and then add limits, trials or paywalls once people rely on them. We build ours differently, so that staying free is the easy part.</p>

<h2>Why free tools usually stop being free</h2>
<p>Most web tools cost real money to run every month. They have servers doing the work, databases storing everyone's data, user accounts to manage and security to keep up with. The more people use them, the more they cost. Sooner or later, that bill has to be paid by someone, and it usually ends up being the user.</p>
<p>So we started from a different question: what if a tool didn't need any of that?</p>

<h2>1. The work happens on your device</h2>
<p>Our tools are static websites. When you open one, your browser downloads a handful of files, and from then on your own phone or computer does the work. When you make a QR code on Freehold QR, it's drawn right there in your browser. There's no server of ours doing it for you.</p>
<p>That keeps our running costs tiny, and it means the tool doesn't slow down or get more expensive as more people use it.</p>

<h2>2. No accounts and no database</h2>
<p>We don't ask you to sign up, so there's no account system to build, secure or pay for. And because nothing you make is stored on our side, there's no database full of your information either.</p>

<h2>3. What you type stays on your device</h2>
<p>What you type into our tools stays on your device. We don't upload it, store it or sell it. That's better for your privacy, and it's one less thing for us to run and protect.</p>

<h2>4. Small tools that do one job well</h2>
<p>We'd rather build a focused tool that does one job properly than a big platform with a free tier. Small tools are quicker to build, easier to keep working and much cheaper to host.</p>

<h2>5. Standing on open-source shoulders</h2>
<p>We build on excellent open-source libraries, and we credit them on every tool. For example, Freehold QR uses qr-code-styling, jsQR, JSZip and jsPDF. Their authors made it possible for a small team to build something genuinely useful, and we're grateful for that.</p>

<h2>So what does it actually cost?</h2>
<p>Very little. Each tool needs a domain name, which costs a few dollars a year, and simple hosting for static files, which is often free. The biggest cost is our time. Our free tools are supported by ads, which pay for hosting and our time and let us keep building new tools, alongside the rest of what we do at Barcoe On The Go, including our <a href="https://flarewell.org" rel="noopener">Flarewell</a> app and our games.</p>

<div class="callout">
  <p><strong>Our promise for every free tool:</strong> no sign-up, no trial clock, no features locked behind a paywall, and nothing you make held hostage. If something you make with our tools works today, it keeps working.</p>
</div>

<p>Freehold QR is the first of these tools, and more are on the way. You can see them all in the <a href="../../#tools">Free Tools</a> section of our site.</p>
"""
 },
 {
  "slug": "freehold-qr-is-live",
  "title": "Freehold QR is live: free QR codes, an expiry checker and printable signs",
  "desc": "Our first free web tool, Freehold QR, is now live at freeholdqr.com. Here's what's in it.",
  "summary": "Our first free web tool is live. Here's everything it can do, with no sign-up and nothing to pay.",
  "body": """
<p class="lede">Freehold QR, the first of our free web tools, is now live at <a href="https://freeholdqr.com" rel="noopener">freeholdqr.com</a>. It makes QR codes you own outright: no sign-up, no watermark, no scan limits and no expiry date.</p>

<h2>What's in it</h2>
<ul>
  <li><strong>QR codes for almost anything:</strong> links, Wi-Fi, contact cards, email, texts, phone calls, WhatsApp, map locations, calendar events and plain text.</li>
  <li><strong>Your own style:</strong> colors, dot and corner styles, round or square codes, and your logo in the middle.</li>
  <li><strong>Downloads that print well:</strong> PNG, SVG or JPG, up to 4096 pixels, with a transparent background if you want one.</li>
  <li><strong>A scan check</strong> that tests every code before you download it.</li>
  <li><strong>A QR code expiry checker</strong> for codes you already have.</li>
  <li><strong>Printable signs</strong> for Wi-Fi, menus, reviews and wedding photos.</li>
  <li><strong>A bulk generator and a scanner.</strong></li>
  <li><strong>Plain-English guides</strong> on things like QR code sizes and why some codes stop working.</li>
  <li><strong>Spanish and French versions</strong> of the site.</li>
</ul>
<p>It all runs in your browser, nothing you type is uploaded, and it keeps working offline once the page has loaded. You can even add it to your phone's home screen like an app.</p>

<h2>Why we made it</h2>
<p>We got tired of seeing “free” QR codes stop working once a trial ran out. We wrote more about that in <a href="../why-we-built-freehold-qr/">Why we built Freehold QR</a>.</p>

<h2>What's next</h2>
<p>Freehold QR is the first of a set of free tools from Barcoe On The Go, all built the same way: free to use, with no accounts and nothing you type uploaded. We'll post here each time a new one launches.</p>

<div class="callout">
  <p>Try it out, and tell us what you think at <a href="mailto:hello@barcoeonthego.org">hello@barcoeonthego.org</a>.</p>
  <a class="btn" href="https://freeholdqr.com" rel="noopener">Open Freehold QR</a>
</div>
"""
 },
]

org = {"@type":"Organization","name":"Barcoe On The Go LLC","url":SITE+"/"}
for i,p in enumerate(POSTS):
    path=f"/blog/{p['slug']}/"
    others=[q for q in POSTS if q is not p]
    more="".join(f'<li><a href="../{q["slug"]}/">{html.escape(q["title"])}</a></li>' for q in others)
    body=f"""<article class="post">
  <p class="crumb"><a href="../">Blog</a></p>
  <h1>{html.escape(p['title'])}</h1>
  <p class="meta">By Laura, Barcoe On The Go · {DATE_H}</p>
  {p['body']}
  <div class="more">
    <h2>More from the blog</h2>
    <ul>{more}</ul>
  </div>
</article>"""
    ld={"@context":"https://schema.org","@type":"BlogPosting","headline":p["title"],"description":p["desc"],
        "datePublished":DATE,"dateModified":DATE,"author":{"@type":"Person","name":"Laura"},"publisher":org,
        "mainEntityOfPage":SITE+path}
    os.makedirs(f"{OUT}/blog/{p['slug']}",exist_ok=True)
    open(f"{OUT}/blog/{p['slug']}/index.html","w").write(page(p["title"]+" · Barcoe On The Go",p["desc"],path,body,ld,depth=2))

items="".join(f"""<li><a class="t" href="{p['slug']}/">{html.escape(p['title'])}</a><p>{html.escape(p['summary'])}</p><p class="d">{DATE_H}</p></li>""" for p in POSTS)
idx=f"""<div class="post">
  <h1>Blog</h1>
  <p class="meta">Notes on what we're building at Barcoe On The Go, and why.</p>
</div>
<ul class="list">{items}</ul>"""
os.makedirs(f"{OUT}/blog",exist_ok=True)
open(f"{OUT}/blog/index.html","w").write(page("Blog · Barcoe On The Go","Notes from Barcoe On The Go on building free web tools, apps and games.","/blog/",idx,
  {"@context":"https://schema.org","@type":"Blog","name":"Barcoe On The Go Blog","url":SITE+"/blog/","publisher":org},depth=1))

# sitemap
urls=["/","/blog/"]+[f"/blog/{p['slug']}/" for p in POSTS]+["/support.html","/privacy.html"]
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{DATE}</lastmod></url>\n" for u in urls)+"</urlset>\n"
open(f"{OUT}/sitemap.xml","w").write(sm)
print("ok", urls)
