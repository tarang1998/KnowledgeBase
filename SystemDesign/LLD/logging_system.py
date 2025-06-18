from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime
import threading
import json
from typing import Optional, Dict, List


class LogLevel(Enum):
    DEBUG = 10 
    INFO = 20 
    WARNING = 30 
    ERROR = 40 
    FATAL = 50 


class LogRecord:
    def __init__(self,level : LogLevel, message: str, context: Dict = None):
        self.timestamp = datetime.now()
        self.level = level
        self.message = message
        self.context = context 

    def __repr__(self):
        return f"<Log Record {self.level.name} {self.timestamp.isoformat()} {self.message} {self.context}>"
    
# Strategy Pattern via LogFormatter → SimpleFormatter & JsonFormatter
class LogFormatter(ABC):
    @abstractmethod
    def format(self, record : LogRecord) -> str:
        pass
# Strategy Pattern via LogAppender → ConsoleAppender & FileAppender
class SimpleFormatter(LogFormatter):
    def format(self, record : LogRecord)->str:
        ts = record.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        ctx = "" if not record.context else f" | context={record.context}"
        return f"[{ts}] [{record.level.name}] {record.message} {ctx}"
        

class JSONFormatter(LogFormatter):
    def format(self,record: LogRecord) -> str:
        payload = {
            "timestamp": record.timestamp.isoformat(),
            "level" : record.level.name,
            "message" : record.message,
            "context" : record.context
        }
        return json.dump(payload)
    
class LogAppender(ABC):
    @abstractmethod
    def append(self,formatted_message: str):
        pass

class ConsoleAppender(LogAppender):
    def append(self, formatted_message):
        print(formatted_message)

class FileAppender(LogAppender):
    def __init__(self, file_path : str):
        self.file_path = file_path
        self._lock = threading.Lock()

    def append(self, formatted_message: str):
        with self._lock:
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(formatted_message + "\n")

class LogHandler(ABC):
    def __init__(self, level : LogLevel, formatter : LogFormatter, appender : LogAppender):
        self.level = level
        self.formatter = formatter
        self.appender = appender
        self.next_handler = None

    def set_next(self, handler : 'LogHandler'):
        self.next_handler = handler

    def handle(self, record : LogRecord):
        if record.level.value >= self.level.value:
            msg = self.formatter.format(record)
            self.appender.append(msg)
        if self.next_handler:
            self.next_handler.handle(record)

class Logger:
    _instances = {}
    _lock = threading.Lock()

    # Singleton Pattern
    def __new__(cls,name:str = 'default'):
        with cls._lock:
            if name not in cls._instances:
                instance = super().__new__(cls)
                instance.name = name
                instance._chain_head = None
                cls._instances[name] = instance
            return cls._instances[name]


    def set_handler_chain(self, head: LogHandler):
        self._chain_head = head

    def log(self, level: LogLevel, message: str, context: dict = None):
        if not self._chain_head:
            raise RuntimeError("Logger chain not configured")
        record = LogRecord(level, message, context)
        self._chain_head.handle(record)

    def debug(self, message: str, context: dict = None):
        self.log(LogLevel.DEBUG, message, context)

    def info(self, message: str, context: dict = None):
        self.log(LogLevel.INFO, message, context)

    def warning(self, message: str, context: dict = None):
        self.log(LogLevel.WARNING, message, context)

    def error(self, message: str, context: dict = None):
        self.log(LogLevel.ERROR, message, context)

    def fatal(self, message: str, context: dict = None):
        self.log(LogLevel.FATAL, message, context)


formatter = SimpleFormatter()
console_appender = ConsoleAppender()
file_appender = FileAppender('app.log')
info_handler = LogHandler(LogLevel.INFO, formatter, console_appender)
error_handler = LogHandler(LogLevel.ERROR, formatter, file_appender)
info_handler.set_next(error_handler)
logger = Logger('app')
logger.set_handler_chain(info_handler)
logger.info('Application started')
logger.error('An error occurred', {'user': 'alice'})
