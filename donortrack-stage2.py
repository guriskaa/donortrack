# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: DonorTrack
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List


@dataclass
class Contact:
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    notes: str = ""

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()


@dataclass
class Gift:
    donor_id: int
    amount: float
    currency: str = "USD"
    date: date = date.today()
    campaign_id: Optional[int] = None
    receipt_number: Optional[str] = None

    def formatted_amount(self) -> str:
        return f"{self.amount:,.2f} {self.currency}"


@dataclass
class Campaign:
    title: str
    description: str = ""
    goal: Optional[float] = None
    current: float = 0.0
    start_date: date = date.today()
    end_date: Optional[date] = None
    status: str = "active"  # active, completed, paused

    def progress(self) -> float:
        if self.goal is None:
            return 0.0
        return (self.current / self.goal) * 100


@dataclass
class ThankYouNote:
    recipient_id: int
    campaign_id: Optional[int] = None
    subject: str = ""
    body: str = ""
    sent_date: date = date.today()
    template: Optional[str] = None
