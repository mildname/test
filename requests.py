import requests
import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_valid_website(website):
    website_regex = r'^(https?://)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return re.match(website_regex, website) is not None

def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def test_users_data():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()

    for user in users:
        name = user['name']
        email = user['email']
        website = user['website']
        lat = user['address']['geo']['lat']
        lng = user['address']['geo']['lng']
        company_name = user['company']['name']

        # ตรวจสอบข้อมูลตามเงื่อนไขที่กำหนด
        name_valid = name != ""
        email_valid = is_valid_email(email)
        website_valid = is_valid_website(website)
        lat_valid = is_valid_number(lat)
        lng_valid = is_valid_number(lng)
        company_name_valid = company_name != ""

        # แสดงผลการทดสอบ
        if all([name_valid, email_valid, website_valid, lat_valid, lng_valid, company_name_valid]):
            result = "PASS"
        else:
            result = "FAIL"
        
        print(f"User ID {user['id']}: {result}")

# เรียกใช้ฟังก์ชันทดสอบ
test_users_data()
