import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from module import DeusVectorMesh, cosine_similarity

class TestVectorMesh(unittest.TestCase):
    def test_similarity(self):
        v1 = [1.0, 0.0, 0.0]
        v2 = [1.0, 0.0, 0.0]
        self.assertAlmostEqual(cosine_similarity(v1, v2), 1.0)
        v3 = [0.0, 1.0, 0.0]
        self.assertAlmostEqual(cosine_similarity(v1, v3), 0.0)

    def test_sharded_cluster(self):
        mesh = DeusVectorMesh(num_shards=4)
        mesh.insert("doc1", [0.9, 0.1, 0.0], {"title": "Doc 1"})
        mesh.insert("doc2", [0.1, 0.9, 0.0], {"title": "Doc 2"})
        mesh.insert("doc3", [0.85, 0.15, 0.0], {"title": "Doc 3"})

        res = mesh.search([1.0, 0.0, 0.0], top_k=2)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0][0], "doc1")
        self.assertEqual(res[1][0], "doc3")

if __name__ == "__main__":
    unittest.main()
