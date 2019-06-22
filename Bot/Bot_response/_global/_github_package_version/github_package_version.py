from requests import exceptions, get

from Bot.Bot_response.abstract_response import BaseResponse


class Github_package_version(BaseResponse):

    def __init__(self, scope=None):

        super(Github_package_version, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def check_for_updates(self, package_name, patch_type=''):
        try:

            url = f'https://verse.pawelad.xyz/projects/{package_name}/{patch_type}'
            fetched_result = get(url)

            return {
                'status_code': fetched_result.status_code,
                'data': fetched_result.json() if fetched_result.status_code == 200  else {
                    'error': 'error in searching of given package'
                },
                'package_name': package_name
            }
        except exceptions.RequestException as e:
            return {
                'status_code': 500,
                'data': None,
                'package_name': package_name

            }

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Github_package_version, self).render(
            class_name=self.class_name, sub_path='_global'
        )

        package_name = super().get_slot_by_name('package_name')
        patch_type = super().get_slot_by_name('checkVersion')
        github = self.check_for_updates(package_name, patch_type)

        return self.render_template.render(pretty=pretty, github=github)