import datetime
import random

"""
    I will use this class to the scheduling stuff
"""


class Scheduler:

    @staticmethod
    def review(
        review_date: str, a_factor, interval, punctuation: int = 1
    ) -> tuple[int, str]:
        """
        Get the next date knowing:
            - Review date
            - A-Factor
            - Interval
            - Punctuation:
                - 0 will serve to start over the schedulling (return
                  to the first interval). This will be a period between 1
                  and 3 days.
                - 1 will serve to work normally (just multiply the
                  interval * a_factor, as a good response in spaced repetion)
        Returns:
            - Interval to next review
            - Due date
        """
        if punctuation == 0:
            new_interval = random.choice([1, 2, 3])
        elif punctuation == 1:
            new_interval = round(a_factor * interval)
        # Using time delta
        interval_td = datetime.timedelta(new_interval)
        last_date = datetime.date.fromisoformat(review_date)
        new_date = (last_date + interval_td).isoformat()
        return (new_interval, new_date)

    # TODO: when creating the next object, remember to first declare
    # the due_date the same as the review_date, just to avoid problems.
    # Or maybe set as today that date.

    @staticmethod
    def new_date_material(interval: int = 1) -> str:
        tomorrow = datetime.date.today() + datetime.timedelta(interval)
        due_date = tomorrow.isoformat()
        return due_date

    @staticmethod
    def new_date_extract() -> tuple[int, str]:
        date_today = datetime.date.today().isoformat()
        return Scheduler.review(date_today, 1.0, 1, 0)

    # TODO: When posponing, remember first to set everything else.
    # Here we are only returning the next due_date.
    @staticmethod
    def pospone(how_much_days: int = 1) -> str:
        new_date = datetime.date.today() + datetime.timedelta(how_much_days)
        due_date = new_date.isoformat()
        return due_date
