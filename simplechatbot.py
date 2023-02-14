import random

# Khai báo một số từ vựng cần thiết
greeting_keywords = ("xin chào", "chào", "hi", "hello")
greeting_responses = ["xin chào", "chào bạn", "hi", "hello"]

def check_for_greeting(sentence):
    """Kiểm tra xem câu trả lời có chứa các từ chào hỏi hay không"""
    for word in sentence.split():
        if word.lower() in greeting_keywords:
            return True
    return False

def greet(sentence):
    """Trả lời các câu chào hỏi"""
    return random.choice(greeting_responses) + "."

def respond(sentence):
    """Xử lý các câu trả lời của người dùng"""
    if check_for_greeting(sentence):
        return greet(sentence)
    else:
        return "Tôi không hiểu ý của bạn. Vui lòng cho tôi biết nội dung cần hỗ trợ."

# Sử dụng vòng lặp để giữ liên lạc với người dùng
while True:
    user_input = input("Người dùng: ")
    print("Chatbot: ", respond(user_input))
