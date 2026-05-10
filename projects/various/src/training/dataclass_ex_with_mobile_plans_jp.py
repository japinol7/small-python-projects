from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from enum import StrEnum, auto
from pprint import pp


class PhoneBrand(StrEnum):
    APPLE = auto()
    SAMSUNG = auto()
    SONY = auto()


@dataclass
class Address:
    country: str
    province: str
    postal_code: str
    city: str
    street: str
    house_num: int | str


@dataclass
class Customer:
    name: str
    address: Address
    email: str


@dataclass(frozen=True)
class Phone:
    brand: PhoneBrand
    model: str
    serial_number: str
    price: Decimal

    def __hash__(self) -> int:
        return hash(self.serial_number)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Phone):
            raise NotImplementedError
        return self.serial_number == other.serial_number


@dataclass
class Plan:
    customer: Customer
    duration_in_months: int
    price_per_month: Decimal
    date_start: date = field(default_factory=date.today)
    phone: Phone | None = None


def main() -> None:
    customer_address = Address(
        country="USA",
        province="NY",
        postal_code="10001",
        city="New York",
        street="W 31st St",
        house_num=350,
        )

    customer = Customer(
        name="John Doe",
        address=customer_address,
        email="john.doe@dummy.invalid",
        )

    iphone = Phone(
        brand=PhoneBrand.APPLE,
        model="iPhone 16",
        serial_number="784-8921",
        price=Decimal("899.99"),
        )

    # Create mobile plan
    premium_plan = Plan(
        customer=customer,
        duration_in_months=12,
        price_per_month=Decimal("34.99"),
        date_start=date(2026, 5, 1),
        phone=iphone,
        )

    # Create another plan without a phone
    basic_plan = Plan(
        customer=customer,
        duration_in_months=6,
        price_per_month=Decimal("19.99"),
        )

    # Display objects
    print("=== Customer ===")
    pp(customer)

    print("\n=== Phone ===")
    pp(iphone)

    print("\n=== Premium plan ===")
    pp(premium_plan)

    print("\n=== Basic plan ===")
    pp(basic_plan)

    # Demonstrate frozen dataclass equality/hash behavior
    same_iphone = Phone(
        brand=PhoneBrand.APPLE,
        model="iPhone 16 Pro",
        serial_number="784-8921",
        price=Decimal("1299.99"),
        )

    print("\n=== Phone comparison - dataclass equality/hash behavior ===")
    print(f"iphone == same_iphone: {iphone == same_iphone}")

    phone_inventory = {iphone, same_iphone}
    print("After adding the two same phones to the phone_inventory "
          "set, this is its content: ")
    pp(phone_inventory)

    print(f"Unique phones in inventory: {len(phone_inventory)}")
    assert len(phone_inventory) == 1


if __name__ == "__main__":
    main()
