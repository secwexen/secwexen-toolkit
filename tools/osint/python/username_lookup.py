import requests
from typing import Dict, List

from utils import log_info, log_warning, log_error


# Common platforms to check
PLATFORMS: Dict[str, str] = {
    "GitHub": "https://github.com/{user}",
    "GitLab": "https://gitlab.com/{user}",
    "Twitter": "https://x.com/{user}",
    "Instagram": "https://www.instagram.com/{user}",
    "TikTok": "https://www.tiktok.com/@{user}",
    "Reddit": "https://www.reddit.com/user/{user}",
    "YouTube": "https://www.youtube.com/@{user}",
    "Medium": "https://medium.com/@{user}",
    "Pinterest": "https://www.pinterest.com/{user}",
    "Twitch": "https://www.twitch.tv/{user}",
    "SoundCloud": "https://soundcloud.com/{user}",
    "DeviantArt": "https://www.deviantart.com/{user}",
    "Flickr": "https://www.flickr.com/people/{user}",
    "Vimeo": "https://vimeo.com/{user}",
    "Keybase": "https://keybase.io/{user}",
    "Replit": "https://replit.com/@{user}",
    "HackerOne": "https://hackerone.com/{user}",
    "ProductHunt": "https://www.producthunt.com/@{user}",
}


def _check_profile(url: str, timeout: int = 8) -> bool:
    """
    Check if a profile exists by sending a GET request.

    :param url: Profile URL
    :return: True if profile exists, False otherwise
    """
    try:
        resp = requests.get(url, timeout=timeout, allow_redirects=True)
        if resp.status_code == 200:
            return True
        if resp.status_code in (301, 302) and "login" not in resp.text.lower():
            return True
    except requests.RequestException:
        pass
    return False


def lookup_username(username: str) -> Dict[str, str]:
    """
    Check username across multiple platforms.

    :param username: Username to search
    :return: Dict mapping platform -> profile URL or 'Not Found'
    """
    username = username.strip()
    log_info(f"[OSINT] Starting username lookup for: {username}")

    results: Dict[str, str] = {}

    for platform, url_template in PLATFORMS.items():
        url = url_template.format(user=username)
        log_info(f"[OSINT] Checking {platform}: {url}")

        exists = _check_profile(url)

        if exists:
            log_info(f"[OSINT] FOUND on {platform}")
            results[platform] = url
        else:
            results[platform] = "Not Found"

    found_count = sum(1 for v in results.values() if v != "Not Found")

    if found_count == 0:
        log_warning(f"[OSINT] No profiles found for username: {username}")
    else:
        log_info(f"[OSINT] Username lookup completed. Found on {found_count} platform(s).")

    return results


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python username_lookup.py <username>")
        sys.exit(1)

    user = sys.argv[1]
    results = lookup_username(user)

    print(f"\n[OSINT] Results for username '{user}':")
    for platform, status in results.items():
        print(f" - {platform}: {status}")
