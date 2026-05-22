from src.bowling_game import BowlingGame


class DescribeBowlingGame:
    def setup_method(self) -> None:
        self.game = BowlingGame()

    def _roll_many(self, n: int, pins: int) -> None:
        for _ in range(n):
            self.game.roll(pins)

    def _roll_spare(self) -> None:
        self.game.roll(5)
        self.game.roll(5)

    def _roll_strike(self) -> None:
        self.game.roll(10)

    def should_score_zero_for_gutter_game(self) -> None:
        self._roll_many(20, 0)
        assert self.game.score() == 0

    def should_score_twenty_for_all_ones(self) -> None:
        self._roll_many(20, 1)
        assert self.game.score() == 20

    def should_score_spare_plus_next_roll_as_bonus(self) -> None:
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(17, 0)
        assert self.game.score() == 16

    def should_score_strike_plus_next_two_rolls_as_bonus(self) -> None:
        self._roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(16, 0)
        assert self.game.score() == 24

    def should_award_extra_roll_in_tenth_frame_for_spare(self) -> None:
        self._roll_many(18, 0)
        self._roll_spare()
        self.game.roll(7)
        assert self.game.score() == 17

    def should_award_two_extra_rolls_in_tenth_frame_for_strike(self) -> None:
        self._roll_many(18, 0)
        self._roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        assert self.game.score() == 17

    def should_score_three_hundred_for_perfect_game(self) -> None:
        self._roll_many(12, 10)
        assert self.game.score() == 300
