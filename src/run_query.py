import tpch.query_generator as query_generator


def run(connection, query_number):

    query = query_generator.generate_query(query_number)

    return query