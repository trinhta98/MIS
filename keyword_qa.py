import csv, re

qa = ['q.áo', 'quần áo', 'đồng phục', 'trang phục', 'sơ mi', 'vest','áo thun', 'thời trang', 'ba lỗ', 'áo cộc', 'áo len', 'váy', 'đầm', 'quần bò', 'áo bò', 'vải', 'cotton', 'áo khoác', 'áo sơ mi', 'áo dài', 'áo gió', 'cái ví', 'khăn', 'áo da', 'quần da', 'đeo len']

new_user = [['ID', 'Họ tên', 'Ngày sinh', 'Tuổi', 'Cung', 'Giới tính', 'Thích', 'Số điện thoại', 'Email', 'Website', 'Học vấn', 'Công việc', 'Quê quán', 'Nơi ở hiện tại', 'Mối quan hệ', 'Ngôn ngữ', 'Chính trị', 'Tôn giáo', 'Thể thao', 'Giới thiệu', 'Trích dẫn', 'Số người theo dõi','Số bài viết chứa keyword quần áo', 'Số page có chứa keyword về quần áo', 'Số group có chứa keyword về quần áo', 'keyword quần áo']]
result_qa = open('result_qa.csv', 'w', encoding='utf-8')
with result_qa:
    writer = csv.writer(result_qa)
    writer.writerows(new_user)
result_qa.close()

list_id = open('list_id.csv', 'r', encoding='utf-8')
with list_id:
    reader = csv.reader(list_id)
    for row in reader:
        try:
            path = 'data/' + row[0] + '_' + row[1]

            user_info = open(path + '/info.csv', 'r', encoding='utf-8')


            # print(row[1] + ':')
            count_timeline = 0
            key = ''
            try:
                for line in open(path + '/feed.txt', 'r', encoding='utf-8'):
                    for item in qa:
                        match = re.search(' ' + item + ' ', line, re.I | re.U)
                        if match:  # nếu tồn tại chuỗi khớp
                            count_timeline += 1
                            key = key + '|' + item
                            break
            except FileNotFoundError:
                continue
            count_page = 0
            try:
                for line in open(path + '/groups.txt', 'r', encoding='utf-8'):
                    for item in qa:
                        match = re.search(' ' + item + ' ', line, re.I | re.U)
                        if match:  # nếu tồn tại chuỗi khớp
                            count_page += 1
                            key = key + '|' + item
                            break
            except FileNotFoundError:
                continue
            count_group = 0
            try:
                for line in open(path + '/page.txt', 'r', encoding='utf-8'):
                    for item in qa:
                        match = re.search(' ' + item + ' ', line, re.I | re.U)
                        if match:  # nếu tồn tại chuỗi khớp
                            count_group += 1
                            key = key + '|' + item
                            break
            except FileNotFoundError:
                continue

            with user_info:
                reader_info = csv.reader(user_info)
                parity = 0
                new_user = []
                for row_info in reader_info:
                    parity += 1
                    if (parity == 2):
                        parity = 0
                        row_info.append(count_timeline)
                        row_info.append(count_page)
                        row_info.append(count_group)
                        row_info.append(key)
                        new_user.append(row_info)
                    # print(row_info)
            # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            user_info.close()
            result_qa = open('result_qa.csv', 'a', encoding='utf-8')
            with result_qa:
                writer = csv.writer(result_qa)
                writer.writerows(new_user)
                result_qa.close()

        except FileNotFoundError:
            pass
print('Đã phân tích xong!')