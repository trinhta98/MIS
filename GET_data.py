import requests
import time, datetime, os, csv
import threading

token1 = 'EAAAAAYsX7TsBAAIT0yKd0gZCtJIXR7hTjzG0m3Bup6f0cjsb0V9pCPGU9n2sSp58ZCC2wdtLzqikd7LioArvoujLXVimzVGBSm4PruzpZCZAoKOQiTHwzUZArx4Tp1Ke0HmzxqJ4F1YqvjeeDfBh7mBBi8JN3cJXw2L2ZCPQbEMgZDZD'
token2 = 'EAAAAAYsX7TsBAKOkYvzoZCTGWAYLeN2RwWQlCz5SDhlTfaBTh7ZBSWjWcUr6LOhZCaGlFn5BRn62s14KKtfxdysVZBf5Xd6tI9eXGKlyO4AhFVqdEZBwhTh2sDUqo6NlbptPrfYAiOxo8tHblpkr4Xl4WSUac3vzNkdtBdeZBbWAZDZD'
token3 = 'EAAAAAYsX7TsBAFPUDk6vjsMmFRYZAGUxDvNymoDpvZBhjBWQIFjDWgBOz6ZC7Wfg6892BEbxZAWhFrE3oZC5uz4XnijgNGZBEE43gqJZB9onpZCucvvnspCeSU2A5ZBiu4xJXEs9j3uo8bqMbm6ZB3ZCUoJjMaeT7gz7Ivrb56M57vulwZDZD'
token4 = 'EAAAAAYsX7TsBAJ1VSKiaZANBBA4tZAMSFWZCYlE5vHRFcq3gzLhV5wxZBFuvuBzFH1ZBhBfPoYXym13zRABiZCgpCwYkTas1SDQewZBXdLWYf2Qz53F243Db3AEakHzpLl9Jl73fUl1KGk9qE3yHDqPLeNO4txd04rtIrS2QLoZCkwZDZD'
try:
    payload = {'method': 'get', 'access_token': token1}
    r = requests.get("https://graph.facebook.com/me", params=payload).json()
    id = r['id']
except KeyError:
    try:
        payload = {'method': 'get', 'access_token': token2}
        r = requests.get("https://graph.facebook.com/me", params=payload).json()
        id = r['id']
    except KeyError:
        try:
            payload = {'method': 'get', 'access_token': token3}
            r = requests.get("https://graph.facebook.com/me", params=payload).json()
            id = r['id']
        except KeyError:
            payload = {'method': 'get', 'access_token': token4}
def convert(text):
    text = text.split(',')
    text = ' '.join(text)
    text = text.split('\n')
    text = ' '.join(text)
    return text

def get_info(dsid):
    try:
        user_id = dsid.pop()
    except IndexError:
        return
    file_id = open('list_id.csv', 'a', encoding='utf-8')
    file_id.close()
    file_id = open('list_id.csv', 'r', encoding='utf-8')
    list_id = file_id.read()

    if user_id not in list_id:
        file_id.close()
        list_id = open('list_id.csv', 'a', newline='', encoding='utf-8')
        r_info = requests.get("https://graph.facebook.com/" + user_id + "?edges&access_token", params=payload).json()
        try:
            name = r_info['name']
        except KeyError:
            get_info(dsid)
        with list_id:
            writer_user = csv.writer(list_id)
            writer_user.writerows([[user_id, name]])

        print('Bắt đầu lấy thông tin: {}'.format(name))
        try:
            os.mkdir("data")
        except FileExistsError:
            pass
        path = "data/" + str(user_id) + '_' + name

        # ---------------------------------------------------------------------
        def info_birthday():
            try:
                birthday = r_info['birthday']
                if (len(birthday) == 5):
                    temp = birthday[3:5]
                    birthday = temp + birthday[2] + birthday[0:2]
                elif (len(birthday) == 10):
                    temp = birthday[3:5]
                    birthday = temp + birthday[2] + birthday[0:2] + birthday[5:10]
                else:
                    birthday = ''
            except KeyError:
                birthday = ''
            return birthday

        # ---------------------------------------------------------------------
        def info_zodiac():
            zodiac = ''
            try:
                if (len(info_birthday()) >= 5):
                    if (int(info_birthday()[3:5]) == 3 and int(info_birthday()[0:2]) >= 21):
                        zodiac = 'Bạch Dương'
                    elif (int(info_birthday()[3:5]) == 4 and int(info_birthday()[0:2]) <= 19):
                        zodiac = 'Bạch Dương'

                    if (int(info_birthday()[3:5]) == 4 and int(info_birthday()[0:2]) >= 20):
                        zodiac = 'Kim Ngưu'
                    elif (int(info_birthday()[3:5]) == 5 and int(info_birthday()[0:2]) <= 20):
                        zodiac = 'Kim Ngưu'

                    if (int(info_birthday()[3:5]) == 5 and int(info_birthday()[0:2]) >= 21):
                        zodiac = 'Song Tử'
                    elif (int(info_birthday()[3:5]) == 6 and int(info_birthday()[0:2]) <= 20):
                        zodiac = 'Song Tử'

                    if (int(info_birthday()[3:5]) == 6 and int(info_birthday()[0:2]) >= 21):
                        zodiac = 'Cự Giải'
                    elif (int(info_birthday()[3:5]) == 7 and int(info_birthday()[0:2]) <= 22):
                        zodiac = 'Cự Giải'

                    if (int(info_birthday()[3:5]) == 7 and int(info_birthday()[0:2]) >= 23):
                        zodiac = 'Sư Tử'
                    elif (int(info_birthday()[3:5]) == 8 and int(info_birthday()[0:2]) <= 22):
                        zodiac = 'Sư Tử'

                    if (int(info_birthday()[3:5]) == 8 and int(info_birthday()[0:2]) >= 23):
                        zodiac = 'Xử Nữ'
                    elif (int(info_birthday()[3:5]) == 9 and int(info_birthday()[0:2]) <= 22):
                        zodiac = 'Xử Nữ'

                    if (int(info_birthday()[3:5]) == 9 and int(info_birthday()[0:2]) >= 23):
                        zodiac = 'Thiên Bình'
                    elif (int(info_birthday()[3:5]) == 10 and int(info_birthday()[0:2]) <= 22):
                        zodiac = 'Thiên Bình'

                    if (int(info_birthday()[3:5]) == 10 and int(info_birthday()[0:2]) >= 23):
                        zodiac = 'Thần Nông'
                    elif (int(info_birthday()[3:5]) == 11 and int(info_birthday()[0:2]) <= 21):
                        zodiac = 'Thần Nông'

                    if (int(info_birthday()[3:5]) == 11 and int(info_birthday()[0:2]) >= 22):
                        zodiac = 'Nhân Mã'
                    elif (int(info_birthday()[3:5]) == 12 and int(info_birthday()[0:2]) <= 21):
                        zodiac = 'Nhân Mã'

                    if (int(info_birthday()[3:5]) == 12 and int(info_birthday()[0:2]) >= 22):
                        zodiac = 'Ma Kết'
                    elif (int(info_birthday()[3:5]) == 1 and int(info_birthday()[0:2]) <= 19):
                        zodiac = 'Ma Kết'

                    if (int(info_birthday()[3:5]) == 1 and int(info_birthday()[0:2]) >= 22):
                        zodiac = 'Bảo Bình'
                    elif (int(info_birthday()[3:5]) == 2 and int(info_birthday()[0:2]) <= 18):
                        zodiac = 'Bảo Bình'

                    if (int(info_birthday()[3:5]) == 2 and int(info_birthday()[0:2]) >= 19):
                        zodiac = 'Song Ngư'
                    elif (int(info_birthday()[3:5]) == 3 and int(info_birthday()[0:2]) <= 20):
                        zodiac = 'Song Ngư'
            except:
                zodiac = ''
            return zodiac

        # ---------------------------------------------------------------------
        def info_age_range():
            now_year = datetime.datetime.now().year
            if (len(info_birthday()) == 10):
                birthday_year = int(info_birthday()[6:])
                age_range = now_year - birthday_year
            else:
                age_range = ''
            return str(age_range)

        # ---------------------------------------------------------------------
        def info_education():
            try:
                # education = r_info['education']  # list
                education = ''
                for i in r_info['education']:
                    try:
                        name_school = i['school']['name']
                        try:
                            concentration_name = ' chuyên ngành ' + i['concentration'][0]['name'] + ' '
                        except KeyError:
                            concentration_name = ' '
                        education = education + name_school + concentration_name
                    except KeyError:
                        pass
            except KeyError:
                education = ''
            education = convert(education)
            return education

        # ---------------------------------------------------------------------
        def info_work():
            # work = r_info['work']  # list
            work = ''
            try:
                for i in r_info['work']:
                    try:
                        work_position = i['position']['name'] + ' tại: '
                    except KeyError:
                        work_position = ''
                    try:
                        work_employer = i['employer']['name']
                        try:
                            work_location = ' ở: ' + i['location']['name'] + ' '
                        except KeyError:
                            work_location = ' '
                    except KeyError:
                        work_employer = ' '
                        work_location = ' '

                    work = work + work_position + work_employer + work_location
            except KeyError:
                work = ''
            work = convert(work)
            return work

        # ---------------------------------------------------------------------
        def info_mobile_phone():
            try:
                mobile_phone = r_info['mobile_phone']
            except KeyError:
                mobile_phone = ''
            return mobile_phone

        # ---------------------------------------------------------------------
        def info_gender():
            try:
                gender = r_info['gender']
                if (gender == 'male'):
                    gender = 'Nam'
                elif (gender == 'female'):
                    gender = 'Nữ'
            except KeyError:
                gender = 'Không xác định'
            return gender

        # ---------------------------------------------------------------------
        def info_interested_in():
            try:
                # interested_in = r_info['interested_in'] #list
                interested_in = ''
                for i in r_info['interested_in']:
                    if (i == 'male'):
                        i = 'Nam'
                    elif (i == 'female'):
                        i = 'Nữ'
                    interested_in = interested_in + i + ' '
            except KeyError:
                interested_in = ''
            return interested_in

        # ---------------------------------------------------------------------
        def info_website():
            try:
                website = r_info['website']
                website = convert(website)
            except KeyError:
                website = ''
            return website

        # ---------------------------------------------------------------------
        def info_email():
            try:
                email = r_info['email']
            except KeyError:
                email = ''
            return email

        # ---------------------------------------------------------------------
        def info_sports():
            try:
                # sports = r_info['sports']  # list
                sports = ''
                for i in r_info['sports']:
                    sports = sports + i['name'] + ' '
                    sports = convert(sports)
            except KeyError:
                sports = ''
            return sports

        # ---------------------------------------------------------------------
        def info_hometown():
            try:
                hometown = r_info['hometown']['name']  # page
                hometown = convert(hometown)
            except KeyError:
                hometown = ''
            return hometown

        # ---------------------------------------------------------------------
        def info_location():
            try:
                location = r_info['location']['name']  # page
                location = convert(location)
            except KeyError:
                location = ''
            return location

        # ---------------------------------------------------------------------
        def info_locale():
            try:
                locale = r_info['locale']
            except KeyError:
                locale = ''
            return locale

        # ---------------------------------------------------------------------
        def info_relationship_status():
            try:
                relationship_status = r_info['relationship_status']
                if (relationship_status == "It's complicated"):
                    relationship_status = 'Phức tạp'
                elif (relationship_status == 'Single'):
                    relationship_status = 'Độc thân'
                elif (relationship_status == 'In a civil union'):
                    relationship_status = 'Kết hôn đồng tính'
                elif (relationship_status == 'In a relationship'):
                    relationship_status = 'Hẹn hò'
                elif (relationship_status == 'Engaged'):
                    relationship_status = 'Đã đính hôn'
                elif (relationship_status == 'Married'):
                    relationship_status = 'Đã kết hôn'
                elif (relationship_status == 'In a domestic partnership'):
                    relationship_status = 'Chung sống'
                elif (relationship_status == 'In an open relationship'):
                    relationship_status = 'Tìm hiểu'
                elif (relationship_status == 'Separated'):
                    relationship_status = 'Đã ly thân'
                elif (relationship_status == 'Đã ly hôn'):
                    relationship_status = 'Hẹn hò'
                elif (relationship_status == 'Widowed'):
                    relationship_status = 'Góa'
            except KeyError:
                relationship_status = ''
            return relationship_status

        # ---------------------------------------------------------------------
        def info_bio():
            try:
                bio = r_info['bio']
                bio = convert(bio)
            except KeyError:
                bio = ''
            return bio

        # ---------------------------------------------------------------------
        def info_languages():
            try:
                # languages = r['languages'] #list
                languages = ''
                for i in r_info['languages']:
                    languages = languages + i['name'] + ' '
            except KeyError:
                languages = ''
            return languages

        # ---------------------------------------------------------------------
        def info_political():
            try:
                political = r_info['political']
                political = convert(political)
            except KeyError:
                political = ''
            return political

        # ---------------------------------------------------------------------
        def info_religion():
            try:
                religion = r_info['religion']
                religion = convert(religion)
            except KeyError:
                religion = ''
            return religion

        # ---------------------------------------------------------------------
        def info_quotes():
            try:
                quotes = r_info['quotes']
                quotes = convert(quotes)
            except KeyError:
                quotes = ''
            return quotes

        # ---------------------------------------------------------------------
        def subcribers():
            subcribers = requests.get('https://graph.facebook.com/' + user_id + '/subscribers',
                                      params=payload).json()
            try:
                subcribers_count = subcribers['summary']['total_count']
            except KeyError:
                subcribers_count = 0
            return str(subcribers_count)

        # ---------------------------------------------------------------------

        info = 'Thông tin {} :'.format(
            name) + '\n- Ngày sinh: ' + info_birthday() + '\n- Tuổi: ' + info_age_range() + '\n- Cung: ' + info_zodiac() + \
               '\n- Giới tính: ' + info_gender() + '\n- Thích: ' + info_interested_in() + '\n- Email: ' + info_email() + \
               '\n- Số điện thoại: ' + info_mobile_phone() + \
               '\n- Học vấn: ' + info_education() + '\n- Website: ' + info_website() + '\n- Làm việc tại: ' + info_work() + \
               '\n- Quê quán: ' + info_hometown() + '\n- Nơi ở hiện tại: ' + info_location() + '\n- Mối quan hệ: ' + info_relationship_status() + \
               '\n- Ngôn ngữ: ' + info_languages() + '\n- Chính trị: ' + info_political() + '\n- Tôn giáo: ' + info_religion() + \
               '\n- Thể thao: ' + info_sports() + '\n- Giới thiệu: ' + info_bio() + '\n- Trích dẫn: ' + info_quotes() + \
               '\n- Số người theo dõi: ' + subcribers()
        # ---------------------------------------------------------------------
        try:
            os.mkdir(path)
        except:
            pass
        file = open(path + "/info.txt", "w", encoding='utf-8')
        file.write(info)
        file.close()
        info = [
            ['ID', 'Họ tên', 'Ngày sinh', 'Tuổi', 'Cung', 'Giới tính', 'Thích', 'Số điện thoại', 'Email', 'Website',
             'Học vấn', 'Công việc', 'Quê quán', 'Nơi ở hiện tại', 'Mối quan hệ', 'Ngôn ngữ', 'Chính trị',
             'Tôn giáo', 'Thể thao', 'Giới thiệu', 'Trích dẫn', 'Số người theo dõi'],
            [user_id, name, info_birthday(), info_age_range(), info_zodiac(), info_gender(), info_interested_in(),
             info_mobile_phone(), info_email(), info_website(), info_education(), info_work(), info_hometown(),
             info_location(), info_relationship_status(), info_languages(), info_political(), info_religion(),
             info_sports(), info_bio(), info_quotes(), subcribers()]
        ]
        file_info = open(path + "/info.csv", 'w', newline='', encoding='utf-8')
        with file_info:
            writer = csv.writer(file_info)
            writer.writerows(info)
        file_info.close()

        # ------------------------------------
        #           get info groups
        # ------------------------------------
        file = open(path + '/groups.txt', 'w', encoding='utf-8')
        file.close()
        file = open(path + '/groups.txt', 'a', encoding='utf-8')
        try:
            r_groups = requests.get('https://graph.facebook.com/' + user_id + '/groups', params=payload).json()
            i = 0
            for group in r_groups['data']:
                i += 1
                group_name = group['name']
                # group_id = group['id']
                group_privacy = group['privacy']
                file.write(str(i) + '. Group ' + group_privacy + ' : ' + group_name + '\n')
        except KeyError:
            pass
        file.close()

        # ------------------------------------
        #           get info page
        # ------------------------------------
        file_page = open(path + "/page.txt", 'w', newline='', encoding='utf-8')
        file_page.close()
        file_page = open(path + "/page.txt", 'a', newline='', encoding='utf-8')
        pages = requests.get("https://graph.facebook.com/" + user_id + "?fields=likes", params=payload).json()
        count = 0
        pagesData = pages['likes']['data']
        while True:
            try:
                for page in pagesData:
                    count += 1
                    page_id = page['id']
                    infoPage = requests.get("https://graph.facebook.com/" + page_id, params=payload).json()
                    try:
                        page_name = ' ' + infoPage['name']
                        page_name = convert(page_name)
                    except KeyError:
                        page_name = ''
                    try:
                        page_about = ' ' + infoPage['about']
                        page_about = convert(page_about)
                    except KeyError:
                        page_about = ''
                    try:
                        page_products = ' ' + infoPage['products']
                        page_products = convert(page_products)
                    except KeyError:
                        page_products = ''
                    try:
                        page_category = ' ' + infoPage['category']
                        page_category = convert(page_category)
                    except KeyError:
                        page_category = ''
                    file_page.write(str(count) + "{}, {}, {}, {}\n".format(page_name, page_category, page_about, page_products))
                else:
                    paging_next = pages['paging']['next']
                pages = requests.get(paging_next).json()
                pagesData = pages['data']
            except KeyError:
                file_page.close()
                break
        # ------------------------------------
        #           get feed
        # ------------------------------------
        file = open(path + "/feed.txt", "w", encoding='utf-8')
        file.close()
        file = open(path + "/feed.txt", "a", encoding='utf-8')
        # ---------------------------------------------------------------------
        r_feed = requests.get('https://graph.facebook.com/' + user_id + '/feed', params=payload).json()
        count_feed = 0
        while True:
            try:
                for data in r_feed['data']:
                    count_feed += 1
                    feed_id = data['id']
                    try:
                        message = convert(data['message'])
                    except KeyError:
                        message = ''
                    try:
                        description = ' | ' + convert(data['description'])
                    except KeyError:
                        description = ''
                    try:
                        name_root = data['name']
                    except KeyError:
                        pass
                    comments = requests.get('https://graph.facebook.com/' + feed_id + '/comments',
                                            params=payload).json()
                    cmt = ''
                    try:
                        for comment in comments['data']:
                            cmt_id = comment['from']['id']
                            if (cmt_id == user_id):
                                try:
                                    cmt_content = ', ' + convert(comment['message'])
                                except KeyError:
                                    cmt_content = ''
                                cmt = cmt + cmt_content
                    except KeyError:
                        pass
                    file.write(str(count_feed) + '. ' + message + description + cmt + '\n')
                try:
                    next_paging = r_feed['paging']['next']
                    r_feed = requests.get(next_paging).json()
                except KeyError:
                    file.close()
                    break
            except KeyError:
                get_info(dsid)
        print("Đã lấy xong thông tin: {}".format(name))
        get_info(dsid)
    else:
        pass

# get_info(['100021329296898'])

file_id = []
for line in open('listID.txt', 'r'):
    file_id.append(line[:-1])
# get_info(file_id)
while True:
    try:
        try:
            t1 = threading.Thread(target=get_info, args=(file_id,))
        except:
            pass
        try:
            t2 = threading.Thread(target=get_info, args=(file_id,))
        except:
            pass
        try:
            t3 = threading.Thread(target=get_info, args=(file_id,))
        except:
            pass
        try:
            t4 = threading.Thread(target=get_info, args=(file_id,))
        except:
            pass
        try:
            t5 = threading.Thread(target=get_info, args=(file_id,))
        except:
            pass
        try:
            t6 = threading.Thread(target=get_info, args=(file_id,))
        except:
            pass
        try:
            t7 = threading.Thread(target=get_info, args=(file_id,))
        except:
            pass
        try:
            t8 = threading.Thread(target=get_info, args=(file_id,))
        except:
            pass
        try:
            t9 = threading.Thread(target=get_info, args=(file_id,))
        except:
            pass
        try:
            t1.start()
            time.sleep(0.5)
        except TypeError:
            pass
        try:
            t2.start()
            time.sleep(0.5)
        except TypeError:
            pass
        try:
            t3.start()
            time.sleep(0.5)
        except TypeError:
            pass
        try:
            t4.start()
            time.sleep(0.5)
        except TypeError:
            pass
        try:
            t5.start()
            time.sleep(0.5)
        except TypeError:
            pass
        try:
            t6.start()
            time.sleep(0.5)
        except TypeError:
            pass
        try:
            t7.start()
            time.sleep(0.5)
        except TypeError:
            pass
        try:
            t8.start()
            time.sleep(0.5)
        except TypeError:
            pass
        try:
            t9.start()
            time.sleep(0.5)
        except TypeError:
            pass
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
    except:
        pass