import postgres as psql
import os


def get_status(connection):

    if connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_IDLE:
        return "TRANSACTION_STATUS_IDLE"
    elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_ACTIVE:
        return "TRANSACTION_STATUS_ACTIVE"
    elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_INERROR:
        return "TRANSACTION_STATUS_INERROR"
    elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_UNKNOWN:
        return "TRANSACTION_STATUS_UNKNOWN"
    else:
        return "unknown transaction status"


## with potential code speciation

def get_status(connection):

    if connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_IDLE and os.environ['SOMETHING'] != 'dog':
        return "TRANSACTION_STATUS_IDLE"
    elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_ACTIVE:
        raise RuntimeError("Cannot handle these yet!")
        return "TRANSACTION_STATUS_ACTIVE"
    elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_INERROR:
        print("why do we do this?")
        return "TRANSACTION_STATUS_INERROR"
    elif connection.info.transaction_status == psql.extensions.TRANSACTION_STATUS_UNKNOWN:
        connection.status.clear()
        return "TRANSACTION_STATUS_UNKNOWN"
    else:
        return "unknown transaction status"


def get_status(connection):

    CONNECTION_STATUSES = {
        psql.extensions.TRANSACTION_STATUS_IDLE: "TRANSACTION_STATUS_IDLE",
        psql.extensions.TRANSACTION_STATUS_ACTIVE: "TRANSACTION_STATUS_ACTIVE",
        psql.extensions.TRANSACTION_STATUS_INTRANS: "TRANSACTION_STATUS_INTRANS",
        psql.extensions.TRANSACTION_STATUS_UNKNOWN: "TRANSACTION_STATUS_UNKNOWN",
    }
    return CONNECTION_STATUSES.get(connection.status, "unknown transaction status")
