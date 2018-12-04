import unittest
from flask import request
import json
from ... import launcher
app = launcher()


class TestFlaskEndPoints(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.data = {
            'id': 23243,
            'CreatedBy': 9,
            'Images': ['fifty.jpg', 'bribe.png'],
            'Videos': ['local.mp3', 'footage.mp4'],
            'comment': 'Requires imediate attention',
            'location': '90,0',
            'status': 'Pending',
            }

    def test_create_new_flag(self):
        with app.test_request_context():
            response = self.app.post('/api/v1/red-flag',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(self.data))
            self.assertEqual(response.status_code, 200,
                             'Success on post should be 204')
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback.get('data'), 'Created',
                             "Should return 'Created' as the success message"
                             )

    def test_fetching_all_flags(self):
        with app.test_request_context():

            # first create an entry, then fetch to ascertain that the replied response is as expected

            response = self.app.post('/api/v1/red-flag',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(self.data))
            response = self.app.get('/api/v1/red-flag')
            self.assertEqual(response.status_code, 200,
                             'Sucessfull query returns 200')
            json_feedback = json.loads(response.data)
            datareceived = json_feedback.get('data')
            final_copy = json.dumps(datareceived[0])
            next_list = final_copy
            self.assertTrue(self.helper_json_checker(next_list),
                            'The returned value should be a valid JSON')

    def test_get_single_flag(self):
        with app.test_request_context():
            response = self.app.post('/api/v1/red-flag',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(self.data))
            response = self.app.get('/api/v1/red-flag/23243')
            self.assertEqual(response.status_code, 200,
                             'Status has to be 200')
            json_feedback = json.loads(response.data)
            datareceived = json_feedback.get('data')
            final_copy = json.dumps(datareceived[0])
            plain_data_sent_as_response = json.loads(final_copy)
            received_id_from_server = \
                plain_data_sent_as_response.get('id')
            self.assertEqual(23243, received_id_from_server,
                             'Posted data should match the fetched result with particular id'
                             )

    def test_deletion_of_red_flag_entry(self):
        with app.test_request_context():
            response = self.app.delete('/api/v1/red-flag/23243')
            self.assertEqual(response.status_code, 200,
                             'Status has to 200')
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback.get('data'), 'Deleted',
                             'Message should be friendly, i.e Deleted')

    def test_put_update_red_flag(self):
        with app.test_request_context():
            response = self.app.post('/api/v1/red-flag',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(self.data))
            response = self.app.put('/api/v1/red-flag/23243',
                                    headers={'Content-Type': 'application/json'
                                    }, data=json.dumps({
                'id': 23243,
                'CreatedBy': 9,
                'Images': ['fifty.jpg', 'bribe.png'],
                'Videos': ['video.mp3', 'footage.mp4'],
                'comment': 'Case resolved.',
                'location': '90,0',
                'status': 'Resolved',
                }))

            self.assertEqual(response.status_code, 200,
                             'Status has to 200')
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback.get('data'), 'Updated',
                             'Should return Updated')

    def test_put_update_without_key(self):
        with app.test_request_context():
            response = self.app.post('/api/v1/red-flag',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(self.data))
            response = self.app.put('/api/v1/red-flag',
                                    headers={'Content-Type': 'application/json'
                                    }, data=json.dumps({
                'id': 23243,
                'CreatedBy': 9,
                'Images': ['fifty.jpg', 'bribe.png'],
                'Videos': ['video.mp3', 'footage.mp4'],
                'comment': 'Case resolved.',
                'location': '90,0',
                'status': 'Resolved',
                }))
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback.get('data'),
                             'Identifier required <id>',
                             'Should not accept update without key')

    def test_user_link(self):
        with app.test_request_context():
            response = self.app.get('/api/v1/user/keronei')
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback, 'keronei',
                             'identifier passed to URL has to be equal to returned message'
                             )

    def test_red_flag_deletion_without_id(self):
        with app.test_request_context():
            response = self.app.delete('/api/v1/red-flag')
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback.get('data'),
                             'Identifier required <id>',
                             'Should not accept deletion request without id'
                             )

    def test_create_new_flag_with_less_params(self):
        with app.test_request_context():
            response = self.app.post('/api/v1/red-flag',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({
                'id': 23243,
                'CreatedBy': 9,
                'Images': ['fifty.jpg', 'bribe.png'],
                'location': '90,0',
                'status': 'Resolved',
                }))
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback.get('data'), 'Less params.',
                             'Less params not accepted')

    def helper_json_checker(self, received):
        try:
            next_list = json.loads(received)
        except ValueError:
            return False
        return True