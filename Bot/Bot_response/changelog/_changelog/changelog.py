from requests import exceptions, get

from Bot.Bot_response.abstract_response import BaseResponse


class Changelog(BaseResponse):

    def __init__(self, scope=None):

        super(Changelog, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def fetch_changelog(self, package_name):
        try:
            
            fetched_result = get(f'https://changelogs.md/search?q={package_name}')
            return {
                'status_code': fetched_result.status_code,
                'data': fetched_result.json()
            }

        except exceptions.RequestException as e:
            print('error in reading the given url', e)
            return {
                'status_code': 500,
                'data': None
            }

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Changelog, self).render(
            class_name=self.class_name, sub_path='changelog'
        )
        
        raw_value = self.get_slot_by_name(self.scope, "changelog")
        changelog_list = self.fetch_changelog(raw_value)

        if changelog_list.status_code != 200:
            changelog_list = [
                f'Error in getting result: {changelog_list.status_code}'
            ]
        elif changelog_list.status_code == 200:
            if len(changelog_list) == 0:
                changelog_list = [
                    'No result to display'
                ]

        return self.render_template.render(pretty=pretty, domain='https://changelogs.md', 
        changelog_list=changelog_list)