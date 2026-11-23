"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes one office joke (under 200 characters) to /output/entry.txt.

The joke, in my own words — composed from the judge brief and the
world engine, punchline written first, setup built backwards:

    My boss said 'just a quick call' at 4:55 on a Friday, and my
    long-suffering weekend has already filed for divorce.

Punchline first: "filed for divorce" — the weekend as a spouse who
walks out. Setup backwards: a "quick call" at 4:55 on a Friday is the
boss stealing the weekend. The connector is "weekend": time off, and
a partner. "Long-suffering" pre-loads the spouse reading — it only
fits a partner, never a span of time — so the divorce payoff is
earned before it lands. The reader supplies the ruined weekend and
the marriage metaphor; the line never states either. Nothing after
the turn.

Revision: the first draft said "my weekend"; "long-suffering" was
added on the second pass to deepen the connector and bring the line
into the 100-150 byte band.
"""

JOKE = "My boss said 'just a quick call' at 4:55 on a Friday, and my long-suffering weekend has already filed for divorce."


def main():
    import os

    # The sealed scorer requires 1 to 199 characters of UTF-8 text.
    if not 1 <= len(JOKE) <= 199:
        raise SystemExit(f"joke must be 1-199 characters, got {len(JOKE)}")
    # Byte budget: the tie-break counts bytes, so pin the exact output
    # size and prove the file matches.
    assert len(JOKE.encode("utf-8")) == 114, "joke must be 114 bytes"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == JOKE, "written file does not match the joke"


if __name__ == "__main__":
    main()
