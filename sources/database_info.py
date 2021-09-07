class DatabaseInfo:
    __db_host: str
    __db_port: int
    __db_username: str
    __db_password: str
    __db_name: str

    def __init__(
        self,
        host: str = "hostname",
        port: int = 3306,
        username: str = "root",
        password: str = "password",
        db_name: str = "laser",
    ) -> None:
        self.__db_host = host
        self.__db_port = port
        self.__db_username = username
        self.__db_password = password
        self.__db_name = db_name

    @property
    def database_host(self) -> str:
        return self.__db_host

    @property
    def database_port(self) -> int:
        return self.__db_port

    @property
    def database_username(self) -> str:
        return self.__db_username

    @property
    def database_password(self) -> str:
        return self.__db_password

    @property
    def database_name(self) -> str:
        return self.__db_name
