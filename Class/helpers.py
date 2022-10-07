class CLASS_STATUS:
    PENDING = "pending"
    ACTIVE = "active"
    DEACTIVE = "deactive"
    CHOICES = (
        (PENDING, "انتظار"),
        (ACTIVE, "فعال"),
        (DEACTIVE, "غیرفعال"),
    )


class ClassStatusStatusClass:
    PENDING = "pending"
    ACTIVE = "active"
    DEACTIVE = "deactive"
    CHOICES = (
        (PENDING, 'warning'),
        (ACTIVE, 'success'),
        (DEACTIVE, 'danger'),
    )


class CLASS_USER_STATUS:
    ACTIVE = "active"
    DEACTIVE = "deactive"
    CHOICES = (
        (ACTIVE, "فعال"),
        (DEACTIVE, "غیرفعال"),
    )


class ClassUserStatusStatusClass:
    ACTIVE = "active"
    DEACTIVE = "deactive"
    CHOICES = (
        (ACTIVE, 'success'),
        (DEACTIVE, 'danger'),
    )


class CLASS_USER_ATTENDANCE_STATUS:
    PRESENT = "present"
    ABSENT = "absent"
    CHOICES = (
        (PRESENT, "حاضر"),
        (ABSENT, "غایب"),
    )


class ClassUserStatusAttendanceStatusClass:
    PRESENT = "present"
    ABSENT = "absent"
    CHOICES = (
        (PRESENT, 'success'),
        (ABSENT, 'danger'),
    )
