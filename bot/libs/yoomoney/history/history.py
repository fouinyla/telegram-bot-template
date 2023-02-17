from datetime import datetime
from typing import Optional
import httpx

from bot.libs.yoomoney.operation.operation import Operation


class History:
    def __init__(self,
                 base_url: str = None,
                 token: str = None,
                 method: str = None,
                 type: str = None,
                 label: str = None,
                 from_date: Optional[datetime] = None,
                 till_date: Optional[datetime] = None,
                 start_record: str = None,
                 records: int = None,
                 details: bool = None,
                 ):

        self.__private_method = method

        self.__private_base_url = base_url
        self.__private_token = token

        self.type = type
        self.label = label
        try:
            if from_date is not None:
                from_date = "{Y}-{m}-{d}T{H}:{M}:{S}".format(
                    Y=str(from_date.year),
                    m=str(from_date.month),
                    d=str(from_date.day),
                    H=str(from_date.hour),
                    M=str(from_date.minute),
                    S=str(from_date.second)
                )
        except Exception as _ex:
            raise _ex

        try:
            if till_date is not None:
                till_date = "{Y}-{m}-{d}T{H}:{M}:{S}".format(
                    Y=str(till_date.year),
                    m=str(till_date.month),
                    d=str(till_date.day),
                    H=str(till_date.hour),
                    M=str(till_date.minute),
                    S=str(till_date.second)
                )
        except Exception as _ex:
            raise _ex

        self.from_date = from_date
        self.till_date = till_date
        self.start_record = start_record
        self.records = records
        self.details = details

        data = self._request()

        if "error" in data:
            raise ValueError("[History] Oops, data error..")

        self.next_record = None
        if "next_record" in data:
            self.next_record = data["next_record"]

        self.operations = list()
        for operation_data in data["operations"]:
            param_datetime = datetime.strptime(
                str(operation_data["datetime"]).replace("T", " ").replace("Z", ""), '%Y-%m-%d %H:%M:%S'
            )
            param = {
                "operation_id": operation_data["operation_id"] if "operation_id" in operation_data else None,
                "status": operation_data["status"] if "status" in operation_data else None,
                "datetime": param_datetime if "datetime" in operation_data else None,
                "title": operation_data["title"] if "title" in operation_data else None,
                "pattern_id": operation_data["pattern_id"] if "pattern_id" in operation_data else None,
                "direction": operation_data["direction"] if "direction" in operation_data else None,
                "amount": operation_data["amount"] if "amount" in operation_data else None,
                "label": operation_data["label"] if "label" in operation_data else None,
                "type": operation_data["type"] if "type" in operation_data else None
            }

            operation = Operation(
                operation_id=param["operation_id"],
                status=param["status"],
                datetime=datetime.strptime(
                    str(param["datetime"]).replace("T", " ").replace("Z", ""), '%Y-%m-%d %H:%M:%S'
                ),
                title=param["title"],
                pattern_id=param["pattern_id"],
                direction=param["direction"],
                amount=param["amount"],
                label=param["label"],
                type=param["type"],
            )
            self.operations.append(operation)

    def _request(self):
        access_token = str(self.__private_token)
        url = self.__private_base_url + self.__private_method

        headers = {
            'Authorization': 'Bearer ' + str(access_token),
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        payload = {
            "type": None if self.type is None else self.type,
            "label": None if self.label is None else self.label,
            "from": None if self.from_date is None else self.from_date,
            "till": None if self.till_date is None else self.till_date,
            "start_record": None if self.start_record is None else self.start_record,
            "records": None if self.records is None else self.records,
            "details": None if self.details is None else self.details,
        }
        response = httpx.post(url, headers=headers, data=payload)
        return response.json()
