import csv, re


mp = ['mỹ phẩm', 'ví trang điểm', ' bông tẩy trang', 'bông tai', 'mặt nạ', 'sữa rửa mặt', 'makeup', 'make up', 'kem nền', 'son phấn', 'tô son', 'bb cream', 'cc cream', 'phấn phủ', 'kẻ mắt', 'bôi son', 'son môi', 'kem chống nắng', 'kem dưỡng da', 'kem dưỡng ẩm', 'dầu dưỡng da', 'sữa tắm', 'sữa rửa mặt', 'uốn mi', 'cọ trang điểm']

new_user = [['ID', 'Họ tên', 'Ngày sinh', 'Tuổi', 'Cung', 'Giới tính', 'Thích', 'Số điện thoại', 'Email', 'Website', 'Học vấn', 'Công việc', 'Quê quán', 'Nơi ở hiện tại', 'Mối quan hệ', 'Ngôn ngữ', 'Chính trị', 'Tôn giáo', 'Thể thao', 'Giới thiệu', 'Trích dẫn', 'Số người theo dõi','Số bài viết chứa keyword mỹ phẩm', 'Số page có chứa keyword về mỹ phẩm', 'Số group có chứa keyword về mỹ phẩm', 'keyword mỹ phẩm']]
result_mp = open('result_mp.csv', 'w', encoding='utf-8')
with result_mp:
    writer = csv.writer(result_mp)
    writer.writerows(new_user)
result_mp.close()

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
                    for item in mp:
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
                    for item in mp:
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
                    for item in mp:
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
            result_mp = open('result_mp.csv', 'a', encoding='utf-8')
            with result_mp:
                writer = csv.writer(result_mp)
                writer.writerows(new_user)
                result_mp.close()

        except FileNotFoundError:
            pass
print('Đã phân tích xong!')