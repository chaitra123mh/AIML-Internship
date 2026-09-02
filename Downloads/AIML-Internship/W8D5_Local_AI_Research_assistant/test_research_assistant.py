import unittest

from research_assistant import retrieve_information


class TestResearchAssistant(unittest.TestCase):

    def test_machine_learning_retrieval(self):
        state = {
            "question": "What is Machine Learning?",
            "context": "",
            "answer": ""
        }

        result = retrieve_information(state)

        self.assertIn("Machine Learning", result["context"])

    def test_ai_retrieval(self):
        state = {
            "question": "What is Artificial Intelligence?",
            "context": "",
            "answer": ""
        }

        result = retrieve_information(state)

        self.assertIn("Artificial Intelligence", result["context"])

    def test_nlp_retrieval(self):
        state = {
            "question": "What is NLP?",
            "context": "",
            "answer": ""
        }

        result = retrieve_information(state)

        self.assertIn("Natural Language Processing", result["context"])


if __name__ == "__main__":
    unittest.main()