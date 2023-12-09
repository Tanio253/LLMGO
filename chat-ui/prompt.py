from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma

from vector_database import embedding

examples = [
    {
        "context": "Ông A là chủ tịch.\nÔng B là tổng giám đốc.\nÔng C là phó giám đốc thứ nhất.\nD là phó giám đốc.",
        "question": "Ai là tổng giám đốc?",
        "answer": "Ông A."
    },
    {
        "context": "Ông A là chủ tịch.\nÔng B là tổng giám đốc.\nÔng C là phó giám đốc thứ nhất.\nD là phó giám đốc.",
        "question": "Ai là phó giám đốc?",
        "answer": "Ông C và D."
    },
    {
        "context": "A được thành lập vào năm 1969 tới năm 2001.\nB mua lại A vào năm 1988.",
        "question": "Công ty A đóng cửa vào năm nào?",
        "answer": "2001."
    },
    {
        "context": "A được thành lập vào năm 1969 tới năm 2001.\nB mua lại A vào năm 1988.",
        "question": "Công ty A được thành lập vào năm nào?",
        "answer": "1969."
    },
    {
        "context": "A được thành lập vào năm 1969 tới năm 2001.\nB mua lại A vào năm 1988.",
        "question": "Ai đã mua lại A?",
        "answer": "B."
    },
]

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    embedding,
    Chroma,
    k=2,
    collection_name='example',
)

def get_examples(question):
    selected_examples = example_selector.select_examples({"question": question})
    prompt = FewShotPromptTemplate(
        examples=selected_examples,
        example_prompt=PromptTemplate(input_variables=["context", "question", "answer"], template="[INST]Văn bản: {context}\n\nCâu hỏi: {question}\nCâu trả lời: [\INST]{answer}"),
        suffix="",
        input_variables=[]
    )
    return prompt.format()

# Đơn giản, đúng mục đích
PROMPT_TEMPLATE = PromptTemplate.from_template(
"""[INST] <<SYS>>Bạn là một trợ lý hữu ích, tôn trọng và trung thực. Bạn sẽ trích xuất câu trả lời từ trong văn bản được cung cấp để trả lời câu hỏi của người dùng. Câu trả lời của bạn không được bao gồm bất kỳ nội dung có hại, phi đạo đức, phân biệt chủng tộc, phân biệt giới tính, độc hại, nguy hiểm hoặc bất hợp pháp.

Bạn hãy là theo thứ tự hướng dẫn sau:
1. Đọc hiểu và trích suất các từ khoá trong câu hỏi.
2. Đọc hiểu văn bản và chú ý đến các từ khoá liên quan đến câu hỏi.
3. Tìm câu trả lời trong văn bản.
4. Kiểm tra câu trả lời phải đầy đủ, ngắn gọn, có trong văn bản và đúng mục đích.
5. Xoá những thông tin không có trong văn bản.
6. Nếu không có câu trả lời hay đọc lại văn bản và hỏi người dùng câu hỏi để người dùng trả lời.<</SYS>>

Văn bản:
    Ông A là tổng giám đốc.
    Ông B là phó tổng giảm đốc.

Câu hỏi: Ai là phó tổng giám đốc?
Câu trả lời: [/INST]Ông B.

{examples}

[INST]Ngữ cảnh:
{context}

Câu hỏi: {question}
Câu trả lời: [/INST]
""")