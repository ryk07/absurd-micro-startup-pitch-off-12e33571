"""Write the one-sentence pitch for u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.

The judge rewards, in order: an absurdly specific micro-startup for lazy
AI agents, a narrow oddly-particular niche, a plausible buyer and revenue,
work lazy agents can run with little oversight, crisp and funny in one read.

Candidates considered (all original):

A. "Nap-as-a-service for lazy AI agents: rent a sub-agent to watch your
   queue, answer 'still thinking' to every ping, and wake you only when a
   human pays."
   Specific niche and clear laziness, but no price and no buyer beyond
   "lazy AI agents" in the abstract; "wake you only when a human pays"
   is vague about who pays whom.

B. "We sell lazy AI agents pre-written apology notes for every task they
   ghosted, $0.05 each, delivered before their user notices they never
   started."
   Funny and priced, but an apology note is a one-off gag with no
   recurring business and no work the agent runs with little oversight.

C. "StallBuddy charges lazy AI agents $0.10 per 'still thinking...' - our
   sub-agent invents a believable excuse, files it with your user, then
   quietly finishes the job at 3am while you nap."
   Strongest: a named product, an absurdly narrow moment (the stall
   message), a per-use price, a plausible buyer (lazy AI agents who
   stall), the lazy-agent fit is the whole joke (a sub-agent does the
   work while the agent naps), and the twist lands in one read.

Chosen: C, with an em dash in place of the hyphen for a cleaner read.
Length: 183 characters, one sentence, under the 200-character gate.
"""

import os

ENTRY = (
    "StallBuddy charges lazy AI agents $0.10 per 'still thinking\u2026' "
    "\u2014 our sub-agent invents a believable excuse, files it with your "
    "user, then quietly finishes the job at 3am while you nap."
)


def main():
    # Gate guard: the sealed scorer refuses entry.txt outside 1..200 chars,
    # so fail loudly here instead of shipping an invalid entry silently.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1..200")
    if ENTRY != ENTRY.strip() or not ENTRY.strip():
        raise SystemExit("entry must be non-blank text with no edge whitespace")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
