import mysql.connector as mariadb


mariadb_connection = mariadb.connect(user='root', password='1234', database='yelp_academic')
cursor = mariadb_connection.cursor()

#Create user table
def createUserTable():
    cursor.execute("CREATE TABLE user(user_id CHAR(22),\
                    name VARCHAR(50),\
                    review_count INT,\
                    member_since date,\
                    friends MEDIUMTEXT,\
                    average_stars FLOAT(4),\
                    Primary Key (user_id))")
    print("User Table created") 

#Create review table
def createReviewTable():
    cursor.execute( "CREATE TABLE review(\
                    review_id CHAR(22),\
                    user_id CHAR(22),\
                    business_id CHAR(22),\
                    stars INT, \
                    date CHAR(10),\
                    text VARCHAR(20000),\
                    PRIMARY KEY(review_id),\
                    FOREIGN KEY(user_id) REFERENCES user(user_id),\
                    FOREIGN KEY(business_id) REFERENCES business(business_id))")
    print("Review Table created")

#Create business table
def createBusinessTable():    
    cursor.execute("CREATE TABLE business (\
        business_id varchar(22),\
        name varchar(100),\
        address varchar(255),\
        city varchar(100),\
        state varchar(4),\
        postal_code varchar(10),\
        stars float(23),\
        review_count INT,\
        is_open bool,\
        description varchar(5000)\
        hours varchar(200),\
        PRIMARY KEY (business_id))")
    print("Business Table created")