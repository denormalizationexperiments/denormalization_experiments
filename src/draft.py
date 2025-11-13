import database.create_connection as create_connection
import database.configure_database as configure_database
import tpch.query_generator as query_generator



if __name__ == "__main__":


    #################################
    #                               #
    #     Experiment Settings       #
    #                               #
    #################################


    # experiment settings, change to input arguments for python file and run shell scripts 

    scaling_factor = 1

    rdbms = "mysql"


    #################################
    #                               #
    #        Connect to DB          #
    #                               #
    #################################

    # authenticate and create database connection, configure database system

    if rdbms == "mysql":
        db_conncetion = create_connection.create_mysql_connection(scaling_factor)
        configure_database.configure_mysql(db_conncetion)

    if rdbms =="postgres":
        # connect to postgres
        # configure postgres
        pass
        

    if rdbms =="sqlserver":
        # connect to sqlserver
        # configure sqlserver
        pass


    #################################
    #                               #
    #     Execture expeiments       #
    #                               #
    #################################

    cursor = db_conncetion.cursor()

    cursor.execute(query_generator.generate_query(1)[0])

    for result in cursor:
        print(result)

        

    










    