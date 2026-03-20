from __future__ import annotations

import unittest

from app import handle_rpc, load_documents, rag_search


class OllamaMcpTests(unittest.TestCase):
    def test_rag_search(self) -> None:
        docs = load_documents()
        hits = rag_search("Redis Postgres", docs)
        self.assertGreaterEqual(len(hits), 1)

    def test_tools_list(self) -> None:
        docs = load_documents()
        response = handle_rpc({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}, docs)
        tool_names = [item["name"] for item in response["result"]["tools"]]
        self.assertIn("rag.search", tool_names)
        self.assertIn("agent.answer", tool_names)

    def test_agent_answer(self) -> None:
        docs = load_documents()

        def fake_ollama(question, context):
            _ = (question, context)
            return "mock answer"

        response = handle_rpc(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {"name": "agent.answer", "arguments": {"question": "What demos are available?"}},
            },
            docs,
            ollama_fn=fake_ollama,
        )

        self.assertEqual(response["result"]["content"][0]["text"], "mock answer")


if __name__ == "__main__":
    unittest.main()
