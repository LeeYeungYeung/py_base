from survey import AnonymousSurvey


def test_store_single_question():
    question = "What language did you first learn to speak?"
    language_answer = AnonymousSurvey(question)
    language_answer.store_response("English")
    assert "English" in language_answer.responses


def test_store_three_responses():
    question = "What language did you first learn to speak?"
    language_answer = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'French']
    for response in responses:
        language_answer.store_response(response)

    for response in responses:
        assert response in language_answer.responses
