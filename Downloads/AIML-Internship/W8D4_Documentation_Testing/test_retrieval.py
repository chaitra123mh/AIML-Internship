import unittest


class TestRetrievalSystem(unittest.TestCase):

    def setUp(self):
        # Sample documents representing the indexed PDF files
        self.documents = {
            "ai.pdf": "Artificial Intelligence is the field of creating computer systems that can perform tasks that normally require human intelligence.",
            "machine_learning.pdf": "Machine Learning is a branch of Artificial Intelligence that allows computers to learn patterns from data and make predictions.",
            "deep_learning.pdf": "Deep Learning is a type of Machine Learning that uses neural networks with multiple layers to learn complex patterns.",
            "nlp.pdf": "Natural Language Processing is a field of Artificial Intelligence that helps computers understand and process human language.",
            "computer_vision.pdf": "Computer Vision is a field of Artificial Intelligence that enables computers to understand and analyze images and videos."
        }

    def test_documents_loaded(self):
        # Check that all 5 documents are available
        self.assertEqual(len(self.documents), 5)

    def test_machine_learning_document(self):
        # Check that the Machine Learning document contains expected information
        self.assertIn(
            "learn patterns from data",
            self.documents["machine_learning.pdf"]
        )

    def test_deep_learning_document(self):
        # Check that the Deep Learning document contains expected information
        self.assertIn(
            "neural networks with multiple layers",
            self.documents["deep_learning.pdf"]
        )

    def test_nlp_document(self):
        # Check that the NLP document contains expected information
        self.assertIn(
            "understand and process human language",
            self.documents["nlp.pdf"]
        )

    def test_computer_vision_document(self):
        # Check that the Computer Vision document contains expected information
        self.assertIn(
            "analyze images and videos",
            self.documents["computer_vision.pdf"]
        )


if __name__ == "__main__":
    unittest.main()