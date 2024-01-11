import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.flipkart.com/apple-iphone-14-midnight-128-gb/product-reviews/itm9e6293c322a84?pid=MOBGHWFHECFVMDCX&lid=LSTMOBGHWFHECFVMDCXXRTRJG&marketplace=FLIPKART&page='


index = 0;
data_rows = []
headers = ['S.No.', 'User', 'Rating', 'Review_summary', 'Customer_info', 'Date', 'Upvote', 'Downvote', 'Review_detail']
cur_page = 1
while(cur_page < 510):
    cur_url = url + str(cur_page);
    response = requests.get(cur_url)
    prev = len(data_rows)
    print(prev, cur_page)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        review_table = soup.find_all('div', class_='col _2wzgFH K0kLPL');

        for i in review_table:
            current_row = []
            
            index = index + 1;
            rating = i.find('div', class_='_3LWZlK').text
            review_summary = i.find('p', class_='_2-N8zT').text
            review_detail = i.find('div', class_='t-ZTKy').text  
            user = i.find('p', class_='_2sc7ZR _2V5EHH').text
            upvote = i.find('div', class_='_1LmwT9').text
            downvote = i.find('div', class_='_1LmwT9 pkR4jH').text
            customer_info = i.find('p', class_='_2mcZGG').text
            date = i.find('p', class_='_2sc7ZR').text

            if(len(review_detail)) :
                review_detail = review_detail.split("READ MORE")[0];
            
            current_row.append(index)
            current_row.append(user)
            current_row.append(rating)
            current_row.append(review_summary)
            current_row.append(customer_info)
            current_row.append(date)
            current_row.append(upvote)
            current_row.append(downvote)
            current_row.append(review_detail)
            data_rows.append(current_row)

    now = len(data_rows)
    if(now > prev):
        cur_page = cur_page + 1


with open('reviews_data.csv', 'w', newline='', encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(headers)
    csv_writer.writerows(data_rows)

print("Done.")
