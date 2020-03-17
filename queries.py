# Select top [number] businesses in a city based on their rating
def topBusinesses(city, number):
    sql = "SELECT name, city, stars, description FROM\
            business\
            WHERE city=" + city + "\
            ORDER BY stars DESC\
            LIMIT " + number

    cursor.execute(sql)
    results = cursor.fetchall()
    i = 1
    for r in results:
            print(i, ")")
            print(r[0], " in ", r[1] , "| rating:", r[2], "/5 |")
            print("Description:", r[3])
            print("_________________________________________")
            i += 1

def businessByCat(category):
    sql = "SELECT name, city, stars, description FROM\
            business b, categories c\
            WHERE business.business_id = categories.business_id\
            AND category.category=" + category
    cursor.execute(sql)
    results = cursor.fetchall()
    i = 1
    for r in results:
            print(i, ")")
            print(r[0], " in ", r[1] , "| rating:", r[2], "/5 |")
            print("Description:", r[3])
            print("_________________________________________")
            i += 1