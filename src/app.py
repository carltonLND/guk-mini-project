#!/usr/bin/env python3
import os

from rich.console import Console
from rich.theme import Theme

from db import db

console = Console(
    theme=Theme(
        {"base": "#FDF1D6", "notify": "#C39E5C", "warn": "#DA723C", "error": "#EB1D36"}
    )
)
