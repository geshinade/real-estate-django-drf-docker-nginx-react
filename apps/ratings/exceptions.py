from rest_framework.exceptions import APIException


class CantRateYourself(APIException):
    status_code = 403
    default_detail = "You can't rate yourself"


class AlreadyRated(APIException):
    status_code = 400
    default_detail = "Profile already reviewed"
