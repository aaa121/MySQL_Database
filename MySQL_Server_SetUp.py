# http://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# http://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
# http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
import mysql.connector
'''
#Fix the bug later
config={'user': 'tripplehay777',
        'password':'akinakin88',
        'host':'tripplehay777.mysql.pythonanywhere-services.com',
        'database':'tripplehay777$tutorial',
        'raise_on-warnings':True,
        }
conn=sql.connect(**config)
'''
con=mysql.connector.connect(user='tripplehay777',password='akinakin88',
                host='tripplehay777.mysql.pythonanywhere-services.com',
                database='tripplehay777$tutorial')

cursor=con.cursor()
query=("SELECT * FROM Poll_Feeds")
cursor.execute(query)

#for rows in cursor:
    #print(rows)
for (time,retweet,likes,tweets) in cursor:
    print("Date:{}\tRetweet:{}\tLikes:{}\tTweet:{}".format(time,retweet,likes,tweets))
'''
# http://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
# http://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
#Add to database using :
    add_poll_feeds=INSERT INTO Poll_Feeds VALUES (%s, %s, %s, %s)
    data_poll_feeds=(1460010403,395,516,'RT @rulajebreal: Trump calls desperate #SyrianRefugees \"vicious snakes.\"  Is US Media a complicit enabler by airing such hateful &amp; racist v\u2026')
    cursor.execute(add_poll_feeds,data_poll_feeds)
    con.commit()

    or

    data_poll_feeds=(time,retweet,likes,tweets)
    con.commit()
'''
cursor.close()
con.close()



