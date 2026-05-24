# Bowling Game - A Python TDD Story

The now classic bowling game kata by Bob Martin.  This is a great kata to practice TDD and BDD.  The kata is described in detail within the [Agile Principles, Patterns, and Practices in C#][1] book and a slide deck can be found on [Bob Martin's web site][2].

## Specification

Before we write a single line of code, let's write our "specs".  What are we attempting to design?

    1) Scoring basics - 10 frames, 10 pins used for scoring, minimum score is 0 and a max is 300.
    2) Implement basic scoring - 10 frames of 2 rolls each.  Normal rolls are 1 point per pin.
    3) Strikes and spare strikes - 1 roll to knock all 10 are strikes (X), 2 rolls to knock all 10 are spares (/).
    4) Scoring strikes - If first throw, (10+a).  If spare, 10 + a.  Max 30 for first, max 20 for second.
    5) Focus on frames for scoring - score is a sum of individual frames.  Note: strikes causes frame crossover.
    6) Implement spare scoring - Spare scoring crossing frames still count for that frame.
    7) Scoring a strike - Finish implementing logic from #3.
    8) Implement scoring considering strikes - Strike scoring crossing frames still count for that frame.
    9) 10th Frame - If strike or spare is rolled, bowler gets extra ball.  This should make it 21 or less rolls.

**Table of Contents**:

* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
* [Scripts](#scripts)
* [License](#license)

## Prerequisites

* [Python 3](https://www.python.org/)
* [pip](https://pip.pypa.io/en/stable/) or [pipenv](https://pipenv.pypa.io/en/latest/)

## Getting Started

Execute the following in your terminal:

```bash
python -m venv venv
source venv/bin/activate  # for Windows, source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Scripts

The project includes BDD-style tests organized for improved readability and comprehension.  Tests live in the `specs/` directory and follow RSpec-inspired conventions: spec files are named `when_*.py`, test classes are named `Describe`, and test methods are named `should_*`.

To run the tests: `./scripts/test.sh`

To run tests with coverage: `./scripts/test-coverage.sh`

To format code: `./scripts/format.sh`

To lint: `./scripts/lint.sh`

Note: formatting and linting will occur whenever you commit code via the [pre-commit](https://pypi.org/project/pre-commit/) package.  You can also run these scripts manually to check for issues before committing. There is also configuration to run tests on pre-push in [.pre-commit-config.yaml](./.pre-commit-config.yaml) to block pushes remotely if tests fail locally.

## License

License information can be found in [LICENSE.md](./LICENSE.md)

[1]: https://www.goodreads.com/book/show/84983.Agile_Principles_Patterns_and_Practices_in_C_
[2]: http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata
