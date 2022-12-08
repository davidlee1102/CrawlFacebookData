import re

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


def get_post_id_from_post_link(link_post: str) -> str:
    match = re.compile(r"posts/(.*)")
    try:
        link_post = match.search(link_post).group(1)
    except:
        return link_post

    return link_post
