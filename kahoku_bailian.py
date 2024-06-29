# 业务空间模型调用请参考文档传入workspace信息: https://help.aliyun.com/document_detail/2746874.html    
        
import random
import dashscope
from http import HTTPStatus
from dashscope import Generation

dashscope.api_key = 'sk-eb805f041a86430ea57a755511f78184'

def generate_text(prompt):

    result = Generation.call(
        model = 'qwen1.5-110b-chat',
        prompt = prompt,
        max_tokens = 1024,
        temperature = 0.5,
        top_p = 0.7,
        # stop = ['###'],
        stream = False,
        return_full_text = False,
        return_full_chat = False,
        return_full_stream = False,
        return_full_chat_stream = False,
        return_full_chat_stream_with_history= False,
    )

    return result


if __name__ == '__main__':
    
    prompt = "请解释什么是人工智能？"
    result = generate_text(prompt)
    print(result.output.text)