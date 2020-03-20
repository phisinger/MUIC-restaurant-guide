import mysql.connector as mariadb


mariadb_connection = mariadb.connect(user='root', password='1234', database='muic_restaurant_guide')
cursor = mariadb_connection.cursor()

# Select top [number] businesses in a city based on their rating
def topBusinesses(city, number):
    sql = "SELECT name, city, stars, description FROM\
            business\
            WHERE city='" + city + "'" + "\
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

# Show all reviews of a business
def allReviews(business_id):
        sql = "SELECT r.user_id, u.name, r.date, r.stars, r.text\
        FROM user u JOIN review r ON u.user_id=r.user_id\
        WHERE r.business_id=" + business_id


        cursor.execute(sql)
        results = cursor.fetchall()
        i = 1
        for r in results:
                print(i, ")")
                print(i, "userID:", r[0], "| username: ", r[1], "| date:", r[2],"rating:", r[3], "/5 |")
                print("Comment:", r[4])
                print("_________________________________________")
                i += 1
         
#returns all businesses with a certain category
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

       

def allFriends(user_id):
    sql = "SELECT u.user_id, u.name, \
        FROM user u, friends f\
        WHERE"
            
