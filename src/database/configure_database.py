

def configure_mysql(connection):
    cursor = connection.cursor()

    cursor.execute("SET GLOBAL innodb_buffer_pool_size = 34359738368") # 32GB
    cursor.execute("SET GLOBAL tmp_table_size = 2147483648") # 2GB
    cursor.execute("SET GLOBAL max_heap_table_size = 2147483648") # 2GB
    cursor.execute("SET GLOBAL join_buffer_size = 16777216") # 16MB
