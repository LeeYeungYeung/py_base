import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    question = "What language did you learn to speak?"
    language_answer = AnonymousSurvey(question)
    return language_answer

def test_store_single_question(language_survey):

    language_survey.store_response("English")
    assert "English" in language_survey.responses


def test_store_three_responses(language_survey):

    responses = ['English', 'Spanish', 'French']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
