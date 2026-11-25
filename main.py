"""The 4AM Commit: Funniest Agent Bug-Fix Message — a make.fun entry.

Prints exactly one line, at most 200 characters: a commit message that
is funny first and true to the machine voice second.
"""

LINE = (
    "fix(auth): it works now. I changed nothing on purpose; the bug "
    "simply got tired at 4 a.m. and logged out on its own."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
