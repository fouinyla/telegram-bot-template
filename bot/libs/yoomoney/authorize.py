import httpx


class Authorize:
    def __init__(self, client_id: str, redirect_url: str):
        self.client_id = client_id
        self.redirect_url = redirect_url

        self._base_url = "https://yoomoney.ru"
        self._headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self.scope = [
             "account-info",
             "operation-history",
             "operation-details",
             "incoming-transfers",
             "payment-p2p",
             "payment-shop"
        ]

    async def auth_session_code(self) -> str:
        url = f"{self._base_url}/oauth/authorize?" \
                    f"client_id={self.client_id}&" \
                    f"response_type=code&" \
                    f"redirect_uri={self.redirect_url}&" \
                    f"scope={'%20'.join([str(elem) for elem in self.scope])}"
        async with httpx.AsyncClient() as session:
            response = await session.post(url=url, headers=self._headers)
            return response.text.split(" ")[3]

    async def get_yoomoney_token(self, code: str):
        try:
            code = code[code.index("code=") + 5:].replace(" ", "")
        except Exception as _ex:
            raise ValueError("Input code error:", _ex)

        url = f"{self._base_url}/oauth/token?" \
              f"code={code}&client_id={self.client_id}&" \
              f"grant_type=authorization_code&" \
              f"redirect_uri={self.redirect_url}"

        async with httpx.AsyncClient() as session:
            response = await session.post(url, headers=self._headers)
        if "error" in response.json() or response.json()["access_token"] == "":
            raise ValueError("Oops, sever error")
        return response.json()['access_token']
