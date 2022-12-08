from typing import Dict, List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from EVNCrawlFacebook.selenium.utils import facebook_login
from EVNCrawlFacebook.utils import pre_process_selenium

import time


def check_more_comments(
        driver: WebDriver,
        post_id: str,
) -> List[Dict[str, str]]:
    """Get comments of a post

    Args:
        driver (WebDriver): a web driver
        post_id (str): id of the post

    Returns:
        List[str]: list of comments
    """
    text_check = driver.find_elements(
        by=By.XPATH,
        value=f'//*[@id="ufi_{post_id}"]/div/div[4]'
    )
    comments_list: List[Dict[str, str]] = []

    if len(text_check) > 0 and "Xem" in text_check[-1].text:
        comments_list.extend(get_large_comments(driver, post_id))
        url = driver.find_element(
            by=By.XPATH,
            value=f'//*[@id="ufi_{post_id}"]/div/div[4]/div/a'
        ).get_attribute('href')
        driver.get(url)
        try:
            comments_list.extend(check_more_comments(driver, post_id))
        except:
            print('Error View previous comments')
    else:
        comments_list.extend(get_small_comments(driver, post_id))
    return comments_list


def get_large_comments(driver: WebDriver, post_id: str) -> List[Dict[str, str]]:
    comments_list: List[str] = []
    users_list: List[Dict[str, str]] = []
    xpath_address = f'//*[@id="ufi_{post_id}"]/div/div[4]/div/div/div[1]'
    comments = driver.find_elements(by=By.XPATH, value=xpath_address)
    for comment in comments:
        comment = comment.text
        comments_list.append(comment)

    xpath_address = f'//*[@id="ufi_{post_id}"]/div/div[4]/div/div/h3/a'
    user_infors = driver.find_elements(by=By.XPATH, value=xpath_address)

    for user_info in user_infors:
        user_info_dict = {}
        user_info_dict['user_info_link'] = user_info.get_attribute('href')
        user_info_dict['user_info_name'] = user_info.text
        users_list.append(user_info_dict)
    for i in range(0, len(users_list)):
        users_list[i]['comment_content'] = comments_list[i]

    return users_list


def get_small_comments(driver: WebDriver, post_id: str) -> List[Dict[str, str]]:
    comments_list: List[str] = []
    users_list: List[Dict[str, str]] = []
    xpath_address = f'//*[@id="ufi_{post_id}"]/div/div[5]/div/div/div[1]'
    comments = driver.find_elements(by=By.XPATH, value=xpath_address)
    for comment in comments:
        comment = comment.text
        comments_list.append(comment)

    xpath_address = f'//*[@id="ufi_{post_id}"]/div/div[5]/div/div/h3/a'
    user_infors = driver.find_elements(by=By.XPATH, value=xpath_address)

    for user_info in user_infors:
        user_info_dict = {}
        user_info_dict['link_user_account'] = pre_process_selenium.post_processing_user_link(
            user_info.get_attribute('href')
        )
        user_info_dict['user_name'] = user_info.text
        users_list.append(user_info_dict)

    for i in range(0, len(users_list)):
        users_list[i]['comment_content'] = comments_list[i]

    return users_list


def crawler_comments(post_link: str, post_id: str):
    driver = facebook_login.login()
    driver.get(post_link)
    time.sleep(5)
    return check_more_comments(driver, post_id)


def process_comment(post_link: str, max_no_comments: int):
    post_id = pre_process_selenium.get_post_id_from_post_link(post_link)
    post_link = pre_process_selenium.change_facebook_link_to_mbasic(post_link)
    if "groups" not in post_link or not post_id:
        return None
    comments_list = crawler_comments(post_link, post_id)
    if max_no_comments is 0 or max_no_comments > len(comments_list):
        return comments_list
    else:
        return comments_list[0:max_no_comments]
