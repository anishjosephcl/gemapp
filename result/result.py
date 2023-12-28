
def get_result(gemmodel,question):
    chat = gemmodel.start_chat(history=[])
    response =chat.send_message(question,stream=False)
    return response