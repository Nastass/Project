import unittest

import python_repos as pr


class PythonReposTestCase(unittest.TestCase):
    """Тестирование файла python_repos.py."""

    def setUp(self):
        """Вызов всех функций и проверка элементов по отдельности."""
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)

    def test_get_response(self):
        """Test that we get a valid response."""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        # создаем словарь для 30 хранилищ.
        self.assertEqual(len(self.repo_dicts), 30)

        # Хранилища и ключи
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())


unittest.main()
