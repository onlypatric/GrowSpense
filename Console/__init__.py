import subprocess as sub
from requests import session

class Winget:
    def __init__(self) -> None:
        self.session=session()
        self.last:dict={}
    def search(self,query:str,take:int=10) -> dict:
        try:
            self.last = self.session.get("https://api.winget.run/v2/packages",params={
                "query":query,
                "take":take,
                "partialMatch":"true",
                "ensureContains":"true",
            }).json()
        finally:None
        return self.last
    def generate_command(self,ins:dict) -> str:
        return "winget install -e --id {}".format(ins["Id"])