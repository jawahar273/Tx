from os import getenv

from plyer import notification

from Bot.Bot_response.abstract_response import BaseResponse
from config.stage import db


class Reminder(BaseResponse):

    def __init__(self, scope=None):

        super(Reminder, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Reminder, self).render(
            class_name=self.class_name, sub_path='_cron'
        )
        # if (getenv('TARGET_PLATFORM') != 'web'):

        #     notification.notify('setting reminder')

        intended_time_set = set(['form now on', 'from now', 'after', 'before'])

        countdown = self.get_slot_by_name('countdown')
        when = self.get_slot_by_name('when')
        message = self.get_slot_by_name('message')
        intended_time = self.get_slot_by_name('intendedTime')
        # huey https://huey.readthedocs.io/en/latest/guide.html

        print('countdown:', countdown, ',mes:', message, ',inttime:', self.get_slot_by_name('intendedTime'), ',when:', when,)
        if countdown and not when and not intended_time or countdown and intended_time:
            # start the count down right now.

            # passing to schedular
            from .scheduler import main
            main(countdown)

        return self.render_template.render(pretty=pretty)