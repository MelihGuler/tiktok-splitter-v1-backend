
import json
        
def test_split_tiktok_video(client):
    response = client.post("/api/video/split/tiktok", data=json.dumps(dict(video_url='https://www.tiktok.com/@hakanyagar98/video/7329585731750432006', part_length=5)),
                       content_type='application/json')
    
    assert response.status_code == 200
    assert response.content_type == 'application/zip'
        
def test_split_tiktok_video_should_return_400(client):
    response = client.post("/api/video/split/tiktok", data=json.dumps(dict(video_url='abc', part_length=5)),
                       content_type='application/json')
    
    assert response.status_code == 400
