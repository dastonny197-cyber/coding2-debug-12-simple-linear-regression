"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "2a09a3b59fa34ead449707712bd2d2c6"
GRADE_HASH = "4d7f35aac38b2b57d11405a9e212ff52f2bd21eb02bcf810430600742b1e1d73"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
