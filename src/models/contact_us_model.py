from dataclasses import dataclass

from faker import Faker

from src.models.base_model import BaseModel

fake = Faker(['en-US'])


@dataclass
class ContactUsModel(BaseModel):
    name: str
    phone: str
    email: str
    address: str
    subject: str
    message: str

    @classmethod
    def create(cls, *args, **kwargs):
        return cls(name=f'{fake.first_name()} {fake.last_name()}',
                   phone=fake.numerify('###-###-####'),
                   email=fake.ascii_safe_email(),
                   address=fake.street_address(),
                   subject=fake.sentence(),
                   message=fake.sentence())
