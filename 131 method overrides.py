# A child class replaces a method from its parent.

# Example: Alert Severity


# class Alert:
#     def notify(self):
#         print("Generic alert")


# class CriticalAlert(Alert):
#     def notify(self):
#         print("CRITICAL: Security breach detected!")


# Usage:

# alert = CriticalAlert()
# alert.notify()


# Access Parent Method with super()


class Alert:
    def notify(self):
        print("Logging alert")


class CriticalAlert(Alert):
    def notify(self):
        super().notify()
        print("Sending SMS to SOC team")


alert = CriticalAlert()
alert.notify()
