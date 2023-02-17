import httpx


class Quickpay:
    def __init__(self,
                 receiver: str,
                 quickpay_form : str,
                 targets: str,
                 paymentType: str,
                 sum: float,
                 formcomment: str = None,
                 short_dest: str = None,
                 label: str = None,
                 comment: str = None,
                 successURL: str = None,
                 need_fio: bool = None,
                 need_email: bool = None,
                 need_phone: bool = None,
                 need_address: bool = None,
                 ):
        self.receiver = receiver
        self.quickpay_form = quickpay_form
        self.targets = targets
        self.paymentType = paymentType
        self.sum = sum
        self.formcomment = formcomment
        self.short_dest = short_dest
        self.label = label
        self.comment = comment
        self.successURL = successURL
        self.need_fio = need_fio
        self.need_email = need_email
        self.need_phone = need_phone
        self.need_address = need_address

        self.response = self._request()

    def _request(self):
        self.base_url = "https://yoomoney.ru/quickpay/confirm.xml?"
        payload = {
            "receiver": self.receiver,
            "quickpay_form": self.quickpay_form,
            "targets": self.targets,
            "paymentType": self.paymentType,
            "sum": self.sum,
            "formcomment": None if self.formcomment is None else self.formcomment,
            "short_dest": None if self.short_dest is None else self.short_dest,
            "label": None if self.label is None else self.label,
            "comment": None if self.comment is None else self.comment,
            "successURL": None if self.successURL is None else self.successURL,
            "need_fio": None if self.need_fio is None else self.need_fio,
            "need_email": None if self.need_email is None else self.need_email,
            "need_phone": None if self.need_phone is None else self.need_phone,
            "need_address": None if self.need_address is None else self.need_address
        }
        for key, value in payload.items():
            if value is not None:
                self.base_url += key.replace("_", "-") + "=" + str(value)
                self.base_url += "&"
        self.base_url = self.base_url[:-1].replace(" ", "%20")

        response = httpx.request("POST", self.base_url)
        self.redirected_url = response.url
        return response


# from httpx import AsyncClient, Response
# import asyncio
#
#
# class Quickpay:
#     def __init__(self,
#                  receiver: str,
#                  quickpay_form: str,
#                  targets: str,
#                  paymentType: str,
#                  summa: float,
#                  formcomment: str = None,
#                  short_dest: str = None,
#                  label: str = None,
#                  comment: str = None,
#                  successURL: str = None,
#                  need_fio: bool = None,
#                  need_email: bool = None,
#                  need_phone: bool = None,
#                  need_address: bool = None
#                  ):
#         self.receiver = receiver
#         self.quickpay_form = quickpay_form
#         self.targets = targets
#         self.paymentType = paymentType
#         self.summa = summa
#         self.formcomment = formcomment
#         self.short_dest = short_dest
#         self.label = label
#         self.comment = comment
#         self.successURL = successURL
#         self.need_fio = need_fio
#         self.need_email = need_email
#         self.need_phone = need_phone
#         self.need_address = need_address
#         self.payload = {
#             "receiver": self.receiver,
#             "quickpay_form": self.quickpay_form,
#             "targets": self.targets,
#             "paymentType": self.paymentType,
#             "sum": self.summa,
#             "formcomment": None if self.formcomment is None else self.formcomment,
#             "short_dest": None if self.short_dest is None else self.short_dest,
#             "label": None if self.label is None else self.label,
#             "comment": None if self.comment is None else self.comment,
#             "successURL": None if self.successURL is None else self.successURL,
#             "need_fio": None if self.need_fio is None else self.need_fio,
#             "need_email": None if self.need_email is None else self.need_email,
#             "need_phone": None if self.need_phone is None else self.need_phone,
#             "need_address": None if self.need_address is None else self.need_address
#         }
#
#     async def set_not_null_params(self):
#         self.base_url = "https://yoomoney.ru/quickpay/confirm.xml?"
#         for key, value in self.payload.items():
#             if value is not None:
#                 self.base_url += key.replace("_", "-") + "=" + str(value)
#                 self.base_url += "&"
#         self.base_url = self.base_url[:-1].replace(" ", "%20")
#
#     async def quickpay_request(self) -> Response:
#         task = asyncio.create_task(coro=self.set_not_null_params())
#         await task
#         async with AsyncClient() as session:
#             response = await session.post(self.base_url)
#             self.redirected_url = response.url
#             return response
