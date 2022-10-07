class REPORT_CARD_TYPE:
    TTC = "ttc"
    MOCK = "mock"
    TERM = "term"
    CHOICES = (
        (TTC, "TTC"),
        (MOCK, "MOCK"),
        (TERM, "ترمی"),
    )


class EXAM_STATUS:
    PASS = "pass"
    CP = "cp"
    FAIL = "fail"
    CHOICES = (
        (PASS, "PASS"),
        (CP, ".C.P"),
        (FAIL, "FAIL"),
    )
