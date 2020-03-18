import mysql.connector as mariadb
import csv
import os
from datetime import datetime


mariadb_connection = mariadb.connect(user='root', password='1234', database='yelp_academic')
cursor = mariadb_connection.cursor()

#Create user table
def createUserTable():
    cursor.execute("CREATE TABLE user(user_id INT,\
                    name VARCHAR(50),\
                    review_count INT,\
                    member_since date,\
                    friends MEDIUMTEXT,\
                    average_stars FLOAT(4),\
                    Primary Key (user_id))")
    print("User Table created")

def createFriendTable():
    cursor.execute("CREATE TABLE friends(user_id INT,\
                    friend INT,\
                    FOREIGN KEY(user_id) REFERENCES user(user_id))")
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

def cleanUp():
    cursor.execute("DROP TABLE if exists review")
    cursor.execute("DROP table if exists user")
    cursor.execute("DROP TABLE if exists business")

# Maybe we need a table "menu" ?

def insertData():
    # function to insert after the initial insert manually by using the application
    pass

def import_csv(tableName):
    # function to import all data given by csv files
    cur_path = os.path.dirname("tables.py")
    with open(os.path.join(cur_path, "csv", tableName+".csv"), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        column = 1
        for row in csv_reader:
            if column:
                column = 0
            else:
                # build the insert command
                #count+=1
                sql = "INSERT INTO "+ tableName + " VALUES ("
                for key in row:
                    if (row[key]==None):
                        string="null,"
                    else:
                        # data processing to clean the data
                        string="'"+(str(row[key]))+ "'," #.replace("'","")).replace("\\","\\\\")+"',"
                    sql+=string
                sql=sql[:-1]+");\n"
                #print(sql)
                cursor.execute(sql)
        mariadb_connection.commit()

# import_csv("business")