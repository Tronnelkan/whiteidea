import uuid
from dataclasses import dataclass
import datetime

import monobank


class NotEnoughMoney:
    pass


class NotFoundPayment:
    pass


@dataclass
class Payment:
    amount: int
    comment: str

    def create_comment(self):
        self.comment = str(uuid.uuid4())

    def check_payment(self):
        mono = monobank.Client(token='uREsWIdblLfSPuPtoTpT3HXvuwtEI0In464xKkH-E4nI')
        client_statements = mono.get_statements('uKMWYopmu0DVxgK1oDqhIA', datetime.datetime(2021, 7, 17, 14),
                                                datetime.datetime.now())
        for item in client_statements:
            comment_bank = dict(item).get('comment')
            need_amount = dict(item).get('amount')
            need_amount = need_amount / 100
            if comment_bank:
                if str(self.comment) in comment_bank:
                    if float(need_amount) >= float(self.amount):
                        return True
                    else:
                        raise NotEnoughMoney
        else:
            raise NotFoundPayment

    @property
    def invoice(self):
        link = 'https://send.monobank.ua/ZYiX9yTmo?amount={amount}&text={comment}'
        return link.format(amount=self.amount, comment=self.comment)
