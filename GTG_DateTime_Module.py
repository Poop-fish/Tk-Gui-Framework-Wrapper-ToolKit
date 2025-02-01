
class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self._validate()

    def _validate(self):
        """Validate the date."""
        if not (1 <= self.month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1 <= self.day <= 31):
            raise ValueError("Day must be between 1 and 31.")
        #* \\ Basic check for months with 30 days
        if self.month in {4, 6, 9, 11} and self.day > 30:
            raise ValueError(f"Month {self.month} only has 30 days.")
        #* \\ Check for February
        if self.month == 2:
            if self._is_leap_year() and self.day > 29:
                raise ValueError("February has only 29 days in a leap year.")
            elif not self._is_leap_year() and self.day > 28:
                raise ValueError("February has only 28 days in a non-leap year.")

    def _is_leap_year(self):
        """Check if the year is a leap year."""
        if self.year % 4 != 0:
            return False
        elif self.year % 100 != 0:
            return True
        else:
            return self.year % 400 == 0

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


class MyTime:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self._validate()

    def _validate(self):
        """Validate the time."""
        if not (0 <= self.hour < 24):
            raise ValueError("Hour must be between 0 and 23.")
        if not (0 <= self.minute < 60):
            raise ValueError("Minute must be between 0 and 59.")
        if not (0 <= self.second < 60):
            raise ValueError("Second must be between 0 and 59.")

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


class GTGDateTime:
    def __init__(self, year, month, day, hour, minute, second):
        self.date = MyDate(year, month, day)
        self.time = MyTime(hour, minute, second)

    @classmethod
    def now(cls):
        """Get the current date and time using system time."""
        from time import localtime
        now = localtime()
        return cls(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    def __str__(self):
        return f"{self.date} {self.time}"


# # Example usage
# if __name__ == "__main__":
#     # # Create a custom date and time
#     # dt = MyDateTime(2023, 10, 5, 14, 30, 45)
#     # print(dt)  # Output: 2023-10-05 14:30:45

#     # Get the current date and time
#     now = GTGDateTime.now()
#     print(now)  # Output: Current date and time in YYYY-MM-DD HH:MM:SS format
 

