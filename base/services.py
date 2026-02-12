from base.models import Shedule


def create_shedule(user,title,description,priority)->bool:
    if user is None or title is None:
        return False
    
    shedule = Shedule(
        user = user,
        title = title,
        description = description,
        priority = priority
    )

    shedule.save()


