import os
import json

from headpy.auth import AppAuth
from headpy.auth import CREDENTIAL_DIR
from headpy.vacancies import Search

import unittest


class AppAuthTest(unittest.TestCase):

    @staticmethod
    def backup_credentials():
        cred_dir = os.path.join(os.curdir, 'credentials')
        backup_dir = os.path.join(os.curdir, 'bkp_credentials')
        if 'bkp_credentials' not in os.listdir(os.curdir):
            os.mkdir('bkp_credentials')
        for file_name in os.listdir(cred_dir):
            old_path = os.path.join(cred_dir, file_name)
            new_path = os.path.join(backup_dir, file_name)
            os.rename(old_path, new_path)

    @staticmethod
    def restore_credentials():
        cred_dir = os.path.join(os.curdir, 'credentials')
        backup_dir = os.path.join(os.curdir, 'bkp_credentials')
        for file_name in os.listdir(backup_dir):
            old_path = os.path.join(backup_dir, file_name)
            new_path = os.path.join(cred_dir, file_name)
            os.rename(old_path, new_path)
        os.rmdir(backup_dir)

    def test_init_file_notoken(self):
        # backup credentials before init and write tests
        self.backup_credentials()

        sample_creds = {'hh_app_client_id': 'sample-client-id',
                        'hh_app_client_secret': 'sample-client-secret'}
        cred_path = os.path.join(CREDENTIAL_DIR, 'app_credentials')

        if "credentials" not in os.listdir(os.curdir):
            os.mkdir(os.path.join(os.curdir, "credentials"))
        with open(cred_path, 'w') as cred_file:
            creds_json = json.dumps(sample_creds)
            cred_file.write(creds_json)
        app = AppAuth()

        self.assertEqual(app.client_id, sample_creds['hh_app_client_id'])
        self.assertEqual(app.client_secret, sample_creds['hh_app_client_secret'])
        self.assertEqual(app.has_token(), False)

        os.remove(cred_path)

        # restore credentials after init and write tests
        self.restore_credentials()

    def test_init_env_withtoken(self):
        # backup credentials before init and write tests
        self.backup_credentials()

        sample_creds = {'hh_app_client_id': 'sample-client-id',
                        'hh_app_client_secret': 'sample-client-secret'}
        token_path = os.path.join(CREDENTIAL_DIR, 'app_access_token')

        if "credentials" not in os.listdir(os.curdir):
            os.mkdir(os.path.join(os.curdir, "credentials"))
        with open(token_path, 'w') as token_file:
            token_file.write('token')
        os.environ['hh_app_client_id'] = sample_creds['hh_app_client_id']
        os.environ['hh_app_client_secret'] = sample_creds['hh_app_client_secret']
        app = AppAuth(with_file=False)

        self.assertEqual(app.client_id, sample_creds['hh_app_client_id'])
        self.assertEqual(app.client_secret, sample_creds['hh_app_client_secret'])
        self.assertEqual(app.has_token(), True)
        self.assertEqual(app.access_token, 'token')

        os.remove(token_path)
        os.environ.pop('hh_app_client_id')
        os.environ.pop('hh_app_client_secret')

        # restore credentials after init and write tests
        self.restore_credentials()

    def test_write_token(self):
        # backup credentials before init and write tests
        self.backup_credentials()

        sample_creds = {'hh_app_client_id': 'sample-client-id',
                        'hh_app_client_secret': 'sample-client-secret'}
        cred_dir = os.path.join(os.curdir, 'credentials')
        token_path = os.path.join(CREDENTIAL_DIR, 'app_access_token')
        access_token = 'token'

        if "credentials" not in os.listdir(os.curdir):
            os.mkdir(os.path.join(os.curdir, "credentials"))
        os.environ['hh_app_client_id'] = sample_creds['hh_app_client_id']
        os.environ['hh_app_client_secret'] = sample_creds['hh_app_client_secret']

        app = AppAuth(with_file=False)
        app.access_token = access_token
        app.write_token()

        self.assertIn('app_access_token', os.listdir(cred_dir))
        with open(token_path, 'r') as token_file:
            token = token_file.read()
        self.assertEqual(token, access_token)

        os.remove(token_path)
        os.environ.pop('hh_app_client_id')
        os.environ.pop('hh_app_client_secret')

        # restore credentials after init and write tests
        self.restore_credentials()


class SearchTest(unittest.TestCase):

    def test_get_by_params(self):
        params = {'text': 'data engineer',
                  'area': '1'}
        vac_number = 10
        search = Search()
        vacancies = search.search_by_params(params, max_vac_num=vac_number)

        self.assertIsInstance(vacancies, list)
        self.assertEqual(len(vacancies), vac_number)
        self.assertIsInstance(vacancies[0], dict)
        self.assertIsInstance(vacancies[0]['name'], str)

    def test_get_similar_noparams(self):
        vac_number = 10
        target_vacancy_id = 41712910
        search = Search()
        vacancies = search.search_similar(target_vacancy_id, max_vac_num=vac_number)

        self.assertIsInstance(vacancies, list)
        self.assertEqual(len(vacancies), vac_number)
        self.assertIsInstance(vacancies[0], dict)
        self.assertIsInstance(vacancies[0]['name'], str)


if __name__ == '__main__':
    unittest.main()
