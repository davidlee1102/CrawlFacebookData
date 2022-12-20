import pandas as pd


def convert_list_comment_to_json(data_list: list):
    user_info_link_list = []
    user_info_name_list = []
    comment_content_list = []
    if isinstance(data_list, list):
        for data in data_list:
            user_info_link_list.append(data.get("user_info_link", "").replace("mbasic.", ""))
            user_info_name_list.append(data.get("user_info_name", ""))
            comment_content_list.append(data.get("comment_content", ""))
        user_comment_dict = {'user_info_link': user_info_link_list, 'user_info_name': user_info_name_list,
                             'comment_content': comment_content_list}
        df = pd.DataFrame(user_comment_dict)
        df.to_csv('EVNCrawlFacebook/data_save/comment_list.csv', encoding="utf-8")
        return True
    else:
        return False


def convert_list_reaction_to_json(data_list: list):
    user_info_link_list = []
    user_info_name_list = []
    reaction_type_list = []
    if isinstance(data_list, list):
        for data in data_list:
            user_info_link_list.append(data.get("user_info_link", "").replace("mbasic.", ""))
            user_info_name_list.append(data.get("user_info_name", ""))
            reaction_type_list.append(data.get("reaction_type", ""))
        user_comment_dict = {'user_info_link': user_info_link_list, 'user_info_name': user_info_name_list,
                             'reaction_type': reaction_type_list}
        df = pd.DataFrame(user_comment_dict)
        df.to_csv('EVNCrawlFacebook/data_save/comment_list.csv', encoding="utf-8")
        return True
    else:
        return False
