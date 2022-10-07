class TicketStatus:
    ANSWERED = "answered"
    CLOSE = "close"
    WAITING = "waiting"
    CHOICES = (
        (ANSWERED, "پاسخ داده شده"),
        (CLOSE, "بسته"),
        (WAITING, "در انتظار"),
    )


class TicketStatusClass:
    ANSWERED = "answered"
    CLOSE = "close"
    WAITING = "waiting"
    CHOICES = (
        (ANSWERED, 'success'),
        (CLOSE, 'danger'),
        (WAITING, 'warning'),
    )
