import unittest
import jira


class TestGenerateItems(unittest.TestCase):
    def test_empty_query(self):
        query = ""
        projects = ["https://jira.somewhere/jira/GBL", "http://other/jira/JIR"]

        actual = jira.generate_items(projects, query)
        expected = [{
            "title": "https://jira.somewhere/jira/GBL-",
            "subtitle": "https://jira.somewhere/jira/GBL-",
            "valid": "YES",
            "arg": "https://jira.somewhere/jira/GBL-",
            "icon": "icon.png"
        }, {
            "title": "http://other/jira/JIR-",
            "subtitle": "http://other/jira/JIR-",
            "valid": "YES",
            "arg": "http://other/jira/JIR-",
            "icon": "icon.png"
        }]

        self.assertEqual(actual, expected)

    def test_numeric_search(self):
        query = "123"
        projects = ["https://jira.somewhere/jira/GBL", "http://other/jira/JIR"]

        actual = jira.generate_items(projects, query)
        expected = [{
            "title": "https://jira.somewhere/jira/GBL-123",
            "subtitle": "https://jira.somewhere/jira/GBL-123",
            "valid": "YES",
            "arg": "https://jira.somewhere/jira/GBL-123",
            "icon": "icon.png"
        }, {
            "title": "http://other/jira/JIR-123",
            "subtitle": "http://other/jira/JIR-123",
            "valid": "YES",
            "arg": "http://other/jira/JIR-123",
            "icon": "icon.png"
        }]

        self.assertEqual(actual, expected)

    def test_project_matching_search(self):
        query = "JIR-456"
        projects = ["https://jira.somewhere/jira/GBL", "http://other/jira/JIR"]

        actual = jira.generate_items(projects, query)
        expected = [{
            "title": "http://other/jira/JIR-456",
            "subtitle": "http://other/jira/JIR-456",
            "valid": "YES",
            "arg": "http://other/jira/JIR-456",
            "icon": "icon.png"
        }]

        self.assertEqual(actual, expected)

    def test_project_prefix_search(self):
        queries = ["J", "JI", "JIR", "JIR-"]
        projects = ["https://jira.somewhere/jira/GBL", "http://other/jira/JIR"]

        for query in queries:
            actual = jira.generate_items(projects, query)
            expected = [{
                "title": "http://other/jira/JIR-",
                "subtitle": "http://other/jira/JIR-",
                "valid": "YES",
                "arg": "http://other/jira/JIR-",
                "icon": "icon.png"
            }]

            self.assertEqual(actual, expected)


class TestSendFeedback(unittest.TestCase):
    def test_init(self):
        self.assertEqual(4, 4)


class TestMain(unittest.TestCase):
    def test_init(self):
        self.assertEqual(4, 4)
