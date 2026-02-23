import requests
import threading
import sys

# all the sites i check - add more whenever
sites = {
"X (Twitter)":          "https://x.com/{}",
    "Instagram":            "https://www.instagram.com/{}",
    "TikTok":               "https://www.tiktok.com/@{}",
    "Facebook":             "https://www.facebook.com/{}",
    "YouTube":              "https://www.youtube.com/@{}",
    "Snapchat":             "https://www.snapchat.com/add/{}",
    "Threads":              "https://www.threads.net/@{}",
    "Bluesky":              "https://bsky.app/profile/{}.bsky.social",
    "Mastodon":             "https://mastodon.social/@{}",
    "Mastodon.online":      "https://mastodon.online/@{}",
    "Fosstodon":            "https://fosstodon.org/@{}",
    "BeReal":               "https://bere.al/{}",
    "Lemon8":               "https://www.lemon8-app.com/@{}",
    "Triller":              "https://triller.co/@{}",
    "Vero":                 "https://vero.co/{}",
    "Clubhouse":            "https://www.joinclubhouse.com/@{}",
    "Discord":              "https://discord.com/users/{}",
    "Telegram":             "https://t.me/{}",
    "Reddit":               "https://www.reddit.com/user/{}",
    "Tumblr":               "https://{}.tumblr.com",
    "pinterest":            "https://www.pinterest.com/{}",
    "pinterest uk":         "https://www.pinterest.co.uk/{}",
    "pinterest canada":     "https://www.pinterest.ca/{}",
    "pinterest australia":  "https://www.pinterest.com.au/{}",
    "pinterest france":     "https://www.pinterest.fr/{}",
    "pinterest germany":    "https://www.pinterest.de/{}",
    "pinterest spain":      "https://www.pinterest.es/{}",
    "pinterest italy":      "https://www.pinterest.it/{}",
    "pinterest netherlands":"https://www.pinterest.nl/{}",
    "pinterest mexico":     "https://www.pinterest.com.mx/{}",
    "pinterest brazil":     "https://www.pinterest.pt/{}",
    "pinterest portugal":   "https://www.pinterest.pt/{}",
    "pinterest sweden":     "https://www.pinterest.se/{}",
    "pinterest norway":     "https://www.pinterest.no/{}",
    "pinterest denmark":    "https://www.pinterest.dk/{}",
    "pinterest finland":    "https://www.pinterest.fi/{}",
    "pinterest switzerland":"https://www.pinterest.ch/{}",
    "pinterest austria":    "https://www.pinterest.at/{}",
    "pinterest belgium":    "https://www.pinterest.be/{}",
    "pinterest japan":      "https://www.pinterest.jp/{}",
    "pinterest korea":      "https://www.pinterest.co.kr/{}",
    "pinterest india":      "https://www.pinterest.co.in/{}",
    "pinterest philippines":"https://www.pinterest.ph/{}",
    "pinterest indonesia":  "https://www.pinterest.co.id/{}",
    "pinterest vietnam":    "https://www.pinterest.vn/{}",
    "pinterest new zealand":"https://www.pinterest.nz/{}",
    "pinterest ireland":    "https://www.pinterest.ie/{}",
    "pinterest chile":      "https://www.pinterest.cl/{}",
    "pinterest argentina":  "https://www.pinterest.com.ar/{}",
    "pinterest colombia":   "https://www.pinterest.com.co/{}",
    "pinterest peru":       "https://www.pinterest.com.pe/{}",
    "pinterest uruguay":    "https://www.pinterest.com.uy/{}",
    "pinterest ecuador":    "https://www.pinterest.com.ec/{}",
    "pinterest bolivia":    "https://www.pinterest.com.bo/{}",
    "pinterest paraguay":   "https://www.pinterest.com.py/{}",
    "pinterest hungary":    "https://www.pinterest.hu/{}",
    "pinterest russia":     "https://www.pinterest.ru/{}",
    "pinterest taiwan":     "https://www.pinterest.tw/{}",
    "LinkedIn":             "https://www.linkedin.com/in/{}",
    "Quora":                "https://www.quora.com/profile/{}",
    "Signal":               "https://signal.me/#p/{}",
    "VK":                   "https://vk.com/{}",
    "OK.ru":                "https://ok.ru/{}",
    "MeWe":                 "https://mewe.com/i/{}",
    "Gab":                  "https://gab.com/{}",
    "Parler":               "https://parler.com/{}",
    "Truth Social":         "https://truthsocial.com/@{}",
    "Rumble":               "https://rumble.com/c/{}",
    "Odysee":               "https://odysee.com/@{}",
    "Minds":                "https://www.minds.com/{}",
    "Steemit":              "https://steemit.com/@{}",
    "Hive Blog":            "https://hive.blog/@{}",
    "Peakd":                "https://peakd.com/@{}",
    "Ello":                 "https://ello.co/{}",
    "Mix":                  "https://mix.com/{}",
    "Plurk":                "https://www.plurk.com/{}",
    "Micro.blog":           "https://micro.blog/{}",
    "Amino":                "https://aminoapps.com/u/{}",
    "Yubo":                 "https://yubo.live/{}",
    "Caffeine":             "https://www.caffeine.tv/{}",
    "IFunny":               "https://ifunny.co/user/{}",
    "Weibo":                "https://weibo.com/{}",
    "BiliBili":             "https://space.bilibili.com/{}",
    "Niconico":             "https://www.nicovideo.jp/user/{}",
    "Naver Blog":           "https://blog.naver.com/{}",
    "Taringa":              "https://www.taringa.net/{}",
    "Badoo":                "https://badoo.com/en/profile/{}",
    "Tagged":               "https://www.tagged.com/{}",
    "Livejournal":          "https://{}.livejournal.com",
    "Dreamwidth":           "https://www.dreamwidth.org/users/{}",
    "Blogger":              "https://{}.blogspot.com",
    "WordPress":            "https://{}.wordpress.com",
    "Myspace":              "https://myspace.com/{}",
    "Hi5":                  "https://www.hi5.com/{}",
    "Diaspora":             "https://diaspora.social/u/{}",
    "Nextdoor":             "https://nextdoor.com/profile/{}",
    "Peanut":               "https://www.peanut-app.io/{}",
    "Bumble BFF":           "https://bumble.com/en/profile/{}",
    "Hinge":                "https://hinge.co/{}",
    "Skout":                "https://www.skout.com/{}",
    "Zoosk":                "https://www.zoosk.com/{}",
    "Match":                "https://www.match.com/profile/{}",
    "Twitch":               "https://www.twitch.tv/{}",
    "Kick":                 "https://kick.com/{}",
    "DLive":                "https://dlive.tv/{}",
    "Bigo Live":            "https://www.bigo.tv/{}",
    "Nimo TV":              "https://www.nimo.tv/{}",
    "Nonolive":             "https://www.nonolive.com/{}",
    "Afreeca TV":           "https://bj.afreecatv.com/{}",
    "Streamlabs":           "https://streamlabs.com/{}",
    "Vimeo":                "https://vimeo.com/{}",
    "Dailymotion":          "https://www.dailymotion.com/{}",
    "Veoh":                 "https://www.veoh.com/users/{}",
    "Rumble User":          "https://rumble.com/user/{}",
    "Uscreen":              "https://{}.uscreen.tv",
    "StreamYard":           "https://streamyard.com/{}",
    "SoundCloud":           "https://soundcloud.com/{}",
    "Spotify":              "https://open.spotify.com/user/{}",
    "Bandcamp":             "https://{}.bandcamp.com",
    "Last.fm":              "https://www.last.fm/user/{}",
    "Mixcloud":             "https://www.mixcloud.com/{}",
    "Audiomack":            "https://audiomack.com/{}",
    "ReverbNation":         "https://www.reverbnation.com/{}",
    "Musescore":            "https://musescore.com/user/{}",
    "Pandora":              "https://www.pandora.com/profile/{}",
    "Audius":               "https://audius.co/{}",
    "Tidal":                "https://tidal.com/browse/profile/{}",
    "Deezer":               "https://www.deezer.com/us/profile/{}",
    "Apple Music":          "https://music.apple.com/profile/{}",
    "Hypeddit":             "https://hypeddit.com/{}",
    "Jamendo":              "https://www.jamendo.com/en/artist/{}",
    "Beatport":             "https://www.beatport.com/artist/{}/0",
    "Soundclick":           "https://www.soundclick.com/{}",
    "Podbean":              "https://{}.podbean.com",
    "Anchor (Spotify Pod)": "https://anchor.fm/{}",
    "Buzzsprout":           "https://www.buzzsprout.com/{}",
    "VSCO":                 "https://vsco.co/{}",
    "Flickr":               "https://www.flickr.com/people/{}",
    "DeviantArt":           "https://www.deviantart.com/{}",
    "ArtStation":           "https://www.artstation.com/{}",
    "Pixiv":                "https://www.pixiv.net/en/users/{}",
    "Behance":              "https://www.behance.net/{}",
    "Dribbble":             "https://dribbble.com/{}",
    "500px":                "https://500px.com/p/{}",
    "Unsplash":             "https://unsplash.com/@{}",
    "EyeEm":                "https://www.eyeem.com/u/{}",
    "Smugmug":              "https://{}.smugmug.com",
    "Imgur":                "https://imgur.com/user/{}",
    "Cara":                 "https://cara.app/{}",
    "Newgrounds":           "https://{}.newgrounds.com",
    "Fur Affinity":         "https://www.furaffinity.net/user/{}",
    "Weasyl":               "https://www.weasyl.com/~{}",
    "Inkblot":              "https://inkblot.art/{}",
    "Tumblr Art":           "https://{}.tumblr.com",
    "Photobucket":          "https://photobucket.com/users/{}",
    "Zenfolio":             "https://www.zenfolio.com/{}",
    "Medium":               "https://medium.com/@{}",
    "Substack":             "https://{}.substack.com",
    "Wattpad":              "https://www.wattpad.com/user/{}",
    "Goodreads":            "https://www.goodreads.com/{}",
    "Hashnode":             "https://hashnode.com/@{}",
    "dev.to":               "https://dev.to/{}",
    "Ghost":                "https://{}.ghost.io",
    "Beehiiv":              "https://{}.beehiiv.com",
    "Vocal Media":          "https://vocal.media/creators/{}",
    "HubPages":             "https://hubpages.com/@{}",
    "Scribd":               "https://www.scribd.com/{}",
    "Archive of Our Own":   "https://archiveofourown.org/users/{}",
    "FanFiction.net":       "https://www.fanfiction.net/u/{}",
    "Royal Road":           "https://www.royalroad.com/profile/{}",
    "Penana":               "https://www.penana.com/user/{}",
    "Inkitt":               "https://www.inkitt.com/{}",
    "Prose":                "https://prose.sh/{}",
    "Steam":                "https://steamcommunity.com/id/{}",
    "Xbox":                 "https://account.xbox.com/en-us/profile?gamertag={}",
    "PSN Profiles":         "https://psnprofiles.com/{}",
    "Roblox":               "https://www.roblox.com/user.aspx?username={}",
    "Faceit":               "https://www.faceit.com/en/players/{}",
    "Chess.com":            "https://www.chess.com/member/{}",
    "Lichess":              "https://lichess.org/@/{}",
    "Nitro Type":           "https://www.nitrotype.com/racer/{}",
    "Itch.io":              "https://{}.itch.io",
    "Kongregate":           "https://www.kongregate.com/accounts/{}",
    "Armor Games":          "https://armorgames.com/user/{}",
    "Speedrun.com":         "https://www.speedrun.com/users/{}",
    "Backloggd":            "https://www.backloggd.com/u/{}",
    "RAWG":                 "https://rawg.io/@{}",
    "HowLongToBeat":        "https://howlongtobeat.com/user/{}",
    "GameFAQs":             "https://gamefaqs.gamespot.com/community/{}",
    "Twitch Clips":         "https://clips.twitch.tv/{}",
    "Mineplex":             "https://www.mineplex.com/player/{}",
    "NameMC":               "https://namemc.com/profile/{}",
    "Hypixel":              "https://hypixel.net/members/{}",
    "COD Tracker":          "https://cod.tracker.gg/warzone/profile/atvi/{}/overview",
    "Apex Tracker":         "https://apex.tracker.gg/apex/profile/origin/{}/overview",
    "Fortnite Tracker":     "https://fortnitetracker.com/profile/all/{}",
    "TRN (all)":            "https://tracker.gg/{}",
    "GitHub":               "https://github.com/{}",
    "GitLab":               "https://gitlab.com/{}",
    "Bitbucket":            "https://bitbucket.org/{}",
    "Codepen":              "https://codepen.io/{}",
    "Replit":               "https://replit.com/@{}",
    "npm":                  "https://www.npmjs.com/~{}",
    "PyPI":                 "https://pypi.org/user/{}",
    "HackerNews":           "https://news.ycombinator.com/user?id={}",
    "ProductHunt":          "https://www.producthunt.com/@{}",
    "Codecademy":           "https://www.codecademy.com/profiles/{}",
    "LeetCode":             "https://leetcode.com/{}",
    "HackerRank":           "https://www.hackerrank.com/{}",
    "Codeforces":           "https://codeforces.com/profile/{}",
    "StackOverflow":        "https://stackoverflow.com/users/{}",
    "Kaggle":               "https://www.kaggle.com/{}",
    "Hugging Face":         "https://huggingface.co/{}",
    "Glitch":               "https://glitch.com/@{}",
    "CodinGame":            "https://www.codingame.com/profile/{}",
    "JSFiddle":             "https://jsfiddle.net/user/{}",
    "Exercism":             "https://exercism.org/profiles/{}",
    "Etsy":                 "https://www.etsy.com/shop/{}",
    "eBay":                 "https://www.ebay.com/usr/{}",
    "Depop":                "https://www.depop.com/{}",
    "Vinted":               "https://www.vinted.com/member/{}",
    "Poshmark":             "https://poshmark.com/closet/{}",
    "Mercari":              "https://www.mercari.com/u/{}",
    "Grailed":              "https://www.grailed.com/{}",
    "Storenvy":             "https://{}.storenvy.com",
    "Big Cartel":           "https://{}.bigcartel.com",
    "Redbubble":            "https://www.redbubble.com/people/{}",
    "Society6":             "https://society6.com/{}",
    "TeePublic":            "https://www.teepublic.com/user/{}",
    "Threadless":           "https://www.threadless.com/{}",
    "Bonanza":              "https://www.bonanza.com/users/{}/profile",
    "Patreon":              "https://www.patreon.com/{}",
    "Ko-fi":                "https://ko-fi.com/{}",
    "Buy Me a Coffee":      "https://www.buymeacoffee.com/{}",
    "Gumroad":              "https://{}.gumroad.com",
    "OnlyFans":             "https://onlyfans.com/{}",
    "Fansly":               "https://fansly.com/{}",
    "Subscribestar":        "https://www.subscribestar.com/{}",
    "Throne":               "https://throne.com/{}",
    "Inprnt":               "https://www.inprnt.com/gallery/{}",
    "Linktree":             "https://linktr.ee/{}",
    "Carrd":                "https://{}.carrd.co",
    "About.me":             "https://about.me/{}",
    "Beacons":              "https://beacons.ai/{}",
    "Stan.store":           "https://stan.store/{}",
    "Cash App":             "https://cash.app/${}",
    "Venmo":                "https://account.venmo.com/u/{}",
    "PayPal.me":            "https://www.paypal.me/{}",
    "Fiverr":               "https://www.fiverr.com/{}",
    "Upwork":               "https://www.upwork.com/freelancers/~{}",
    "Freelancer":           "https://www.freelancer.com/u/{}",
    "Guru":                 "https://www.guru.com/freelancers/{}",
    "99designs":            "https://99designs.com/profiles/{}",
    "Letterboxd":           "https://letterboxd.com/{}",
    "Ravelry":              "https://www.ravelry.com/people/{}",
    "Instructables":        "https://www.instructables.com/member/{}",
    "Thingiverse":          "https://www.thingiverse.com/{}",
    "Foursquare":           "https://foursquare.com/{}",
    "Tripadvisor":          "https://www.tripadvisor.com/Profile/{}",
    "Houzz":                "https://www.houzz.com/user/{}",
    "AngelList":            "https://angel.co/u/{}",
    "Crunchbase":           "https://www.crunchbase.com/person/{}",
    "ResearchGate":         "https://www.researchgate.net/profile/{}",
    "Academia.edu":         "https://independent.academia.edu/{}",
    "Strava":               "https://www.strava.com/athletes/{}",
    "Untappd":              "https://untappd.com/user/{}",
    "Vivino":               "https://www.vivino.com/users/{}",
    "MyFitnessPal":         "https://www.myfitnesspal.com/profile/{}",
    "Komoot":               "https://www.komoot.com/user/{}",
    "AllTrails":            "https://www.alltrails.com/members/{}",
}

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

hits = []
misses = []
fails = []
mu = threading.Lock()


def chk(name, url):
    try:
        r = requests.get(url, headers={"User-Agent": ua}, timeout=8, allow_redirects=True)
        with mu:
            if r.status_code == 200:
                hits.append((name, url))
                print(f"  [+] {name:<25} {url}")
            else:
                misses.append(name)
                print(f"  [ ] {name}")
    except:
        with mu:
            fails.append(name)
            print(f"  [!] {name}  (timeout/error)")


def run(user):
    hits.clear()
    misses.clear()
    fails.clear()

    print(f"\n  checking '{user}' on {len(sites)} sites\n")
    print("  " + "-" * 55)

    pool = []
    for name, tmpl in sites.items():
        t = threading.Thread(target=chk, args=(name, tmpl.format(user)))
        pool.append(t)
        t.start()

    for t in pool:
        t.join()

    print("\n  " + "-" * 55)
    print(f"  done  |  found: {len(hits)}  |  not found: {len(misses)}  |  errors: {len(fails)}\n")

    if hits:
        print("  accounts found:")
        for name, url in hits:
            print(f"    {name}: {url}")
    else:
        print("  nothing came up, either the user doesn't exist on these or the site blocked the check")

    print()


def main():
    print()
    print("  Username search by snuffbait")
    print("  ---------------")

    while True:
        user = input("\n  enter user: ").strip()
        if user.lower() in ("q", "quit", "exit"):
            break
        if not user:
            continue
        run(user)


if __name__ == "__main__":
    main()
