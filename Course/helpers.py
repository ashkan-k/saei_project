class COURSE_STATUS:
    DRAFT = "draft"
    PUBLISHED = "published"
    FINISHED = "finished"
    CHOICES = (
        (DRAFT, "در انتظار"),
        (PUBLISHED, "منتشر شده"),
        (FINISHED, "پایان یافته"),
    )


class CourseStatusStatusClass:
    DRAFT = "draft"
    PUBLISHED = "published"
    FINISHED = "finished"
    CHOICES = (
        (DRAFT, 'warning'),
        (PUBLISHED, 'success'),
        (FINISHED, 'danger'),
    )


class COURSE_USER_STATUS:
    ACTIVE = "active"
    DEACTIVE = "deactive"
    CHOICES = (
        (ACTIVE, "فعال"),
        (DEACTIVE, "غیرفعال"),
    )

class CourseUserStatusStatusClass:
    ACTIVE = "active"
    DEACTIVE = "deactive"
    CHOICES = (
        (ACTIVE, 'success'),
        (DEACTIVE, 'danger'),
    )
