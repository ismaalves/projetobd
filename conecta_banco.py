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


#SELECTS "CRUS" EM SQL PELO PYTHON SE FAZEM ASSIM:

#Abre um cursor
cursor = conn.cursor()

#Passa o comando em SQL como string para o metodo execute()
select="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Filme'"

cursor.execute(select)

nomes_colunas = cursor.fetchall()

cursor.execute('select * from "Filme"')

print(f'{nomes_colunas[:3]}')

#Itera sobre a saida do fetchall()
for filme in cursor.fetchall():
    print(f'{filme[0]} | {filme[1]} | {filme[2]}')


cursor.close()
conn.close()