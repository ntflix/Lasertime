from sources.database_info import DatabaseInfo


class LasertimeServer:
    __db_info: DatabaseInfo

    def start_server(self, database: DatabaseInfo) -> int:
        error_code = 0

        print("Server started")
        raise NotImplementedError()

        return error_code
