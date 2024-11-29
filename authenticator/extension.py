from common_utils.logger import ActionLogger

from authenticator.infras.db.connection import DBConnectionHandler

action_logger = ActionLogger()
db = DBConnectionHandler()
