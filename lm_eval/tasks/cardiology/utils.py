def doc_to_text(doc) -> str:
    answers = "".join((f"{k}. {v}\n") for k, v in doc["options"].items())
    return f"Question: {doc['question']}\n{answers}Answer:"

def doc_to_target(doc) -> str:
    return doc["answer_idx"]
