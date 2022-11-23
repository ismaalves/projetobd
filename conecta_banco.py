import os
import psycopg2

print("Conectando...")
try:
    conn = psycopg2.connect(
        host="ec2-18-209-78-11.compute-1.amazonaws.com",
        database="db2t6gb1jdbstc",
        user="qivwowphbqoskt",
        password="f3a71db6832d18c702e3a8ffc7982beec2f2494c28fc178c965c683b2c15e1c0"
    )
except psycopg2.Error as err:
    print(f"{err.pgerror}")