
import json
        
def test_get_tiktok_video(client):
    response = client.post("/api/video/tiktok", data=json.dumps(dict(video_url='https://www.tiktok.com/@hakanyagar98/video/7329585731750432006')),
                       content_type='application/json')
    
    assert response.status_code == 200
    assert response.content_type == 'video/mp4'
    
def test_get_tiktok_video_should_return_400(client):
    response = client.post("/api/video/tiktok", data=json.dumps(dict(video_url='abc')),
                       content_type='application/json')
    
    assert response.status_code == 400

    