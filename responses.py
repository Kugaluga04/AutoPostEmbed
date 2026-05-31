def get_response(user_input: str) -> str:
    
    if "/twitter.com/" in user_input:
        send_vid = user_input.replace("/twitter.com", "/vxtwitter.com")
        return send_vid
    
    if "/x.com/" in user_input:
        send_vid = user_input.replace("/x.com", "/vxtwitter.com")
        return send_vid
    
    if "/vxtwitter.com/" in user_input:
        send_vid = user_input
        return send_vid
    
    if "/instagram.com/" in user_input:
        send_vid = user_input.replace("/instagram.com", "/kkinstagram.com")
        return send_vid
    
    if "/www.instagram.com/" in user_input:
        send_vid = user_input.replace("/www.instagram.com", "/kkinstagram.com")
        return send_vid
    
    if "/kkinstagram.com/" in user_input:
        send_vid = user_input
        return send_vid
    
    if "/www.kkinstagram.com/" in user_input:
        send_vid = user_input
        return send_vid