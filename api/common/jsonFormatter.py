import datetime
from datetime import datetime, timedelta, timezone
from pythonjsonlogger import jsonlogger


class JsonFormatter(jsonlogger.JsonFormatter):

    def parse(self):

        log_list = [
            'timestamp',
            'level',
            'name',
            'message'
        ]

        return log_list

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)

        if not log_record.get('timestamp'):
            jst = timezone(timedelta(hours=+9), 'JST')
            now = datetime.now(jst).strftime('%Y-%m-%dT%H:%M:%S%z')
            log_record['timestamp'] = now

        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname
