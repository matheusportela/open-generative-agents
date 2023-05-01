from engine.large_language_model import EchoLLM


def test_language_model_can_complete_text():
    language_model = EchoLLM()
    prompt = 'The quick brown fox jumps over the lazy dog.'
    completion = language_model.complete(prompt)
    assert completion == 'The quick brown fox jumps over the lazy dog.'
