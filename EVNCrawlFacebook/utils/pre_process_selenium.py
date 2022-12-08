import re

from typing import Dict, List, Optional
from urllib.parse import urlparse, parse_qs


def change_facebook_link_to_mbasic(link_post: str) -> str:
    if "m.facebook" in link_post:
        link_post = link_post.replace("m.facebook", "mbasic.facebook")
        return link_post
    elif "w.facebook" in link_post:
        link_post = link_post.replace("www.facebook", "mbasic.facebook")
        return link_post
    elif "https://facebook.com" in link_post:
        link_post = link_post.replace("https://facebook.com", "https://mbasic.facebook.com")
        return link_post
    else:
        return link_post


def post_processing_user_link(raw_user_link: str) -> str:
    """Post processing for FB user's link

    There are 2 cases:
    1. Customized username
    raw_user_link = 'https://mbasic.facebook.com/ron.nguyen.3956?eav=AfYjeaOoH-eqxxXYACSWASeS6g3ha7sdS2pB2B-ogyRgB2aVKOeTGpnuoyA2cZLtOgU&paipv=0'
    2. Id
    raw_user_link = 'https://mbasic.facebook.com/profile.php?id=100074596420324&eav=AfYeYfHSPfkwTty78NbnrlW5eQC9afOivrr3yGde4chfuYWkzOuWEzRygQOx7_vU9_k&paipv=0'

    Args:
        raw_user_link (str): Raw user's link

    Returns:
        str: FB user link with format https://facebook.com/{user_name}. user_name can be either id or customized user name
    """

    parsed = urlparse(raw_user_link)
    ids: Optional[List[str]] = parse_qs(parsed.query).get('id')
    if ids is not None:
        id = ids[0]
    else:
        try:
            id = raw_user_link.split('?')[0].split('/')[-1]
        except:
            return raw_user_link
    return f'https://facebook.com/{id}'


def get_post_id_from_post_link(link_post: str) -> str:
    match = re.compile(r"posts/(.*)")
    try:
        link_post = match.search(link_post).group(1)
    except:
        return link_post

    return link_post
