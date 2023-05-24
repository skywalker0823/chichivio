# from dotenv import load_dotenv
# import os
# import MySQLdb

# load_dotenv()

# class DB:
#     def __init__(self) -> None:
#         self.connection = MySQLdb.connect(
#             host= os.getenv("HOST"),
#             user=os.getenv("USERNAME"),
#             passwd= os.getenv("PASSWORD"),
#             db= os.getenv("DATABASE"),
#             autocommit = True,
#             ssl_mode = "VERIFY_IDENTITY",
#             ssl      = {
#                 "ca": "/etc/ssl/cert.pem"
#             }
#         )
#         self.cursor = self.connection.cursor()
    
#     def is_connected(self):
#         if self.connection.open:
#             return True
#         else:
#             return False