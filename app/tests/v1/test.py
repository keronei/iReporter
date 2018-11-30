import unittest
from flask import request
import json
import sys
from ... import launcher

app = launcher()
class TestFlaskEndPoints(unittest.TestCase):
    def test_create_new_flag(self):
        self.app = app.test_client()
        response=self.app.post('/api/v1/red-flag', 
                       data=json.dumps({
                        "id":23243,
                        "CreatedBy":9,
                        "Images":["fifty.jpg","bribe.png"],
                        "Videos":["local.mp3","footage.mp4"],
                        "comment":"Requires imediate attention",
                        "location":"90,0",
                        "status":"Pending"
                        
                     }
                    ),
                       content_type='application/json')
        self.assertEqual(response.status_code,204,"Success on post should be 204")
        
        
    def test_fetching_all_flags(self):
        self.app = app.test_client()
        response = self.app.get("/api/v1/red-flag")
        self.assertEqual(response.status_code, 200, "Sucessfull query returns 200")
        
    def test_get_single_flag(self):
        self.app = app.test_client()
        response = self.app.get("/api/v1/red-flag/23243")
        self.assertEqual(response.status_code, 200, "Status has to be 200")
    def test_deletion(self):
        self.app = app.test_client()
        response = self.app.delete("/api/v1/red-flag/23243")
        self.assertEqual(response.status_code, 200, "Status has to 200")
    def test_put_update(self):
        self.app = app.test_client()
        response=self.app.post('/api/v1/red-flag', 
                       data=json.dumps({
                        "id":23243,
                        "CreatedBy":9,
                        "Images":["fifty.jpg","bribe.png"],
                        "Videos":["video.mp3","footage.mp4"],
                        "comment":"Case observed more than once",
                        "location":"90,0",
                        "status":"Pending"
                        
                     }
                    ),
                       content_type='application/json')
        response = self.app.put("/api/v1/red-flag/23243",
                        data=json.dumps({
                        "id":23243,
                        "CreatedBy":9,
                        "Images":["fifty.jpg","bribe.png"],
                        "Videos":["video.mp3","footage.mp4"],
                        "comment":"Case resolved.",
                        "location":"90,0",
                        "status":"Resolved"
                        
                     }
                    ),
                       content_type='application/json')
        self.assertEqual(response.status_code, 200, "Status has to 200")
        
        
        
    
if __name__ == '__main__':
    unittest.main()