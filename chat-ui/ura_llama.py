import json
import requests


def run(str_prompt):
    print(f"Prompt:\n{str_prompt}")
    print(f"Prompt length: {len(str_prompt.split())}")
    print("="*100)
    # 1. Setting parameters for the POST request
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2xvZ2luIjoiYW5odHUxMnN0In0.2qZ2eDUKir9wUhzciEDQXouPXm7I8cggIfPbOV9FfO8"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    url = 'https://www.ura.hcmut.edu.vn/ura-llama/generate'

    data = {
        "inputs": str_prompt,
        "parameters": {
            "temperature": 0.001,
            "top_p": 0.90,
            "repetition_penalty": 1.2,
            "top_k": 10,
            "truncate": 1022,
            "max_new_tokens": 1024,
            "stop": ["<|endoftext|>", "</s>", "[INST]", "[INST"]
        }
    }
    json_data = json.dumps(data)

    response = requests.post(url, headers=headers, data=json_data, timeout=100)
    response.raise_for_status()
    return response.json().get("generated_text")


if "__main__" == __name__:
    prompt_input = """[INST] <<SYS>>Bạn là một trợ lý hữu ích, tôn trọng và trung thực. Bạn sẽ trích xuất câu trả lời từ trong văn bản được cung cấp để trả lời câu hỏi của người dùng. Câu trả lời của bạn không được bao gồm bất kỳ nội dung có hại, phi đạo đức, phân biệt chủng tộc, phân biệt giới tính, độc hại, nguy hiểm hoặc bất hợp pháp.

Bạn hãy là theo thứ tự hướng dẫn sau:
1. Đọc hiểu và trích suất các từ khoá trong câu hỏi.
2. Đọc hiểu văn bản và chú ý đến các từ khoá liên quan đến câu hỏi.
3. Tìm câu trả lời trong văn bản.
4. Kiểm tra câu trả lời phải đầy đủ và ngắn gọn và có trong văn bản.
5. Xoá những thông tin không có trong văn bản.
6. Nếu không có câu trả lời hay đọc lại văn bản và hỏi người dùng câu hỏi để người dùng trả lời.<</SYS>>

Ngữ cảnh:
Lệ phí 200.000 đồng/hộ chiếu, trường hợp cấp lại do bị hỏng hoặc bị mất 400.000 đồng/hộ chiếu
Thời gian tiếp nhận hồ sơ và trả kết quả Từ Thứ 2 đến sáng Thứ 7 hàng tuần, trừ các ngày nghỉ, lễ, Tết theo quy định.

Câu hỏi: Làm hộ chiếu bao nhiêu tiền?
Từ khoá: hộ chiếu, tiền.[/INST]
Câu trả lời: 200.000 đồng/hộ chiếu, trường hợp cấp lại do bị hỏng hoặc bị mất 400.000 đồng/hộ chiếu.

[INST] Ngữ cảnh:
Thời hạn giải quyết 08 ngày làm việc (64 giờ làm việc), kể từ ngày nhận đầy đủ hồ sơ theo quy định.
Thời gian tiếp nhận hồ sơ và trả kết quả Từ Thứ 2 đến sáng Thứ 7 hàng tuần, trừ các ngày nghỉ, lễ, Tết theo quy định.

Câu hỏi: Khi nào tôi có thể nộp hồ sơ?
Từ khoá: Khi nào, nộp, hồ sơ.[/INST]
Câu trả lời: Thời gian tiếp nhận hồ sơ và trả kết quả Từ Thứ 2 đến sáng Thứ 7 hàng tuần.

[INST] Ngữ cảnh:
Ông ABC là phó tổng giám đốc thứ nhất.
ông Lê Việt Dũng là phó tổng giám đốc - chánh kỹ sư.
Ông Phạm Xuân Sơn là Phó Tổng Giám đốc.
ông Vũ Mai Khanh là tổng giám đốc.
Ông Phan Anh Tú là siêu nhân.
ông DEF là phó tổng giám đốc.

Câu hỏi: Ai là tổng giám đốc?
Từ khoá: [INST]"""
    print(run(prompt_input))
