from aiogram.fsm.state import State, StatesGroup


class JobBlank(StatesGroup):
    """
    There states for job-blank registration
    """
    start = State()
    full_name = State()
    age = State()
    technologies = State()
    tg_profile = State()
    phone = State()
    province = State()
    price = State()
    profession = State()
    time_to_apply = State()
    goal = State()
    save_or_edit = State()
