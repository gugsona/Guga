import requests
import json
import sqlite3
# ნაწილი 1
# ბაზის გახსნამდე

# url = 'https://yts.mx/api/v2/movie_suggestions.json?movie_id=1'                   # ლინკი
# r = requests.get(url)

# print(r)                                                                       # request მოდულები
# print(r.text)
# print(r.headers)
# print(r.status_code)

# res = json.loads(r.text)                                                         # json ში გადაყვანა

# with open('movies.json', 'w') as f:                                            # json ფაილში შენახვა
#     json.dump(res, f, indent=4)


# print(json.dumps(res, indent=4))                                               # მთლიანი ინფორმაცია ფილმზე


# movie_name = (res['data']['movies'][0]['title'])
# movie_year = (res['data']['movies'][0]['year'])
# movie_rating = (res['data']['movies'][0]['rating'])
# print('ფილმის სახელია -', movie_name, ',', 'გამოშვების წელი -', movie_year, ',', 'რეიტინგი -', movie_rating)   # ინფორმაციის დაბეჭდვა


# ორად გავყავი რომ მარტივად გაგეგოთ კოდი <3



# ნაწილი 2
# ბაზის გახსნა
# conn = sqlite3.connect('movies.sqlite')
# c = conn.cursor()
# c.execute(''' CREATE TABLE if not exists movies
#          (id INTEGER PRIMARY KEY AUTOINCREMENT,
#          Movie_name VARCHAR(20),
#          Publish_year INTEGER,
#          Rating INTEGER)''')
#
#
#
# numbers = range(100)
# for x in numbers:
#     url = f'https://yts.mx/api/v2/movie_suggestions.json?movie_id={x}'                   # ლინკი
#     r = requests.get(url)
#     res = json.loads(r.text)
#     movie_name = (res['data']['movies'][0]['title'])
#     movie_year = (res['data']['movies'][0]['year'])
#     movie_rating = (res['data']['movies'][0]['rating'])
#     all_rows = []
#     row = (movie_name, movie_year, movie_rating)
#     all_rows.append(row)
#
#
#
#     c.executemany('INSERT INTO movies (Movie_name, Publish_year, Rating) VALUES (?, ?, ?)', all_rows)
#
#
# conn.commit()
# conn.close()


