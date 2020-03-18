def allReviews(business_id):
   sql = "SELECT r.user_id, u.name, r.date, r.stars, r.text\
            FROM user u, review r\
            WHERE r.business_id='" + business_id
    cursor.execute(sql)
    results = cursor.fetchall()
    i = 1
    for r in results:
        print(i, ")")
        print(i, "userID:", r[0], "| username: ",
        r[1], "| date:", r[2],"rating:", r[3] "/5 |")
        print("Comment:", r[4])
        print("_________________________________________")
        i += 1

def allFriends(user_id):
    sql = "SELECT u.user_id, u.name, \
        FROM user u, friends f\
        WHERE
            
