import unittest
from flask import request
import json
import sys
from ... import launcher

app = launcher()
class TestFlaskEndPoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.data = {
                                "id":23243,
                                "CreatedBy":9,
                                "Images":["fifty.jpg","bribe.png"],
                                "Videos":["local.mp3","footage.mp4"],
                                "comment":"Requires imediate attention",
                                "location":"90,0",
                                "status":"Pending"
                                
                             }
                            
    def test_create_new_flag(self):
        with app.test_request_context():
            response=self.app.post('/api/v1/red-flag',headers={'Content-Type': 'application/json'},data=json.dumps(self.data) )
            self.assertEqual(response.status_code,200,"Success on post should be 204")
    def test_fetching_all_flags(self):
        with app.test_request_context():
            response = self.app.get("/api/v1/red-flag")
            self.assertEqual(response.status_code, 200, "Sucessfull query returns 200")
            
    def test_get_single_flag(self):
        with app.test_request_context():
            response = self.app.get("/api/v1/red-flag/23243")
            self.assertEqual(response.status_code, 200, "Status has to be 200")
    def test_deletion(self):
        with app.test_request_context():
            response = self.app.delete("/api/v1/red-flag/23243")
            self.assertEqual(response.status_code, 200, "Status has to 200")
            
    def test_put_update(self):
        with app.test_request_context():
            response = self.app.post('/api/v1/red-flag', headers={'Content-Type': 'application/json'},data=json.dumps(self.data) )
            response = self.app.put("/api/v1/red-flag/23243",headers={'Content-Type': 'application/json'},
                            data=json.dumps({
                            "id":23243,
                            "CreatedBy":9,
                            "Images":["fifty.jpg","bribe.png"],
                            "Videos":["video.mp3","footage.mp4"],
                            "comment":"Case resolved.",
                            "location":"90,0",
                            "status":"Resolved"
                            
                         }
                        ))
            self.assertEqual(response.status_code, 200, "Status has to 200")

    def test_put_update_without_key(self):
           with app.test_request_context():
               response = self.app.post('/api/v1/red-flag', headers={'Content-Type': 'application/json'},data=json.dumps(self.data) )
               response = self.app.put("/api/v1/red-flag",headers={'Content-Type': 'application/json'},
                               data=json.dumps({
                               "id":23243,
                               "CreatedBy":9,
                               "Images":["fifty.jpg","bribe.png"],
                               "Videos":["video.mp3","footage.mp4"],
                               "comment":"Case resolved.",
                               "location":"90,0",
                               "status":"Resolved"
                               
                            }
                           ))
               json_feedback = json.loads(response.data)
               self.assertEqual(json_feedback.get("data"),"Identifier required <id>", "Should not accept update without key")
    def test_user_link(self):
        with app.test_request_context():
            response = self.app.get("/api/v1/user/keronei")
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback, "keronei", "identifier passed to URL has to be equal to returned message")
            
    def test_deletion_without_id(self):
        with app.test_request_context():
            response = self.app.delete("/api/v1/red-flag")
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback.get("data"),"Identifier required <id>", "Should not accept deletion request without id")
        
    def test_create_new_flag_with_less_params(self):
        with app.test_request_context():
            response=self.app.post('/api/v1/red-flag',headers={'Content-Type': 'application/json'}, data=json.dumps({
                            "id":23243,
                            "CreatedBy":9,
                            "Images":["fifty.jpg","bribe.png"],
                            "location":"90,0",
                            "status":"Resolved"
                            
                         } ))
            json_feedback = json.loads(response.data)
            self.assertEqual(json_feedback.get("data"),"Less params.","Less params not accepted")
